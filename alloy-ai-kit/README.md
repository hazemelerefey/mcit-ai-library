# Alloy AI — Document Generation Kit

A complete, opinionated toolkit for generating professional documents:
PowerPoints, PDF reports, infographics, and spreadsheet dashboards.
Every type has one main tool, one skill with the full workflow, one
approved template, and a quality bar. Nothing here is a suggestion;
these are the tested defaults.

## The four primary types

| Type | Main tool | Skill | Template |
|---|---|---|---|
| PowerPoint decks | DeckCraft + PptxGenJS | `skills/powerpoint/SKILL.md` | `templates/powerpoint/` |
| PDF reports | PdfCraft + reportlab/matplotlib | `skills/pdf-report/SKILL.md` | `templates/pdf-report/` |
| Infographics | VectorCraft + Open Doodles | `skills/infograph/SKILL.md` | `templates/infograph/` |
| Spreadsheets / dashboards | GridCraft | `skills/spreadsheet/SKILL.md` | `templates/spreadsheet/` |

Helpers:

| Helper | For | Skill |
|---|---|---|
| VectorCraft (custom vector design) | Stunning one-off designs | `skills/design-helper/SKILL.md` |
| AntV Infographic (professional figures) | Charts/figures inside reports and decks | `skills/figures/SKILL.md` |

Full tool inventory with versions, paths, and repo links:
`tools/TOOLS.md`. Type-by-type breakdown: `TYPES.md`.

## How to use this kit

1. Pick the document type. Read its skill file first, top to bottom.
2. Follow the skill's workflow exactly: tool commands, design tokens,
   build steps, QA steps.
3. Match the approved template in `templates/<type>/` — that is the
   design bar, not a starting suggestion.
4. Run the skill's QA checklist before delivery. Every artifact gets
   opened and judged. No blind handoffs.

## Role of each tool (one line)

- **DeckCraft** — renders PPTX slides to images so every slide is
  visually QA-checked before delivery.
- **PptxGenJS** — builds the .pptx file itself (DeckCraft renders it).
- **PdfCraft** — the PDF toolchain: build, edit, export documents.
- **GridCraft** — Excel workbooks with real pivot tables and pivot
  charts; never hardcoded summary tables.
- **VectorCraft** — headless vector design: custom graphics, sketchnote
  layouts, placed artwork.
- **EffectCraft** — motion graphics and 60fps video renders
  (not a document tool; listed for completeness).
- **AntV Infographic** — declarative infographic/figure engine for
  professional charts and figures (no API key, fully offline).
- **Open Doodles** — CC0 hand-drawn doodle SVG library; the artwork
  source for sketchnote infographics.

## Default designs (approved)

- **PowerPoint:** Platinum Silver — navy `#0A1A2F`, steel `#5E6B7A`,
  silver `#B9C2CE`, light `#F4F6F8`. Cambria headers, Calibri body.
  No title underlines, no edge stripes, no slide numbers, no gradients.
- **PDF report:** Platinum Silver, heavy headings, hairline rules,
  generous margins, matplotlib/AntV figures with real data. No em/en
  dashes, no source-credit lines.
- **Infographic:** sketchnote style — red `#D92626` + dark `#1A1A1A`
  on white; speech-bubble title, columns, verdict box; real hand-drawn
  doodles (CC0), never AI-generated art.
- **Spreadsheet:** the people-dataset template — real pivot tables and
  pivot charts over raw rows, KPI formulas verified against the data.

## Integration note

You decide how to integrate this kit into your project: copy the
skills into your agent's skill directory, wrap the tools behind your
own interfaces, or call the CLIs directly. The kit prescribes outputs
and quality bars, not your architecture.
