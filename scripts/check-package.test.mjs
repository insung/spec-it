import test from 'node:test';
import assert from 'node:assert/strict';
import { cpSync, mkdtempSync, rmSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { checkPackage } from './check-package.mjs';

const root = resolve(import.meta.dirname, '..');
test('repository package passes without Git-dependent checks', () => assert.deepEqual(checkPackage(root), []));
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
