# MCIT AI Library Skill

Use this skill whenever generating a visual deliverable: presentations,
infographics, reports, whiteboards, forms/surveys, charts, documents,
or any other templated content.

## Step 1 — Pick a template

Read `~/workspace/mcit-ai-library/templates.json`. Match the request to:
- `category` — the deliverable type (presentations, infographics, ...).
- `name` — keywords describing the topic or layout.

Each entry has `name`, `url` (Visme template page), and `thumbnail`
(preview image URL). Open the thumbnail to see the layout.

## Step 2 — Pick the generator

Read `~/workspace/mcit-ai-library/free-tools-research.md`, find the
template's category, and use the listed free/open-source tool:

- presentations → pptx skill + DeckCraft (main toolchain, see below) / PptxGenJS / python-pptx
- infographics → antvis/Infographic (.ifgc) / Satori
- reports → Typst / WeasyPrint / ReportLab
- charts & graphs → Apache ECharts / Vega-Lite / Matplotlib
- whiteboards → tldraw SDK / Excalidraw
- forms & surveys → SurveyJS
- documents → Typst / docx
- social media graphics → Satori / Pillow

## Step 3 — Customize professionally

Follow the template's **structure**: layout, section order, visual
hierarchy, and information density. Do NOT copy its artwork, stock
photos, or text content.

Apply in order:
1. The user's real data and copy (never lorem ipsum in final output).
2. MCIT Platinum theme (`#0A1A2F` navy, `#5E6B7A` steel, `#B9C2CE`
   silver, `#F4F6F8` light) unless the user specifies otherwise.
3. The user's standing design rules: no em/en dashes in prose, no
   gradient text, no glowing pills, no glassmorphism, no decorative
   gradient soup, sharp professional layouts.
4. Arabic deliverables are genuinely RTL: mirrored layout, right
   alignment, Arabic reshaping where the renderer needs it.

## Hard constraints (learned from corrections — never violate)

### Fonts
- ALWAYS use the user's font library: **Nohemi** for headings,
  **Public Sans** for body text.
  Source: https://github.com/hazemelerefey/ui-ux-library/tree/main/fonts
- Set these font names in every deliverable. No exceptions.

### Text readability
- Body text NEVER below 20pt. Headings 40pt+.
- Every word must be easily readable at normal viewing distance.
- If text looks small in review, regenerate bigger. Do not ship it.

### Figures
- ALWAYS generate figures with proper tools (AntV via mcp-server-chart,
  ECharts, or Matplotlib). NEVER draw charts as manual shapes.
- Figure text must be big and clear: generate charts at 900x550 so
  labels render proportionally large. Verify by opening the image.
- NEVER reuse the same chart type twice in one deliverable. Vary:
  column, bar, line, pie, area, scatter — pick different types per figure.
- Match figure colors to the deliverable theme.

### Completeness
- Generate ALL slides/pages of the template structure. Never a subset.
- Reports: LONG detailed content, never brief. Full paragraphs,
  findings, analysis — not bullet-point summaries.

### Review
- Open and judge every figure image yourself before embedding.
- Open and judge the final output yourself before handing it over.
- If anything is small, duplicated, or off-theme, fix it before delivery.

### Design assets (VectorCraft)
- Design real vector assets for heroes, covers, footers, and dividers
  using VectorCraft (`~/workspace/tools/vectorcraft/`), never weak
  CSS-only decorations.
- Asset library lives at `~/workspace/mcit-ai-library/assets/`:
  `mcit-hero.svg`, `mcit-cover.svg`, `mcit-footer.svg`,
  `mcit-divider.svg`, `mcit-corner.svg` — all in Platinum Silver.
- Design in VectorCraft CLI (`vectorcraft-cli run --cmd ... --export`),
  export SVG + PNG, preview before use.
- Embed assets in presentations (python-pptx) and reports (WeasyPrint)
  as real designed artwork.

### Spreadsheets and dashboards (GridCraft)
- ALWAYS use GridCraft (`~/workspace/tools/gridcraft/`, CLI `gridcraft-cli`)
  for dashboards and spreadsheets. Never build dashboard web apps when
  the user asks for Excel-style dashboards.
- Design dashboards using `~/workspace/skills/design-dashboards/` principles:
  KPIs with context (not raw numbers), horizontal bars for ranking,
  bars not pies, clean vertical layout, restrained color, one accent.
- Style in Platinum Silver: navy headers (#0A1A2F), steel accents (#5E6B7A).
- Use real formulas (percentages as =B10/5000), native charts (`insert.chart`),
  formatted tables with percentage number formats.
- Set landscape orientation for dashboards. Keep to 3 columns (A:C) max
  for clean PDF rendering. Verify with LibreOffice PDF export before delivery.
- Dashboard demo: `demo-people-dashboard.xlsx`.

## Presentations: main toolchain (pptx skill + DeckCraft)

Standing rule: for all PowerPoint work, ALWAYS use the `pptx` skill
(`~/workspace/skills/pptx/`, from anthropics/skills) together with DeckCraft
(`~/workspace/tools/deckcraft/`, CLI `deckcraft-cli`). This is the main
skill and tool combo for designing decks.

- Create new decks with `pptxgenjs` per the skill's gotchas: set
  `pres.layout` first, 6-digit hex without `#`, fresh option objects
  (never shared), `margin: 0` on text boxes, native charts via `addChart`.
- Design per skill principles: bold content-informed palette, dark/light
  sandwich structure, one repeating visual motif (never accent stripes
  or title underlines), every slide carries a visual element, vary
  layouts across slides, safe fonts (Cambria headers + Calibri body).
- QA with `deckcraft-cli render` on every slide; fix overflow, overlaps,
  and clipping before delivery. Skill's `validate.py` for file integrity.
- Test deck proving the toolchain: `demo-pptx-skill-test.pptx` (15 slides).

## Motion graphics: main toolchain (EffectCraft + video-motion-graphics skill)

Standing rule: for motion graphics and video animation work, ALWAYS use
EffectCraft (`~/workspace/tools/effectcraft/`, v0.9.2, CLI `effectcraft-cli`)
together with the `video-motion-graphics` skill
(`~/workspace/skills/video-motion-graphics/`, from
dylantarre/animation-principles). This is the main skill and tool combo
for motion design.

- EffectCraft: open-source After Effects reimplementation in Rust.
  CLI supports comp/layer/keyframe commands and headless rendering.
  Check `effectcraft-cli commands` for the current API (young, moving fast).
- Skill applies Disney's 12 animation principles to motion graphics:
  anticipation, slow in/out (never linear), squash & stretch (overshoot),
  follow through (stagger), staging, arcs, secondary action, timing,
  exaggeration, solid drawing, appeal.
- Standing rule: all video output at 60fps.
- Test piece: `demo-motion-graphics-60fps.mp4`.
