# Spreadsheet template — xls report template

Template file: `file_example_XLS_5000.xls` (5,000 rows). This is the
approved input shape for xls reports and dashboards: raw row data
in, pivot tables and pivot charts out.

## Columns

| Column | Type | Notes |
|---|---|---|
| First Name | text | person record |
| Last Name | text | person record |
| Gender | category | Female / Male |
| Country | category | United States / Great Britain / France |
| Age | number | years; bracketed 20s / 30s / 40s / 50s |
| Date | date | DD/MM/YYYY |

## Dashboard built from it

`~/workspace/mcit-ai-library/demo-people-dashboard.xlsx` — the
reference build. Genuine GridCraft pivot tables and bound pivot
charts:

- By gender: Female 3,800 (76.00%), Male 1,200 (24.00%)
- By country: United States 2,400 (48.00%), Great Britain 1,400
  (28%), France 1,200 (24%)
- By age bracket: 20s 2,300 · 30s 1,900 · 40s 500 · 50s 300
- Total: 5,000 — reconciles across all pivots

## Rules

- Pivots are built by GridCraft, never Python-computed static tables
- Front Dashboard sheet: KPI formulas referencing the pivots
  (values, never typed constants); verified: 5,000 · 76.00% · 48.00%
- One pivot sheet per analytical question, each with its bound chart
- No stale sheets from earlier iterations; clean sheet names
- Open every sheet before delivery
