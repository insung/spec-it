"""Guard smoke evidence against an exit-zero checker that did not execute."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest


class PluginSmokeTests(unittest.TestCase):
    @unittest.skipUnless(all(shutil.which(name) for name in ('claude', 'codex', 'node')), 'host CLIs required')
    def test_zero_exit_without_checker_output_is_rejected(self):
        root = Path(__file__).resolve().parents[1]
        real_node = shutil.which('node')
        with tempfile.TemporaryDirectory(prefix='spec-it-noop-checker-') as temporary:
            node = Path(temporary) / 'node'
            node.write_text(f'#!{sys.executable}\nimport os,sys\nif len(sys.argv)>1 and sys.argv[1].endswith("check-package.mjs"):\n sys.exit(0)\nos.execv({json.dumps(real_node)}, [{json.dumps(real_node)}, *sys.argv[1:]])\n')
            node.chmod(0o755)
            env = os.environ.copy()
            env['PATH'] = str(node.parent) + os.pathsep + env['PATH']
            result = subprocess.run([sys.executable, str(root / 'scripts/smoke-plugin-install.py')], env=env, cwd=root, capture_output=True, text=True, timeout=90)
            self.assertNotEqual(result.returncode, 0, 'empty checker stdout must not become successful cache evidence')
            self.assertIn('checker did not confirm execution', result.stderr)
