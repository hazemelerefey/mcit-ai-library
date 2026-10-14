---
name: alloy-pdf-report
description: Build formal PDF reports the approved way — reportlab layout, matplotlib/AntV figures with real data, PdfCraft for PDF operations. Midnight Noir dark + light themes, Nohemi headings, Libre Franklin body, hairline rules.
---

# PDF report skill

Use for formal multi-page reports (A4 portrait): cover, table of
contents, chapter openers, content pages with figures, back cover.
EN and AR editions are separate renders from the same data model.
Every report ships in two themes: Midnight Noir dark and light,
matching the presentation decks.

## When to use

Any request for a formal report, whitepaper, or multi-page PDF
document with chapters and figures.

## Tools

- **reportlab** — programmatic page layout (canvas API, A4).
- **matplotlib** — figures with real data, generated at print size.
- **AntV Infographic** — alternative figure engine; see
  `../figures/SKILL.md`.
- **PdfCraft** — `~/workspace/tools/pdfcraft/` for PDF build, edit,
  merge, and export operations.

## Design tokens (Midnight Noir — approved 2026-10-14)

Dark theme:
- Midnight `#010612` page bg · Abyss `#030F1F` panels · Royal `#1E507A`
  hairlines · Pulse `#16A6E9` data accent · Pale Gold `#F7EF8A`
  rare premium highlights only · White `#FFFFFF` text ·
  Silver `#B9C2CE` secondary text
- One accent per page; gold never dominates charts or body text;
  gold ornament lives on covers only.

Light theme:
- White `#FFFFFF` page bg · ink `#0A1628` headings ·
  body ink `#1B2C45` · muted `#5A6B82` secondary ·
  hairline `#E2E5EA` · Royal `#1E507A` eyebrows and rules ·
  Pulse `#16A6E9` data accent (large elements only; Royal for
  small text for contrast).

Both themes:
- EN headings: Nohemi Bold, tight tracking. EN body:
  Libre Franklin Regular, 1.5 line height. Eyebrows:
  Libre Franklin SemiBold, uppercase, letterspaced.
- AR headings: Noto Sans Arabic Condensed Black. AR body:
  Noto Sans Arabic Regular. Never letterspace Arabic.
- Scale (A4): Title 42 / H1 28 / H2 20 / body 11 / caption 8.5.
- Accent rule: 3px accent bar, 48px wide, under every major title.
- Banned: em/en dashes in copy, source-credit or photo-credit lines,
  gradients, glassmorphism, glowing elements, green-dot status
  indicators, dot-plus-label chips.

## Structure (fixed)

1. Cover — noir cover artwork (approved hero system), title,
   date line. Same artwork for both themes (brand bookend).
2. Inside title + TOC — theme surface, section list with hairline
   rules and page numbers.
3. Chapter openers — theme surface, eyebrow + H1 + accent rule;
   dark theme may use a Royal band.
4. Content pages — theme surface, H1 + accent rule, stat callouts,
   figures. Running header with short title, page numbers
   bottom-outer.
5. Back cover — noir cover artwork, logo, footer line.

Margins: 22mm. One idea per page spread; figures never float
without a caption that states what the reader should see.
Figure assets: generate per theme (dark figures on `#010612`,
light figures on white); reuse the 2x AntV pipeline from the
WSIS deck (`~/workspace/wsis-deck/figures*/`).

## Workflow

1. **Lock the data model.** Every figure traces to real data.
   No placeholder numbers, ever.
2. **Generate figures first** (matplotlib at 1400px+ width, or AntV
   per `../figures/SKILL.md`). Inspect each PNG before placing it.
3. **Lay out with reportlab**, following the structure above and
   the tokens. Wrap text with measured widths; never let text run
   past margins.
4. **Render the PDF, read every page.** Check overflow, widows,
   figure placement, TOC page numbers.
5. **Fix in the generator, re-render.** Deliver only after full
   visual review.

## Worked example

Code reference: `~/workspace/mcit-doc-agent/generator/build_report_v6.py`
— the v6 formal report (EN+AR, Platinum Silver era). Study its structure:
`eyebrow`, `section_head`, `data_table`, `rpt_fig`/`antv_fig`,
`body_para`, `insight_line`, `footer_line`, `logo_card` helpers;
`build(style_key, lang, out_path)` assembles the full document.
Midnight Noir reference implementation (dark + light):
`~/workspace/wsis-deck/build_report_noir.py` (4-page sample),
`~/workspace/wsis-deck/build_report_noir_full.py` (7-page full report,
the v6 page structure: cover, contents, at-a-glance, 2 figure pages,
findings, back cover) with outputs
`~/workspace/your_files/MCIT-WSIS-Report-Noir-DARK.pdf` and
`...-LIGHT.pdf`. Covers are CONSTANT:
`../../templates/covers/cover-hero.png` /
`cover-end.png` — see `../../templates/covers/USAGE.md`.
Design tokens distilled in `../../templates/pdf-report/DESIGN.md`.

## Gotchas

- reportlab text does not wrap automatically — measure with
  `stringWidth` and wrap manually.
- Matplotlib default styles look cheap: set the palette, quiet the
  spines, and size for print (1400×500 for full-width slide-style
  figures; A4 column width for report figures).
- Arabic needs proper reshaping (arabic_reshaper + python-bidi) and
  mirrored layouts; test with real Arabic copy, not lorem ipsum.
- Embed or outline fonts the reader may not have.

## References

- Design notes: `../../templates/pdf-report/DESIGN.md`
- Full design system: `~/workspace/mcit-doc-agent/design-system.md`
- Figures: `../figures/SKILL.md`
- Tool inventory: `../../tools/TOOLS.md`
