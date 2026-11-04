# HTML Reading Report (图文解读网页)

Required on every run. The report is written in round 2 (SKILL.md step 19) and rendered in step 20 as one self-contained HTML file next to the saved note. The Markdown note stays the primary artifact; round 2 revises it through Final Note Lint and Formal Save, never by direct edits after save.

Two inputs, both written by the model in the output directory:

- `reading_report.md`: narrative sections plus reserved blocks (format below)
- `scorecard.json`: self-review rounds (format below)

Then run:

```bash
python3 scripts/lint_report.py --report reading_report.md --source-text <p>_full_text.md --output report_lint.json
python3 scripts/render_html.py --strict --report reading_report.md --scorecard scorecard.json --lint report_lint.json --insight insight_pass.json --note <final note>.md --output <final note>.html
```

`render_html.py` reads metadata from the note's YAML block and first core-information lines. Images referenced as `images/...` are inlined as base64 so the file works when moved.

## reading_report.md format

```markdown
---
title: <paper title>
subtitle: <plain-language title in the output language>
authors: <authors and institutions, one line>
venue: <arXiv id and status>
type: <paper type chip>
tags: [tag1, tag2, tag3]
source_url: https://arxiv.org/abs/...
one_sentence: <the whole paper in one sentence>
---

## 1. <section title>
Narrative paragraphs. Standard Markdown: **bold**, lists, tables, `code`, $math$, $$math$$.

![Figure 2](images/page_002_fig_figure_2.png)
*论文原图编号：Figure 2。<caption>*

:::highlights
- <claim worth remembering>
:::

:::data
- <number worth remembering>
:::

## @takeaways
- <what the reader should remember>

## @strengths
- <strength>

## @weaknesses
- <weakness>

## @questions
- <open question>
```

Rules:

- Number the regular sections. Reserved sections start with `@`.
- Every figure line keeps the italic caption line directly below it.
- Every number in the prose must appear in the source text. `lint_report.py` checks this and lists the numbers it cannot find.
- Follow `references/narrative-style.md` for voice. Follow the zh-CN style gate for wording.

## scorecard.json

Written only by `scripts/record_round.py`, never by hand. Each round holds its stage, the note's and the report's SHA-256, snapshot paths under `review_rounds/`, whether the report changed since the previous round, the hard gates, the dimension scores, the computed overall, a verdict, and the fixes planned after that round. See `references/report-scorecard.md` for the order of operations.

The page labels the score as a model self-review. Objective checks (number grounding, structure, insight-pass gaps) appear above it.

Render with:

```bash
python3 scripts/render_html.py --strict --report reading_report.md --scorecard scorecard.json \
  --lint report_lint.json --insight insight_pass.json --note <final note>.md --output <final note>.html
```
