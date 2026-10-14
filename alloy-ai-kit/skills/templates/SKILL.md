---
name: alloy-templates
description: The master template system — every approved template, how to pick one, edit it for a user request, QA it with the right engine, and deliver output matching the approved quality. Read this before any document generation task.
---

# Templates — Master Skill

This is how you handle ALL document generation. You never design from
scratch when a template exists. You load the template, edit a COPY for
the user's request, QA it, and deliver.

## The template library

`../templates/TEMPLATES.md` is the index. Everything lives under
`../templates/`:

| What | Where | Engine |
|---|---|---|
| Presentation dark/light | `templates/powerpoint/MCIT-WSIS-Egypt-30-DARK.pptx`, `-LIGHT.pptx` | PptxGenJS + DeckCraft |
| PDF report dark/light | `templates/pdf-report/MCIT-WSIS-Report-Noir-DARK-sample.pdf`, `-LIGHT-sample.pdf` | PdfCraft (reportlab builds) |
| Word report dark/light | reference `.docx` in `~/workspace/your_files/` | WordCraft |
| Infographic sketchnote | `templates/infograph/wsis-sketchnote.png`, `sketchnote-toolchain.png` | VectorCraft + Open Doodles |
| Spreadsheet Noir | `templates/spreadsheet/MCIT-ICT-Monthly-Report-Noir-Template.xlsx`, `MCIT-ICT-2025-FullYear-Noir-Template.xlsx` | GridCraft |
| Constant covers | `templates/covers/cover-hero.png`, `cover-end.png` + `USAGE.md` | all visual formats |

## The loop (every document, every time)

1. **Pick the template** matching the user's request and theme
   (dark is default; light when asked).
2. **Copy it** — never edit the master. Work on the copy.
3. **Apply the request**: new title, new data, new sections — but
   keep the template's structure, covers, palette, and typography.
4. **QA with the engine**:
   - PPTX → DeckCraft render every slide, fix, re-render.
   - DOCX → WordCraft render every page, fix, re-render.
   - XLSX → `~/workspace/tools/preview_xls.sh`, fix, re-render.
   - PNG → VectorCraft export, view it, fix.
   - PDF → render pages, fix.
5. **Deliver** only when the output is visually indistinguishable
   in quality from the reference template.

## Covers are constant

`templates/covers/USAGE.md` — read it before any presentation or
report. The hero and end art never change. Gold ornament lives only
on covers. The logo sits on a white card, never directly on art.

## Agent-as-data-entry (spreadsheets)

The user pastes figures in the prompt; you enter them into the
period columns. Computed columns are ALWAYS formulas with
blank-guards (`=IF(D5="","",(E5-D5)/D5)`), never typed values.
See `../spreadsheet/SKILL.md` for the general example prompt.

## Theme

Midnight Noir everywhere unless the user asks otherwise:
Midnight `#010612`, Abyss `#030F1F`, Royal `#1E507A`,
Pulse `#16A6E9`, Pale Gold `#F7EF8A`, White, Silver `#B9C2CE`.
Full tokens: `templates/covers/PALETTE.md`.

## Rules

- One accent per page/slide. No gradients, no glassmorphism, no
  glowing dots, no AI-slop (see project memory).
- Nohemi titles, Libre Franklin body, Inter on covers.
- No em/en dashes in content. No source-credit lines.
- Figures use real data and get visual QA.
