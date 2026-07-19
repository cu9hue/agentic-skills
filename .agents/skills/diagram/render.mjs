#!/usr/bin/env node
/*
 * Renders a model.json into the standalone interactive atlas.
 *
 * Usage:
 *   node render.mjs --model <model.json> [--out-dir <dir>]
 *
 * Writes into <out-dir> (defaults to the model's own directory):
 *   <system>.html            open this in a browser
 *   <system>.fragment.html   body-only, for publishing via the Artifact tool
 *
 * No dependencies. Runs under node or bun.
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

function arg(name, def) {
  const i = process.argv.indexOf('--' + name);
  return i >= 0 && i + 1 < process.argv.length ? process.argv[i + 1] : def;
}

const modelPath = arg('model');
if (!modelPath) {
  console.error('usage: node render.mjs --model <model.json> [--out-dir <dir>]');
  process.exit(1);
}

const modelFile = resolve(modelPath);
const model = JSON.parse(readFileSync(modelFile, 'utf8'));
const system = (model.meta && model.meta.system) || 'system';
const outDir = resolve(arg('out-dir', dirname(modelFile)));
mkdirSync(outDir, { recursive: true });

const template = readFileSync(join(__dirname, 'template.html'), 'utf8');
const title = (model.meta && (model.meta.title || model.meta.system)) || 'Architecture Atlas';
const icon = (model.meta && model.meta.icon) || '🗺️';

const fragment = template
  .replace('__ATLAS_TITLE__', escapeHtml(title))
  .replace('__ATLAS_ICON__', icon)
  .replace('__ATLAS_MODEL__', serializeInlineScriptJson(model));

const standalone = `<!doctype html>\n<html lang="en">\n<head>\n</head>\n<body>\n${fragment}\n</body>\n</html>\n`;

const htmlPath = join(outDir, `${system}.html`);
const fragmentPath = join(outDir, `${system}.fragment.html`);
writeFileSync(htmlPath, standalone);
writeFileSync(fragmentPath, fragment);

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// The model is injected into an inline <script>; "<" must not be able to close it.
function serializeInlineScriptJson(value) {
  return JSON.stringify(value).replace(/</g, '\\u003c');
}

console.log(JSON.stringify({
  system,
  html: htmlPath,
  fragment: fragmentPath,
  counts: {
    components: Object.keys(model.nodes || {}).length,
    edges: (model.edges || []).length,
    'state machines': (model.stateMachines || []).length,
    scenarios: (model.scenarios || []).filter((s) => s.id !== 'full').length,
    facts: (model.facts || []).length,
  },
}, null, 2));
