---
name: alloy-pdf-report
description: Build formal PDF reports the approved way — reportlab layout, matplotlib/AntV figures with real data, PdfCraft for PDF operations. Platinum Silver, heavy headings, hairline rules.
---

# PDF report skill

Use for formal multi-page reports (A4 portrait): cover, table of
contents, chapter openers, content pages with figures, back cover.
EN and AR editions are separate renders from the same data model.

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

## Design tokens (Platinum Silver — approved)

- Navy `#0A1A2F` · Steel `#5E6B7A` · Silver `#B9C2CE` · Light `#F4F6F8`
- Supporting neutrals: ink `#141414`, muted `#6B7280`, hairline `#E2E5EA`
- EN headings: heavy grotesque, tight tracking (Arial Black /
  Helvetica Neue; DejaVu Sans Bold as render stand-in).
  EN body: regular grotesque, 1.5 line height.
- AR headings: Noto Sans Arabic Condensed Black. AR body:
  Noto Sans Arabic Regular. Never letterspace Arabic.
- Scale (A4): Title 42 / H1 28 / H2 20 / body 11 / caption 8.5.
- Accent rule: 3px accent bar, 48px wide, under every major title.
- Banned: em/en dashes in copy, source-credit or photo-credit lines,
  gradients, glassmorphism, glowing elements.

## Structure (fixed)

1. Cover — dark surface, motif, title, date line.
2. Inside title + TOC — light surface, section list with hairline
   rules and page numbers.
3. Chapter openers — dark band + chapter number.
4. Content pages — light surface, H1 + accent rule, stat callouts,
   figures. Running header with short title, page numbers
   bottom-outer.
5. Back cover — dark surface, logo, footer line.

Margins: 22mm. One idea per page spread; figures never float
without a caption that states what the reader should see.

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
— the approved v6 formal report (EN+AR). Study its structure:
`eyebrow`, `section_head`, `data_table`, `rpt_fig`/`antv_fig`,
`body_para`, `insight_line`, `footer_line`, `logo_card` helpers;
`build(style_key, lang, out_path)` assembles the full document.
Design tokens distilled in `../templates/pdf-report/DESIGN.md`.

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

- Design notes: `../templates/pdf-report/DESIGN.md`
- Full design system: `~/workspace/mcit-doc-agent/design-system.md`
- Figures: `../figures/SKILL.md`
- Tool inventory: `../../tools/TOOLS.md`
