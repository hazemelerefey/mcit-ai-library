# PDF report template — design notes (Midnight Noir, approved 2026-10-14)

Reference implementation: `~/workspace/wsis-deck/build_report_noir.py`
(dark + light). Sample outputs:
`~/workspace/your_files/MCIT-WSIS-Report-Noir-DARK-sample.pdf`,
`~/workspace/your_files/MCIT-WSIS-Report-Noir-LIGHT-sample.pdf`.
Supersedes the Platinum Silver v6 spec for all new reports.

## Tokens

Dark theme:
- Midnight `#010612` page bg, Abyss `#030F1F` panels,
  Royal `#1E507A` hairlines, Pulse `#16A6E9` data accent,
  Pale Gold `#F7EF8A` rare premium highlights only,
  White `#FFFFFF` text, Silver `#B9C2CE` secondary text.

Light theme:
- White `#FFFFFF` page bg, ink `#0A1628` headings,
  body ink `#1B2C45`, muted `#5A6B82` secondary,
  hairline `#E2E5EA`, Royal `#1E507A` eyebrows and rules,
  Pulse `#16A6E9` data accent (large elements; Royal for small text).

## Type

- EN headings: Nohemi Bold, tight tracking.
- EN body: Libre Franklin Regular, 1.5 line height.
- Eyebrows: Libre Franklin SemiBold, uppercase, letterspaced.
- AR headings: Noto Sans Arabic Condensed Black; AR body:
  Noto Sans Arabic Regular (never letterspace Arabic).
- Scale (A4): Title 42 / H1 28 / H2 20 / body 11 / caption 8.5.
- Accent rule: 3px bar, 48px wide, under every major title.

## Structure

Cover (noir artwork, same for both themes) → inside title + TOC
(theme surface, hairline rules) → chapter openers (theme surface,
eyebrow + H1 + accent rule) → content pages (theme surface, H1 +
accent rule, stat callouts, figures; running header; page numbers
bottom-outer) → back cover (noir artwork).

Margins 22mm. One idea per page spread.

## Rules

- Every report ships dark + light, like the decks.
- Every figure carries real data, generated per theme at 2x
  (dark figures on `#010612`, light on white).
- Figures never float without a caption stating what the reader
  should see.
- No em/en dashes in copy; no source-credit or photo-credit lines.
- EN and AR are separate renders from the same data model,
  never a translated overlay.
- One accent per page; gold never dominates charts or body text;
  gold ornament lives on covers only.
- Banned: gradients, glassmorphism, glowing elements, green-dot
  status indicators, dot-plus-label chips.
- Read every page before delivery.
