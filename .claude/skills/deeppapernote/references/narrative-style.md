# Narrative Style (图文解读写法)

Required in round 2 (SKILL.md step 19) for revising the Markdown note and writing the HTML reading report (`references/html-report.md`), and as the scoring standard for D9. Round 1 does not use it, so the original flow stays the baseline. It changes how the prose reads. It never relaxes grounding, lint gates, or claim boundaries.

Distilled from a reference reading page that explains a paper in plain language, then checked against this skill's own failure modes.

## What the reference does well

1. **Sections follow the paper's logic, not a fixed template.** The reader sees "真/仿两难" before any method name. Each section answers one question the reader would ask next.
2. **Each section opens with the tension.** One or two sentences say what is hard or unknown, then the paper's answer arrives.
3. **Analogy before mechanism.** A reward formula is explained as "会用工具的奖励加倍", then the symbols are listed one by one.
4. **Every number gets a "so what".** "27B 从 67.1 涨到 79.9" is followed by what that shows and what it does not.
5. **Bold carries the argument.** A reader who only reads the bold sentences should recover the storyline.
6. **Sections end with a bridge.** The last sentence says why the next section exists.
7. **Terms are defined at first use**, in one clause, in the reader's words.
8. **Short strips summarize each section**: 亮点 (claims worth remembering) and 数据 (numbers worth remembering).
9. **A short takeaways block, then an independent critique** (优点 / 不足 / 开放问题), then the review history.

## What the reference gets wrong (do not copy)

- It hedges a number the paper states plainly ("据原文推断…以原文为准") when the value is in the hyperparameter table. Read the table and state the number.
- It writes "逼近 GPT-5.6 级别" without a row in the results table to back it. Every comparison needs a table cell.
- It says "接近闭源前沿" while the paper's MobileWorld result is well below the closed model. Name the benchmarks where the claim fails.
- Its self-score moves 8.3 → 8.6 → 8.3 with no stated reason. Scores here must come from checked criteria.

## Rules

- One idea per paragraph. Open with the point, then the evidence.
- Plain words. If a sentence needs the paper's jargon, define the jargon in the same sentence.
- Use `**bold**` for the sentence a skimmer must not miss. At most one or two per paragraph.
- Use a question as a section opener only when the reader would really ask it. Do not stack rhetorical questions.
- Analogies must be accurate. Drop an analogy that needs a caveat.
- Say "论文未报告" when the paper is silent, and say what that limits. Never fill the gap.
- Separate three voices: what the paper shows, what the authors claim, what you infer. Mark inference with 我的判断 or 推断.
- Keep the zh-CN style gate in mind: no half-translated phrases, no Latin words unless they are stable proper nouns, benchmark names, or code identifiers.

## Discourse order (篇章顺序)

Both the Markdown note and the HTML report follow one order. The note keeps its fixed section names; the order below shows where each part goes inside them.

1. **背景与动机.** What is hard, who is stuck, why now. Two to four short paragraphs. In the note this opens `研究问题`.
2. **核心观点速览.** Right after the background, state the paper's answer in plain words: the idea, the three or four moves that carry it, and the headline result with its boundary. Keep it to one screen. In the note this closes `研究问题` as `### 核心观点速览`; do not move it ahead of `研究问题`, the lint order stays.
3. **具体观点.** One section per move: the design, the data, the protocol. Each opens with the question it answers.
4. **实验.** Main result first, then the ablations that explain it, then the controls that rule out cheating or chance.
5. **深入分析.** Why it works, what it costs, where it breaks, and what the evidence cannot show. This is argument, not repeated numbers.
6. **边界与复现.** What to check before trusting or reusing it.

A reader who stops after step 2 must still hold the right picture. A reader who reads all of it must find nothing in step 5 that step 3 or 4 did not set up.

## Concision (凝练)

- Cut any sentence that repeats the one before it in different words.
- A paragraph carries one idea and fits on a phone screen. `lint_report.py` warns above 220 Chinese characters.
- Prefer a short list or a small table over a paragraph that enumerates parallel items.
- Say a number once in the place where it matters, then refer to it by name.
- Drop transitions that only announce ("下面我们来看…"). Keep bridges that carry a reason.
- Define a term once, at first use. Do not re-explain it.

## Multi-round thinking (多轮思考)

Do the thinking in the round-2 Insight Pass, before revising, and keep it as a compact artifact. See `references/insight-pass.md`. The pass has three rounds: knowledge points the reader needs, detail questions answered from the source, and a challenge round that tests each central claim. Anything the source cannot answer is written as 论文未说明, with what that limits.

## Section skeleton for the HTML report

Choose 8 to 12 sections that follow this paper, in the discourse order above. A typical set for a method paper:

1. 背景与动机
2. 核心观点速览
3. one section per major component or move
4. 训练或验证协议
5. 结果说了什么
6. 为什么有效 (深入分析)
7. 结果没说什么
8. 怎么确认不是作弊或巧合
9. 复现要注意什么

Drop sections the paper does not support. Add a section when the paper has a distinctive piece (a reward formula, a data pipeline).
