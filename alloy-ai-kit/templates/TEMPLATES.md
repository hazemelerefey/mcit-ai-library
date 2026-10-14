# Templates — Master Index

Every approved template, what it is, which tool builds it, and the
reference file the agent copies. The agent NEVER designs from scratch
when a template exists: it loads the template, edits it for the user's
request, and delivers output that matches these references.

## Presentations (PptxGenJS + DeckCraft)

| Template | File | Theme |
|---|---|---|
| 30-slide WSIS dark (approved) | `powerpoint/MCIT-WSIS-Egypt-30-DARK.pptx` | Midnight Noir dark |
| 30-slide WSIS light (approved) | `powerpoint/MCIT-WSIS-Egypt-30-LIGHT.pptx` | Midnight Noir light |

- Builders: `~/workspace/wsis-deck/build_deck.py`, `build_deck_light.py`
- Covers: `covers/cover-hero.png` / `covers/cover-end.png` (constant)
- Fonts: Nohemi (titles), Libre Franklin (body), Inter (covers)
- QA: DeckCraft render every slide before delivery
- Skill: `../../skills/powerpoint/SKILL.md`

## PDF reports (ReportLab + PdfCraft)

| Template | Reference |
|---|---|
| 7-page Noir report dark | `~/workspace/your_files/MCIT-WSIS-Report-Noir-DARK.pdf` |
| 7-page Noir report light | `~/workspace/your_files/MCIT-WSIS-Report-Noir-LIGHT.pdf` |

- Builders: `~/workspace/wsis-deck/build_report_noir_full.py`
  (full), `build_report_noir.py` (4-page sample)
- Covers: `covers/cover-hero.png` / `covers/cover-end.png` (constant)
- Structure: cover, contents, at-a-glance, 2 figure pages, findings,
  back cover — keep this structure for new reports
- Skill: `../../skills/pdf-report/SKILL.md`

## Word reports (WordCraft — editable)

| Template | Reference |
|---|---|
| 7-page Noir report dark (editable) | `~/workspace/your_files/MCIT-WSIS-Report-Noir-DARK.docx` |
| 7-page Noir report light (editable) | `~/workspace/your_files/MCIT-WSIS-Report-Noir-LIGHT.docx` |

- Driver: `~/workspace/wsis-deck/build_docx_wordcraft.py`
- Gotchas: base64 `data=` for pictures (not `path=`); `caret.docEnd`
  after `insert.picture`; `para.borders` is sticky (set after typing,
  clear after); no Tab in last table cell
- Skill: `../../skills/wordcraft/` (to be added) / TOOLS.md entry

## Infographics (VectorCraft + Open Doodles)

| Template | File |
|---|---|
| Sketchnote toolchain (approved) | `infograph/sketchnote-toolchain.png` |
| WSIS sketchnote (approved) | `infograph/wsis-sketchnote.png` |

- Driver: `~/workspace/wsis-deck/build_infographic_sketchnote.py`
- Doodles: `~/workspace/tools/sketchnote-doodles/` (CC0)
- Style: red `#D92626` / dark `#1A1A1A` on white, speech-bubble title,
  2 columns, verdict box — see `infograph/DESIGN.md`
- Skill: `../../skills/infograph/SKILL.md`

## Spreadsheets (GridCraft)

| Template | File |
|---|---|
| ICT monthly report, Noir dark | `spreadsheet/MCIT-ICT-Monthly-Report-Noir-Template.xlsx` |
| ICT full-year 2025, Noir dark | `spreadsheet/MCIT-ICT-2025-FullYear-Noir-Template.xlsx` |
| People dashboard (pivots) | `spreadsheet/file_example_XLS_5000.xls` |

- Drivers: `~/workspace/wsis-deck/build_xls_noir.py`,
  `build_xls_2025.py`, `build_xls_dashboard.py`
- Pattern: agent-as-data-entry — user pastes figures, agent enters
  them, computed columns are formulas (never typed values)
- Visual QA: `~/workspace/tools/preview_xls.sh`; charts MUST get
  `chart.changeColors` or they render grayscale
- Skill: `../../skills/spreadsheet/SKILL.md`

## Tool links (local paths)

- GridCraft: `~/workspace/tools/gridcraft/gridcraft-0.6.1-linux-x86_64/bin/gridcraft-cli`
- DeckCraft: `~/workspace/tools/deckcraft/deckcraft-0.6.1-linux-x86_64/bin/deckcraft-cli`
- PdfCraft: `~/workspace/tools/pdfcraft/pdfcraft-cli-0.7.1-linux-x86_64/bin/pdfcraft-cli`
- VectorCraft: `~/workspace/tools/vectorcraft/vectorcraft-0.10.0-linux-x86_64/bin/vectorcraft-cli`
- WordCraft: `~/workspace/tools/wordcraft/wordcraft-0.6.1-linux-x86_64/bin/wordcraft-cli`
- EffectCraft: `~/workspace/tools/effectcraft/effectcraft-0.9.2-linux-x86_64/bin/effectcraft-cli`

## How the agent works with templates (the loop)

1. User requests a file → agent picks the matching template above.
2. Agent edits a COPY for the request (never the master).
3. Agent renders QAs with the template's tool (DeckCraft PNGs,
   WordCraft render, preview_xls.sh, VectorCraft export).
4. Agent fixes issues, re-renders, then delivers.
5. Output must be visually indistinguishable in quality from the
   reference template.
