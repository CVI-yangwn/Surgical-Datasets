# Report Scorecard (自评打分)

Used by the two required reading rounds (SKILL.md steps 18 to 20). Round 1 scores the note alone; round 2 scores the note and the report together. The reviewer is the same model that wrote them, so the score is a self-review. Treat it as a checklist result, not an independent grade.

This file adapts `evals/note-quality-rubric.md` from the upstream repository. It adds D9 for narrative clarity.

## Hard gates

Each gate is `pass`, `fail`, or `unknown`. Any `fail` caps the overall score at 6.0.

| Gate | Check |
|---|---|
| H1 | The title, authors, and arXiv id match the source manifest |
| H2 | No sentence contradicts the paper's text, tables, or figures |
| H3 | Every number in the report appears in the source text (`lint_report.py` shows no unmatched number, or each unmatched one is explained) |
| H4 | Unproven claims are not written as the paper's conclusions; claims beyond the evidence are marked |

## Dimensions

Score each from 0 to 10. Write the evidence for any score below 8 in `verdict`.

| Id | Dimension | A score of 8 or higher needs |
|---|---|---|
| D1 | Evidence chain | Problem, method, protocol, result, and limit each have a section and tie to a table or figure |
| D2 | Mechanism depth | A reader can state the input, operation, and output of each core step |
| D3 | Numbers and settings | Main results, baselines, and key settings are present, with units and benchmark names |
| D4 | Claim boundaries | At least three things the results do not show are named, each with a reason |
| D5 | Positioning | The report names the alternatives and says what is new against each |
| D6 | Reuse | Takeaways say what to copy, what to check, and what to avoid |
| D7 | Navigation | Sections are numbered, figures sit beside the text they support, highlights and data strips match the prose |
| D8 | Language | No half-translated phrases; terms defined at first use |
| D9 | Narrative | Each section opens with its tension, numbers are followed by a "so what", sections end with a bridge |

## Overall score

Weights: D1 15%, D2 15%, D3 15%, D4 15%, D5 10%, D6 10%, D7 5%, D8 5%, D9 10%. Round to one decimal. Apply the hard-gate cap after the weighted sum.

## Rounds

Two rounds, each recorded with `scripts/record_round.py`. The script snapshots the note (and the report in round 2) into `review_rounds/`, stores their SHA-256, computes the weighted score, and refuses rounds out of order. Never write `scorecard.json` by hand.

**Round 1, `--stage baseline`.** The note exactly as the original DeepPaperNote flow saved it (step 17), scored **before any edit**. No report yet. List as `fixes` what the user's method will change: missing 核心观点速览, sections that open without their question, numbers without a "so what", claims beyond the evidence, gaps not named. The script requires a non-empty list.

**Round 2, `--stage narrative_review`.** The iteration lives here, in the Insight Pass (`references/insight-pass.md`): knowledge points, detail questions, then a challenge round, followed by the narrative revision. When that work is done, score the final note and report from scratch and fix what the scoring finds. Then rerun the lints and Formal Save, and record. `--fixes` must be empty; limits that cannot be fixed go in the verdict. There is no third round: the Insight Pass is the multi-round thinking.

If a score drops between the rounds, write the reason in the verdict.

`render_html.py --strict` refuses to render unless the rounds are baseline then narrative_review and round 2's hashes match the final note and report. The page shows the objective checks (number grounding, structure, insight-pass gaps) above the self-score.
