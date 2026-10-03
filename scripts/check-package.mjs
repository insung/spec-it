import { readFileSync, readdirSync, statSync, existsSync, realpathSync } from 'node:fs';
import { resolve, dirname, relative, join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const skillNames = ['spec-it-check', 'spec-it-clarify', 'spec-it-converge', 'spec-it-evolve', 'spec-it-impact', 'spec-it-specify'];

// Runs against a filesystem export too: no Git or installed-host dependency.
export function checkPackage(root) {
  root = realpathSync(root);
  const errors = [];
  const requirePath = (path) => {
    const target = resolve(root, path);
    if (!existsSync(target)) { errors.push(`missing: ${path}`); return false; }
    if (relative(root, realpathSync(target)).startsWith('..')) { errors.push(`outside package: ${path}`); return false; }
    return true;
  };
  const readJson = (path) => {
    if (!requirePath(path)) return {};
    try { return JSON.parse(readFileSync(resolve(root, path), 'utf8')); }
    catch { errors.push(`invalid JSON: ${path}`); return {}; }
  };
  const common = readJson('plugin.json');
  for (const path of ['plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json']) {
    const data = path === 'plugin.json' ? common : readJson(path);
    if (data.name !== 'spec-it' || data.version !== '0.1.0') errors.push(`identity/version: ${path}`);
    for (const key of ['hooks', 'mcpServers', 'scripts']) if (key in data) errors.push(`side effect component: ${path}:${key}`);
  }
  if (readJson('.codex-plugin/plugin.json').skills !== './skills/') errors.push('Codex skills path');
  for (const path of ['.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json']) {
    const data = readJson(path);
    const plugins = data.plugins;
    if (data.name !== 'spec-it' || !Array.isArray(plugins) || plugins.length !== 1 || plugins[0]?.name !== 'spec-it') errors.push(`marketplace identity: ${path}`);
    const source = plugins?.[0]?.source;
    if (path.startsWith('.claude') ? source !== '.' : source?.source !== 'local' || source?.path !== './') errors.push(`marketplace source: ${path}`);
  }
  for (const path of ['VERSION', 'rules/README.md', 'profiles/README.md', 'schemas', 'templates/project', 'skills/spec-it-evolve/references/document-routing.md']) requirePath(path);
  if (requirePath('VERSION') && readFileSync(join(root, 'VERSION'), 'utf8').trim() !== '0.7.0') errors.push('policy version changed');
  if (requirePath('skills')) {
    const actual = readdirSync(join(root, 'skills')).filter(name => statSync(join(root, 'skills', name)).isDirectory()).sort();
    if (JSON.stringify(actual) !== JSON.stringify(skillNames)) errors.push(`skill inventory: ${actual.join(',')}`);
  }
  for (const name of skillNames) {
    const path = `skills/${name}/SKILL.md`;
    if (requirePath(path) && !new RegExp(`^name: ${name}$`, 'm').test(readFileSync(join(root, path), 'utf8'))) errors.push(`skill name: ${name}`);
  }
  const seen = new Set();
  function walk(path) {
    if (!requirePath(path)) return;
    const target = join(root, path);
    const canonical = realpathSync(target);
    if (seen.has(canonical)) return;
    seen.add(canonical);
    if (statSync(target).isDirectory()) { for (const name of readdirSync(target)) walk(join(path, name)); return; }
    if (!path.endsWith('.md')) return;
    const content = readFileSync(target, 'utf8').replace(/```[\s\S]*?```/g, '');
    for (const match of content.matchAll(/\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)/g)) {
      const link = match[1].replace(/^<|>$/g, '').split('#')[0];
      if (!link || /^[a-z][a-z0-9+.-]*:/i.test(link)) continue;
      // The AGENTS template points at artifacts created in the adopting project.
      if (path === 'templates/project/AGENTS.md' && ['.architecture/project.md', '.architecture/manifest.yaml', '.architecture/lock.yaml', '.architecture/decisions/', '.architecture/changes/'].includes(link)) continue;
      const dest = relative(root, resolve(dirname(target), decodeURIComponent(link)));
      if (dest.startsWith('..') || dest.startsWith('/')) errors.push(`escaped link: ${path} -> ${link}`);
      else if (requirePath(dest)) walk(dest);
    }
  }
  // All policy and template resources are retained in the repository-root package.
  for (const path of ['skills', 'rules', 'profiles', 'schemas', 'templates']) walk(path);
  return errors;
}

if (process.argv[1] && realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url))) {
  const errors = checkPackage(process.argv[2] || resolve(dirname(fileURLToPath(import.meta.url)), '..'));
  if (errors.length) { console.error(errors.join('\n')); process.exitCode = 1; }
  else console.log('Package structure OK: 6 skills, package 0.1.0, policy 0.7.0. Host execution is not verified by this check.');
}
