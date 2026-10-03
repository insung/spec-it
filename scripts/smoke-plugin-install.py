"""Model-free local installation/discovery smoke; only temporary child env changes."""
import hashlib
import json
import os
from pathlib import Path
import selectors
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parent.parent
EXPECTED = sorted(f'spec-it-{name}' for name in ('check', 'clarify', 'converge', 'evolve', 'impact', 'specify'))


def fingerprints():
    # Compare contents without copying or displaying user settings or credentials.
    paths = [ROOT / 'VERSION', ROOT / 'AGENTS.md', ROOT / '.architecture/manifest.yaml', ROOT / '.architecture/lock.yaml']
    paths += list((ROOT / 'rules').rglob('*'))
    user = Path.home()
    codex = Path(os.environ.get('CODEX_HOME', user / '.codex'))
    claude = Path(os.environ.get('CLAUDE_CONFIG_DIR', user / '.claude'))
    paths += [codex / name for name in ('config.toml', 'plugins/installed_plugins.json', 'plugins/marketplaces.json')]
    paths += [claude / name for name in ('settings.json', 'plugins/installed_plugins.json', 'plugins/known_marketplaces.json')]
    paths += [user / '.claude.json']
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None for path in paths if not path.is_dir()}


def discovery(env, cwd):
    process = subprocess.Popen(['codex', 'app-server'], env=env, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ)
    pending = b''

    def send(payload):
        process.stdin.write(json.dumps(payload).encode() + b'\n')
        process.stdin.flush()

    def rpc(identifier, method, params):
        nonlocal pending
        send(dict(id=identifier, method=method, params=params))
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            while b'\n' in pending:
                line, pending = pending.split(b'\n', 1)
                message = json.loads(line)
                if message.get('id') == identifier:
                    if 'error' in message:
                        raise RuntimeError(f'{method}: {message["error"]}')
                    return message['result']
            if selector.select(1):
                chunk = os.read(process.stdout.fileno(), 65536)
                if not chunk:
                    raise RuntimeError('app-server closed before response')
                pending += chunk
        raise TimeoutError(method)

    try:
        rpc(1, 'initialize', {'clientInfo': {'name': 'spec-it-install-smoke', 'version': '0.1.0'}, 'capabilities': {'experimentalApi': True}})
        send({'method': 'initialized'})
        result = rpc(2, 'skills/list', {'cwds': [str(cwd)], 'forceReload': True})
        skills = []
        for group in result['data']:
            if group.get('errors'):
                raise RuntimeError('skills/list returned discovery errors')
            skills.extend(skill for skill in group['skills'] if skill.get('pluginId') == 'spec-it@spec-it')
        assert sorted(skill['name'] for skill in skills) == [f'spec-it:{name}' for name in EXPECTED]
        assert all(skill['enabled'] for skill in skills)
        return skills
    finally:
        selector.close()
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()


def main():
    before = fingerprints()
    report = {'time': datetime.now(timezone.utc).isoformat(), 'source': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(), 'commands': [], 'representativeInvocation': 'human-review: model execution not run'}
    with tempfile.TemporaryDirectory(prefix='spec-it-plugin-smoke-') as temporary:
        tmp = Path(temporary)
        # Allowlist; no credential environment, global configuration or credential copying.
        env = {key: os.environ[key] for key in ('PATH', 'TMPDIR', 'LANG', 'LC_ALL', 'SYSTEMROOT') if key in os.environ}
        env.update(HOME=str(tmp), CLAUDE_CONFIG_DIR=str(tmp / 'claude'), CODEX_HOME=str(tmp / 'codex'), XDG_CONFIG_HOME=str(tmp / 'xdg'))
        (tmp / 'claude').mkdir()
        (tmp / 'codex').mkdir()
        package = tmp / 'package'
        package.mkdir()
        # Export the exact tracked commit, never concurrent ignored/untracked skills.
        archive = subprocess.check_output(['git', 'archive', 'HEAD'], cwd=ROOT)
        subprocess.run(['tar', '-x', '-C', str(package)], input=archive, check=True)

        def run(args):
            result = subprocess.run(args, cwd=tmp, env=env, capture_output=True, text=True, timeout=40)
            report['commands'].append({'command': [str(arg).replace(str(tmp), '<temporary>') for arg in args], 'exit': result.returncode})
            if result.returncode:
                raise RuntimeError(f'{args[0:3]} failed: {result.stderr[:500]}')
            return result.stdout

        report['versions'] = {'claude': run(['claude', '--version']).strip(), 'codex': run(['codex', '--version']).strip(), 'node': run(['node', '--version']).strip()}
        run(['node', str(package / 'scripts/check-package.mjs')])
        run(['claude', 'plugin', 'marketplace', 'add', str(package)])
        run(['claude', 'plugin', 'install', 'spec-it@spec-it'])
        details = run(['claude', 'plugin', 'details', 'spec-it@spec-it'])
        assert 'Skills (6)' in details and all(name in details for name in EXPECTED)
        assert all(f'{kind} (0)' in details for kind in ('Agents', 'Hooks', 'MCP servers', 'LSP servers'))
        report['claudeSkills'] = EXPECTED
        run(['codex', 'plugin', 'marketplace', 'add', str(package), '--json'])
        installed = json.loads(run(['codex', 'plugin', 'add', 'spec-it@spec-it', '--json']))
        skills = discovery(env, tmp)
        report['codexSkills'] = [skill['name'] for skill in skills]
        for skill in skills:
            assert Path(skill['path']).resolve().is_relative_to(Path(installed['installedPath']).resolve())
        # Check actual cached packages, including mandatory skill references and resources.
        claude_manifests = list((tmp / 'claude/plugins/cache/spec-it').rglob('.claude-plugin/plugin.json'))
        assert len(claude_manifests) == 1
        for cached in (Path(installed['installedPath']), claude_manifests[0].parent.parent):
            run(['node', str(cached / 'scripts/check-package.mjs')])
        report['cachedReferences'] = 'pass: both cached repository-root packages checked'
    report['preservedFiles'] = before == fingerprints()
    assert report['preservedFiles'], 'user settings or policy files changed'
    report['temporaryEnvironmentRemoved'] = True
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
