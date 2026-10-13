---
name: alloy-figures
description: Professional figures and charts with AntV Infographic — offline, no API key. Declarative .ifgc DSL to SVG to PNG for placement inside reports and presentations.
---

# Figures skill (AntV Infographic)

Use for publication-grade figures and charts placed inside reports
and presentations. Data-first, restrained, serving the document —
never decoration.

## When to use

- A chart or figure needed inside a PDF report or deck.
- A standalone data infographic in the clean vector style
  (for the hand-drawn sketchnote style, use `../infograph/SKILL.md`).

## Tool

**@antv/infographic** 0.2.20 (MIT) at `~/workspace/tools/antv-infographic/`.
Offline, zero API keys. Skills: `~/workspace/skills/antv-infographic/`.

## Pipeline

1. **Write the `.ifgc` DSL.** First line: `infographic <template>`.
   Two-space indents. `data` block (title/desc + one main field like
   `lists`), `theme` block (`palette #0A1A2F #5E6B7A #B9C2CE`).
2. **Pick the template** from
   `~/workspace/mcit-doc-agent/infographic-library/samples.json`
   using each entry's `best_for` field (~200 templates).
3. **DSL → SVG:** `cd ~/workspace/tools/antv-infographic && node render-ifgc.js <in.ifgc> <out.svg>`
   (`renderToString` from `@antv/infographic/ssr` — the export is
   `./ssr`, not `./lib/ssr`).
4. **SVG → PNG:** `node shot-one.js <in.svg> <out.png>`
   (puppeteer-core + `/opt/meta-chromium/chrome`, 1200px wide).
5. **Read the PNG.** QA every render before placing the figure.

## Design tokens

- Platinum palette: `#0A1A2F #5E6B7A #B9C2CE` (+ light `#F4F6F8`).
- One accent per figure. Quiet axes, no chartjunk, tabular numbers.
- If a template hardcodes pink `#FF356A` arrows (snake/badge
  templates), `sed 's/#FF356A/#5E6B7A/g'` the SVG before screenshotting.

## Worked example

`~/workspace/mcit-ai-library/infographics/antv-free-test/toolchain-antv.{ifgc,svg,png}`
— "Our AI Toolchain, Visualized" vertical timeline, Platinum theme,
built from a 20-line `.ifgc` file. The `.ifgc` source is the
reference for DSL structure.

## Gotchas

- Icon keywords are approximate — `presentation` once rendered an
  audience icon, `document` rendered a bank icon. QA every render
  and try alternate keywords (`projector screen`, `pdf file`).
- `list-row-horizontal-icon-arrow` overlaps label+desc on top items —
  use label-only there.
- SVG references a remote font CSS; Chromium falls back cleanly
  offline, but for exact typography register a local font.
- There is no `ifgc` CLI binary — the two node scripts are the pipeline.

## References

- Agent skills: `~/workspace/skills/antv-infographic/` (+ English
  `README.md` there documenting the pipeline)
- Template gallery: `~/workspace/mcit-doc-agent/infographic-library/`
  (`gallery.html` visual browser, `samples.json` manifest)
- Tool inventory: `../../tools/TOOLS.md`
