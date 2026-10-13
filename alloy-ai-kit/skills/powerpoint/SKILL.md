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

## Design tokens (Platinum Silver — approved)

- Navy `#0A1A2F` · Steel `#5E6B7A` · Silver `#B9C2CE` · Light `#F4F6F8`
- Headers: Cambria · Body: Calibri
- Flat surfaces, hairline borders, restrained type scale
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

Approved 15-slide test deck: `../../templates/powerpoint/demo-pptx-skill-test.pptx`
("Applied AI in Production") with `../../templates/powerpoint/DESIGN.md`.
It demonstrates: Platinum Silver theme, Cambria/Calibri pairing,
native charts with palette colors, varied layouts, and the
build → render → fix loop (a clipped contact line on slide 15 was
caught in QA and fixed before delivery).

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
