import test from 'node:test';
import assert from 'node:assert/strict';
import { cpSync, mkdtempSync, rmSync, readFileSync, writeFileSync, mkdirSync, symlinkSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { checkPackage } from './check-package.mjs';

const root = resolve(import.meta.dirname, '..');
test('repository package passes without Git-dependent checks', () => assert.deepEqual(checkPackage(root), []));
test('published manifests preserve the Apache-2.0 repository license', () => {
  assert.match(readFileSync(join(root, 'LICENSE'), 'utf8'), /Apache License\s+Version 2\.0/);
  for (const path of ['plugin.json', '.claude-plugin/plugin.json']) assert.equal(JSON.parse(readFileSync(join(root, path))).license, 'Apache-2.0');
});
for (const broken of [false, true]) {
  test(`CLI through filesystem alias ${broken ? 'rejects missing material' : 'executes and prints success'}`, () => {
    const dir = mkdtempSync(join(tmpdir(), 'spec-it-cli-'));
    try {
      const canonical = join(dir, 'package');
      cpSync(root, canonical, { recursive: true, filter: path => !['.git', '.worktree', '__pycache__'].includes(path.split('/').at(-1)) });
      const alias = join(dir, 'alias');
      symlinkSync(canonical, alias, 'dir');
      if (broken) rmSync(join(canonical, 'rules'), { recursive: true });
      const result = spawnSync(process.execPath, [join(alias, 'scripts/check-package.mjs')], { encoding: 'utf8' });
      assert.equal(result.status, broken ? 1 : 0);
      assert.match(broken ? result.stderr : result.stdout, broken ? /missing: rules/ : /^Package structure OK: 6 skills/);
    } finally { rmSync(dir, { recursive: true, force: true }); }
  });
}
function fixture(name, mutate, expected) {
  test(name, () => {
    const dir = mkdtempSync(join(tmpdir(), 'spec-it-package-'));
    try {
      cpSync(root, dir, { recursive: true, filter: path => !['.git', '.worktree', '__pycache__'].includes(path.split('/').at(-1)) });
      mutate(dir);
      assert.ok(checkPackage(dir).some(error => error.includes(expected)), checkPackage(dir).join('\n'));
    } finally { rmSync(dir, { recursive: true, force: true }); }
  });
}
fixture('reject mismatched host package version', dir => {
  const path = join(dir, '.codex-plugin/plugin.json');
  const data = JSON.parse(readFileSync(path)); data.version = '0.7.0'; writeFileSync(path, JSON.stringify(data));
}, 'identity/version');
fixture('reject missing policy material', dir => rmSync(join(dir, 'rules'), { recursive: true }), 'missing: rules');
fixture('reject missing skill reference', dir => rmSync(join(dir, 'skills/spec-it-evolve/references/document-routing.md')), 'missing: skills/spec-it-evolve/references');
fixture('reject unpublished extra skill', dir => mkdirSync(join(dir, 'skills/spec-it-pair')), 'skill inventory');
fixture('reject broken relative skill link', dir => {
  const path = join(dir, 'skills/spec-it-check/SKILL.md'); writeFileSync(path, readFileSync(path, 'utf8') + '\n[required](missing.md)\n');
}, 'missing: skills/spec-it-check/missing.md');
fixture('reject escaping relative link', dir => {
  const path = join(dir, 'skills/spec-it-check/SKILL.md'); writeFileSync(path, readFileSync(path, 'utf8') + '\n[escape](../../../outside.md)\n');
}, 'escaped link');
fixture('reject install hook component', dir => {
  const path = join(dir, '.claude-plugin/plugin.json'); const data = JSON.parse(readFileSync(path)); data.hooks = './hooks.json'; writeFileSync(path, JSON.stringify(data));
}, 'side effect component');
fixture('reject marketplace source drift', dir => {
  const path = join(dir, '.agents/plugins/marketplace.json'); const data = JSON.parse(readFileSync(path)); data.plugins[0].source.path = './other'; writeFileSync(path, JSON.stringify(data));
}, 'marketplace source');
