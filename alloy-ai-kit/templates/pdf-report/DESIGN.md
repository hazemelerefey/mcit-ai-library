# PDF report template — design notes

Code reference: `~/workspace/mcit-doc-agent/generator/build_report_v6.py`
(the approved v6 formal report, EN+AR). Full visual spec:
`~/workspace/mcit-doc-agent/design-system.md`.

## Tokens

- Palette: navy `#0A1A2F`, steel `#5E6B7A`, silver `#B9C2CE`,
  light `#F4F6F8`; neutrals ink `#141414`, muted `#6B7280`,
  hairline `#E2E5EA`
- EN headings: heavy grotesque, tight tracking (Arial Black /
  Helvetica Neue; DejaVu Sans Bold as render stand-in)
- AR headings: Noto Sans Arabic Condensed Black; AR body:
  Noto Sans Arabic Regular (never letterspace Arabic)
- Scale (A4): Title 42 / H1 28 / H2 20 / body 11 / caption 8.5
- Accent rule: 3px bar, 48px wide, under every major title
- Margins 22mm; page numbers bottom-outer; running header on
  content pages

## Structure

Cover (dark) → inside title + TOC (light, hairline rules) →
chapter openers (dark band + number) → content pages (light, H1 +
accent rule, stat callouts, figures) → back cover (dark).

## Rules

- Every figure carries real data, generated at print size
  (matplotlib 1400px+ or AntV per the figures skill)
- No em/en dashes in copy; no source-credit or photo-credit lines
- EN and AR are separate renders from the same data model,
  never a translated overlay
- Read every page before delivery
