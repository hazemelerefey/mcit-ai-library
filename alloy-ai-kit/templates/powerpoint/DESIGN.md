# PowerPoint template — design notes

Reference deck: `demo-pptx-skill-test.pptx` (15 slides,
"Applied AI in Production"). This is the approved bar. Match it;
don't reinterpret it.

## Tokens

- Palette: navy `#0A1A2F`, steel `#5E6B7A`, silver `#B9C2CE`,
  light `#F4F6F8`
- Headers: Cambria · Body: Calibri
- Flat surfaces, hairline borders, restrained type scale

## Layout rules

- 16:9 (`LAYOUT_16x9` = 10" × 5.625" in PptxGenJS coordinates)
- One idea per slide, max 6 body lines
- Vary layouts across the deck: cover, agenda, section opener,
  hero stat, chart, two-column, findings, timeline, table, closing
- Charts are native PowerPoint charts with palette colors, value
  labels on, quiet axes — never screenshots

## Banned

Title underlines · edge stripes · slide numbers · gradients ·
gradient text · glassmorphism · glowing pills · purple-blue soup ·
decorative shimmer · generic icon grids · text-only slides

## QA history

Slide 15 shipped with a clipped contact line in the first render;
DeckCraft's slide render caught it and the generator was fixed.
This is why every slide gets rendered and read before delivery.
