# Insight Pass (多轮思考)

The required first part of round 2 (SKILL.md step 19). It runs on the note saved in round 1, before the narrative revision. It replaces a long free-form thinking block with a short JSON file, so every conclusion is traceable and every gap is named.

Write `insight_pass.json` next to the other run artifacts. Check it with:

```bash
python3 scripts/lint_insight.py --insight insight_pass.json --source-manifest <p>_source_manifest.json
```

The pass does not change the note schema or any existing lint. Every `revisions` item and every `not_stated` gap must appear in the revised note and in the report. Each answer is checked against the source, not against the round-1 note.

## Three passes (inside round 2)

**Pass 1: knowledge points.** List what a reader needs to know before the paper makes sense: terms, metrics, algorithms, evaluation settings. For each: `term`, a one-sentence `plain` explanation, `where` it first matters (a section id), and `needed_for` (which later claim breaks without it). Skip what the target reader already knows. Aim for 6 to 12.

**Pass 2: detail questions.** Ask the questions a careful reader would ask about each design choice, number, and setting: why this value, why this baseline, what changed between two rows, what the paper does not say. Answer each one from the source. Each answer carries `evidence` (section ids or pages) and a `status`: `resolved`, `partly`, or `not_stated`. A `not_stated` answer is written as 论文未说明 in the note, with what that limits. Never fill the gap. Aim for 8 to 15.

**Pass 3: challenge.** For each central claim, write the strongest alternative explanation, the evidence that would separate it from the paper's reading, and whether the paper contains that evidence. Record `verdict`: `supported`, `partly_supported`, or `not_separated`. Then list `revisions`: concrete edits to the draft or plan that the three passes produced.

## File shape

```json
{
  "knowledge_points": [
    {"term": "", "plain": "", "where": "sec:...", "needed_for": ""}
  ],
  "detail_questions": [
    {"question": "", "answer": "", "evidence": ["sec:..."], "status": "resolved"}
  ],
  "challenges": [
    {"claim": "", "alternative": "", "separating_evidence": "", "in_paper": false, "verdict": "not_separated"}
  ],
  "revisions": ["<edit made because of the pass>"]
}
```

## Rules

- Every `evidence` id must exist in the source manifest. A `resolved` answer with no evidence fails lint.
- Do not copy the paper's own framing into `alternative`. Write what a skeptical reader would propose.
- A pass that produces no `revisions` was probably too shallow. Look again at row-to-row differences in the main tables.
- Keep the file under about 6 KB. It is a working artifact, not a second note.
