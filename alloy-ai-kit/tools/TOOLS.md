# Tool inventory

Every tool in the kit: version, local path, repo, role. All paths
below were verified on 2026-10-13.

## Document tools

### GridCraft — xls reports and dashboards
- Version: ~0.6.1
- Path: `~/workspace/tools/gridcraft/` (CLI: `gridcraft-cli`)
- Repo: https://github.com/storytold/gridcraft
- Role: main tool for spreadsheets and dashboards. Builds real pivot
  tables and pivot charts; never hardcoded summaries.

### DeckCraft — PowerPoint render and visual QA
- Version: 0.6.1
- Path: `~/workspace/tools/deckcraft/deckcraft-0.6.1-linux-x86_64/bin/deckcraft-cli`
- Repo: https://github.com/storytold/deckcraft
- Role: main tool for PowerPoints. Renders every slide to PNG so
  decks are QA-checked visually before delivery. Pairs with
  PptxGenJS, which constructs the .pptx file.

### PptxGenJS — pptx construction library
- Version: npm `pptxgenjs` (pinned per project)
- Path: npm package (project-local `node_modules`)
- Repo: https://github.com/gitbrent/pptxgenjs
- Role: builds the .pptx itself — slides, shapes, native charts,
  text. Always paired with DeckCraft for rendering and QA.

### PdfCraft — PDF build, edit, export
- Version: 0.7.1
- Path: `~/workspace/tools/pdfcraft/`
- Repo: https://github.com/storytold/pdfcraft
- Role: main PDF tool. Works alongside reportlab (programmatic
  layout) and matplotlib (figures) for formal reports.

### VectorCraft — vector design and infographic layout
- Version: 0.10.0
- Path: `~/workspace/tools/vectorcraft/` (CLI:
  `vectorcraft-0.10.0-linux-x86_64/bin/vectorcraft-cli`)
- Repo: https://github.com/storytold/vectorcraft
- Role: main tool for designs and infographics. Headless CLI:
  artboards, shapes, text, placed artwork, PNG/SVG export. Also the
  layout engine for sketchnote infographics.

### EffectCraft — motion graphics (reference only)
- Version: 0.9.2
- Path: `~/workspace/tools/effectcraft/effectcraft-0.9.2-linux-x86_64/bin/effectcraft-cli`
- Repo: https://github.com/storytold/effectcraft
- Role: motion graphics and 60fps video. Not a document tool;
  listed so the kit inventory is complete.

### WordCraft — Word documents (editable reports)
- Version: 0.6.1
- Path: `~/workspace/tools/wordcraft/wordcraft-0.6.1-linux-x86_64/bin/wordcraft-cli`
- Repo: https://github.com/storytold/wordcraft
- Role: main tool for editable Word reports (.docx). Headless `run`
  executes a `--cmd 'id={json}'` command sequence, then `--save`.
  `render --page N` QA-checks every page to PNG before delivery.
- Gotchas (verified 2026-10-14): `insert.picture` with `path=` is
  broken in headless run — use base64 `data=` instead (keep each
  arg under ~120KB, MAX_ARG_STRLEN). `text.newParagraph`
  immediately after `insert.picture` deletes the picture — move the
  caret first (`caret.docEnd`). `para.borders` is sticky: set it
  AFTER `text.insert` and clear with `{"kind":"none"}` or it leaks
  onto every following paragraph. Tab in the last table cell
  creates a new row — skip the trailing Tab. Tab navigates table
  cells; `caret.down` exits a table to its trailing paragraph.
  Driver example: `~/workspace/wsis-deck/build_docx_wordcraft.py`.

## Figure and artwork tools

### AntV Infographic — professional figures
- Version: 0.2.20 (MIT)
- Path: `~/workspace/tools/antv-infographic/` (npm `@antv/infographic`)
- Repo: https://github.com/antvis/Infographic
- Role: declarative infographic/figure engine. ~200 templates,
  offline, no API key. Produces charts and figures for placement
  inside reports and presentations.
- Pipeline: `.ifgc` DSL → SVG (`node render-ifgc.js`, `renderToString`
  from `@antv/infographic/ssr`) → PNG (`node shot-one.js`,
  puppeteer-core + meta-chromium).

### Open Doodles — hand-drawn doodle artwork
- Version: n/a (art library)
- Path: `~/workspace/tools/sketchnote-doodles/` (17 SVGs)
- Source: https://www.opendoodles.com — Pablo Stanley, CC0 public
  domain, free for any use, no attribution required.
- Role: the artwork source for sketchnote infographics. Real
  hand-drawn doodles, placed into VectorCraft layouts. Zero image
  APIs involved.

## Supporting skills (agent playbooks)

| Skill | Path | Source |
|---|---|---|
| pptx | `~/workspace/skills/pptx/` | proprietary (Anthropic) |
| design-dashboards | `~/workspace/skills/design-dashboards/` | workspace |
| video-motion-graphics | `~/workspace/skills/video-motion-graphics/` | https://github.com/dylantarre/animation-principles |
| infographic (hand-drawn HOW X WORKS) | `~/workspace/skills/infographic/` | https://github.com/amigoscode/infographics-skill (MIT) |
| antv-infographic | `~/workspace/skills/antv-infographic/` | https://github.com/antvis/Infographic (MIT) |

## Version notes

- The storytold "Craft" tools (Grid/Deck/Effect/Pdf/Vector) are young
  and move fast. Re-check `*-cli commands` / `help` when a command
  fails; the API surface changes between minor versions.
- Keep binaries under `~/workspace/` so they survive VM rebuilds.
