# Document types

One section per type: purpose, main tool, supporting skill, template,
default design, quality bar.

---

## 1. PowerPoint decks

- **Purpose:** slide decks, pitch decks, presentations — 10 to 15
  slides, one idea per slide.
- **Main tool:** PptxGenJS builds the .pptx; DeckCraft
  (`deckcraft-cli`) renders every slide to PNG for visual QA.
- **Skill:** `skills/powerpoint/SKILL.md`
- **Template:** `templates/powerpoint/demo-pptx-skill-test.pptx`
  (15 slides, "Applied AI in Production") + `DESIGN.md`.
- **Default design:** Platinum Silver — navy `#0A1A2F`, steel
  `#5E6B7A`, silver `#B9C2CE`, light `#F4F6F8`. Cambria headers,
  Calibri body. Flat surfaces, hairline borders. No title underlines,
  no edge stripes, no slide numbers, no gradients, no glassmorphism.
- **Quality bar:** every slide rendered with DeckCraft and inspected;
  no text overflow, no clipped content, no repetitive layouts, no
  text-only slides. Charts are native PowerPoint charts with the
  palette applied, never screenshots.

---

## 2. PDF reports

- **Purpose:** formal multi-page reports (A4 portrait): cover, TOC,
  chapters, figures, back cover. EN and AR editions supported.
- **Main tool:** PdfCraft for PDF build/edit/export; reportlab for
  programmatic layout, matplotlib for figures.
- **Skill:** `skills/pdf-report/SKILL.md`
- **Template:** `templates/pdf-report/DESIGN.md` (tokens + structure;
  code reference: `~/workspace/mcit-doc-agent/generator/build_report_v6.py`).
- **Default design:** Platinum Silver, heavy grotesque headings,
  hairline rules, 22mm margins, page numbers bottom-outer, running
  header on content pages. Figures carry real data, generated at
  print size.
- **Quality bar:** every figure traceable to real data; no em/en
  dashes in copy; no source-credit or photo-credit lines; every page
  opened and judged before delivery.

---

## 3. Infographics

- **Purpose:** one-page visual explainers — sketchnote style is the
  default.
- **Main tool:** VectorCraft headless CLI for layout; Open Doodles
  (CC0) SVGs for hand-drawn artwork. Zero image-generation APIs.
- **Skill:** `skills/infograph/SKILL.md`
- **Template:** `templates/infograph/sketchnote-toolchain.png` +
  `DESIGN.md`.
- **Default design:** sketchnote — red `#D92626` + dark `#1A1A1A`
  on white; speech-bubble title, column layout with dividers,
  numbered badges, curved arrows, verdict box; real hand-drawn
  doodles placed near the text they illustrate.
- **Quality bar:** dense but never cluttered; no overlap, no clipped
  doodles, no orphaned arrows. Doodles match their concept by vibe.
- **Alternatives (not default):** hand-drawn "HOW X WORKS" via the
  infographic skill (needs image pipeline); clean vector diagrams via
  AntV Infographic (`skills/figures/SKILL.md`).

---

## 4. Spreadsheets / dashboards

- **Purpose:** xls reports and dashboards over raw row data.
- **Main tool:** GridCraft — real pivot tables and pivot charts.
- **Skill:** `skills/spreadsheet/SKILL.md`
- **Template:** `templates/spreadsheet/file_example_XLS_5000.xls`
  (5,000-row people dataset) + `TEMPLATE.md`.
- **Default design:** front Dashboard sheet with KPI formulas bound
  to the data, pivot sheets with bound pivot charts, verified totals.
- **Quality bar:** pivots are genuine (built by the tool, not
  Python-computed static tables); KPI formulas verified against raw
  data; every sheet opened and reviewed before delivery.

---

## 5. Design helper (VectorCraft)

- **Purpose:** stunning custom vector designs that don't fit a type
  template — covers, diagrams, one-off graphics.
- **Main tool:** VectorCraft headless CLI.
- **Skill:** `skills/design-helper/SKILL.md`
- **Rule:** reach for it when the type tools can't express the
  design; never as a substitute for a type's main tool.

---

## 6. Professional figures (AntV Infographic)

- **Purpose:** publication-grade figures and charts placed inside
  reports and presentations.
- **Main tool:** @antv/infographic (MIT, offline, no API key).
- **Skill:** `skills/figures/SKILL.md`
- **Rule:** figures are data-first and restrained; they serve the
  document, never decorate it.
