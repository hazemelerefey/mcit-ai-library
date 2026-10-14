---
name: alloy-powerpoint
description: Build professional PowerPoint decks the approved way — PptxGenJS constructs the .pptx, DeckCraft renders every slide for visual QA. Platinum Silver design, no AI-slop.
---

# PowerPoint skill

Use for every .pptx deck: pitch decks, presentations, slide reports.
The workflow is fixed: construct with PptxGenJS, render with DeckCraft,
fix everything the render shows, deliver only after visual review.

## When to use

Any request involving slides or a .pptx file — creating, editing,
restyling, or extracting content from one.

## Tools

- **PptxGenJS** (npm `pptxgenjs`) — constructs the deck: slides,
  shapes, text, native charts.
- **DeckCraft** — `~/workspace/tools/deckcraft/deckcraft-0.6.1-linux-x86_64/bin/deckcraft-cli`
  renders slides to PNG for QA: `deckcraft-cli render deck.pptx --all --scale 2 out/`
- Supporting playbook: `~/workspace/skills/pptx/SKILL.md` (construction
  gotchas, editing existing decks, validation).

## Design tokens (Midnight Noir — approved 2026-10-14, derived from the noir hero cover)

- Midnight `#010612` · Abyss `#030F1F` · Royal `#1E507A` · Pulse `#16A6E9` · Pale Gold `#F7EF8A` · White `#FFFFFF` · Silver `#B9C2CE`
- Dark slides by default. One accent per slide: Pulse for data, Pale Gold for premium moments, never both competing.
- Pale Gold: ornaments and single highlights only, never charts or body text.
- The gold divider ornament lives in cover backgrounds only, never inside slides. No generic shape slop.
- Headers/body: Inter · Flat surfaces, hairline borders, restrained type scale
- Banned: title underlines, edge stripes, slide numbers, gradients,
  gradient text, glassmorphism, glowing pills, purple-blue soup,
  decorative shimmer, generic icon grids

## Workflow

1. **Plan the deck.** 10–15 slides for a full deck. One idea per
   slide, max 6 body lines. Vary layouts: cover, agenda, section
   opener, hero stat, chart, two-column, findings, timeline, table,
   closing. Never two identical layouts in a row.
2. **Build with PptxGenJS.** Set `pres.layout` before adding slides
   (`LAYOUT_16x9` = 10" × 5.625"). Hex colors without `#`, 6 digits.
   Never share option objects between `add*` calls (the library
   mutates them). Charts: native `addChart()` with `chartColors`
   from the palette, `showValue: true`, quiet axes. See
   `~/workspace/skills/pptx/SKILL.md` for the full gotcha list.
3. **Render every slide.** `deckcraft-cli render deck.pptx --all --scale 2 out/`
4. **Read every render.** Check: text overflow, clipped content,
   misaligned shapes, repetitive layouts, empty-looking slides.
5. **Fix in the generator, re-render.** Never hand-edit the packed
   XML for layout fixes; fix the script so the fix is repeatable.
6. **Validate.** `python ~/workspace/skills/pptx/scripts/office/validate.py deck.pptx`
   (needs `defusedxml`; if unavailable, rely on the DeckCraft renders).
7. **Deliver** only after all slides pass visual review.

## Worked example

APPROVED templates (Midnight Noir, the current standard):
`../../templates/powerpoint/MCIT-WSIS-Egypt-30-DARK.pptx` and
`MCIT-WSIS-Egypt-30-LIGHT.pptx` (30 slides each, WSIS+10 Egypt).
They demonstrate: Midnight Noir theme, Nohemi titles + Libre Franklin
body, constant cover art (`../../templates/covers/cover-hero.png` /
`cover-end.png` — see `../../templates/covers/USAGE.md`), 2x AntV
figures, one accent per slide, and the build → render → fix loop.
Builders: `~/workspace/wsis-deck/build_deck.py` (dark),
`build_deck_light.py` (light). The studio offers a dark/light option;
both themes share structure, only the palette flips.

## Gotchas

- Coordinates past the slide edge are written, not clamped — the
  shape silently vanishes. Double-check the layout size first.
- `dataLabelPosition: "outEnd"` on stacked bars corrupts the file;
  use `ctr`, `inEnd`, or `inBase`.
- Combo charts with a secondary axis need both `valAxes` and
  `catAxes` declared, or PowerPoint discards the chart.
- `margin: 0` on text boxes that must align with shapes.
- One `new pptxgen()` per output file.

## References

- Template + design notes: `../../templates/powerpoint/`
- Construction playbook: `~/workspace/skills/pptx/SKILL.md`
- Tool inventory: `../../tools/TOOLS.md`
