#!/usr/bin/env python3
"""Build docs/index.html: papers grouped by surgical domain in collapsible sections.

Run from the repository root. Reads each reading_report.md front matter and
scorecard.json under DeepPaperNote_output/手术数据集/, and the CATALOG below,
which mirrors the dataset tables in README.md.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "DeepPaperNote_output" / "手术数据集"
GH = '<svg viewBox="0 0 16 16" width="14" height="14" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>'

# Mirrors README.md. "note" is the directory prefix under 手术数据集/, or None.
CATALOG = [
    ("ophthalmic", "👁️ 眼科", "Ophthalmic", [
        dict(name="Cataract-1K", year=2023, paper="https://arxiv.org/abs/2312.06295", data="https://github.com/Negin-Ghamsarian/Cataract-1K",
             task="阶段识别 / 分割 / 异常检测", size="1000 个视频", source="医院", slug="cataract-1k", note="Cataract_1K"),
        dict(name="OphNet", year=2024, paper="https://arxiv.org/abs/2406.07471", data="https://minghu0830.github.io/OphNet-benchmark",
             task="阶段、器械、操作识别", size="2278 个视频", source="YouTube", slug="ophnet", note="OphNet"),
    ]),
    ("endoscopic", "🔬 内镜", "Endoscopic", [
        dict(name="EndoBench", year=2025, paper="https://arxiv.org/abs/2505.23601", data="https://huggingface.co/datasets/Saint-lsy/EndoBench",
             task="视觉问答", size="", source="", slug="endobench", note="EndoBench"),
    ]),
    ("laparoscopic", "🩻 腹腔镜", "Laparoscopic", [
        dict(name="SLAM", year=2025, paper="", data="https://figshare.com/articles/dataset/SLAM_-_Surgical_LAparoscopic_Motions/28104782/3",
             task="分类", size="~3650 个视频", source="", slug=None, note=None),
    ]),
    ("notyet", "🕒 尚未公开", "Not yet", [
        dict(name="OphCLIP", year=2025, paper="https://arxiv.org/abs/2411.15421", data="",
             task="图文对齐", size="375K 图文对", source="YouTube", slug="ophclip", note="OphCLIP", tag="眼科"),
    ]),
]


def front_matter(path: Path) -> dict:
    meta = {}
    for line in path.read_text(encoding="utf-8").split("---")[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta


def reading(prefix: str) -> dict:
    d = next(p for p in NOTES.iterdir() if p.is_dir() and p.name.startswith(prefix))
    meta = front_matter(d / "reading_report.md")
    meta["score"] = json.loads((d / "scorecard.json").read_text(encoding="utf-8"))["rounds"][-1]["overall"]
    return meta


def esc(s) -> str:
    return html.escape(str(s))


def card(item: dict) -> str:
    links = []
    if item["paper"]:
        links.append(f'<a href="{esc(item["paper"])}" target="_blank" rel="noopener">论文</a>')
    if item["data"]:
        label = f"{GH} 数据" if "github" in item["data"] else "数据"
        links.append(f'<a href="{esc(item["data"])}" target="_blank" rel="noopener">{label}</a>')
    facts = " · ".join(esc(x) for x in (item["year"], item["task"], item["size"], item["source"]) if x)
    extra = f'<span class="chip ghost">{esc(item["tag"])}</span>' if item.get("tag") else ""
    if not item["note"]:
        return (f'<div class="card pending"><div class="top"><span class="name">{esc(item["name"])}</span>{extra}'
                f'<span class="state">精读待补</span></div><p class="facts">{facts}</p>'
                f'<p class="one">论文链接待补，暂未精读。</p><div class="links">{"".join(links)}</div></div>')
    r = reading(item["note"])
    tags = "".join(f'<span class="tag">{esc(t.strip())}</span>' for t in r["tags"].strip("[]").split(",") if t.strip())
    return (f'<div class="card"><div class="top"><span class="name">{esc(item["name"])}</span>{extra}'
            f'<span class="score">{r["score"]}<small> / 10 自评</small></span></div>'
            f'<p class="facts">{facts}</p><p class="sub">{esc(r["subtitle"])}</p><p class="one">{esc(r["one_sentence"])}</p>'
            f'<div class="tags">{tags}</div><div class="links"><a class="go" href="papers/{item["slug"]}.html">阅读精读 →</a>'
            f'{"".join(links)}</div></div>')


def section(key: str, title: str, en: str, items: list) -> str:
    done = sum(1 for i in items if i["note"])
    cards = "".join(card(i) for i in items)
    return (f'<details class="group" id="{key}" open><summary><span class="t">{title}</span><span class="en">{en}</span>'
            f'<span class="cnt">{len(items)} 个数据集 · {done} 篇精读</span><span class="arr"></span></summary>'
            f'<div class="grid">{cards}</div></details>')


CSS = """
:root{--bg:#f6f7fb;--card:#fff;--bd:#e4e6f0;--tx:#1b1d2b;--tx2:#4b4f66;--mut:#7c8099;--ac:#4f5bd5;--ac2:#b84fa3;--sum:#fff}
@media(prefers-color-scheme:dark){:root{--bg:#12131c;--card:#1b1d2b;--bd:#2a2d42;--tx:#eef0fb;--tx2:#c3c6dc;--mut:#8a8ea8;--ac:#8b93ff;--ac2:#f07ad0;--sum:#171927}}
*{box-sizing:border-box}body{margin:0;font:16px/1.65 -apple-system,"PingFang SC","Microsoft YaHei",system-ui,sans-serif;background:var(--bg);color:var(--tx)}
header{padding:52px 20px 28px;text-align:center;background:linear-gradient(135deg,#4f5bd5,#8b5cf6 55%,#b84fa3);color:#fff}
header h1{margin:0 0 8px;font-size:2.05em}header p{margin:4px auto;max-width:720px;opacity:.92}header a{color:#fff}
.stats{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:16px}.stats span{background:rgba(255,255,255,.16);border-radius:999px;padding:3px 14px;font-size:.88em}
.wrap{max-width:1080px;margin:0 auto;padding:24px 18px 60px}
.tools{display:flex;justify-content:flex-end;gap:8px;margin-bottom:12px}.tools button{background:var(--card);color:var(--tx2);border:1px solid var(--bd);border-radius:8px;padding:4px 12px;font:inherit;font-size:.85em;cursor:pointer}
.tools button:hover{border-color:var(--ac);color:var(--ac)}
.group{background:var(--sum);border:1px solid var(--bd);border-radius:16px;margin-bottom:16px;overflow:hidden}
summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:10px;padding:16px 22px;user-select:none}
summary::-webkit-details-marker{display:none}summary:hover{background:rgba(79,91,213,.06)}
summary .t{font-size:1.18em;font-weight:700}summary .en{color:var(--mut);font-size:.9em}summary .cnt{margin-left:auto;color:var(--mut);font-size:.85em}
summary .arr{width:10px;height:10px;border-right:2px solid var(--mut);border-bottom:2px solid var(--mut);transform:rotate(-45deg);transition:.2s;align-self:center}
details[open] summary .arr{transform:rotate(45deg)}details[open] summary{border-bottom:1px solid var(--bd)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:16px;padding:18px 20px 20px}
.card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:18px 20px;transition:.18s}
.card:hover{box-shadow:0 10px 26px rgba(79,91,213,.14);border-color:var(--ac)}.card.pending{opacity:.75;border-style:dashed}
.top{display:flex;gap:8px;align-items:center}.name{font-weight:700;font-size:1.08em}
.chip{border-radius:999px;padding:0 9px;font-size:.75em}.chip.ghost{color:var(--ac);border:1px solid var(--ac)}
.score{margin-left:auto;font-weight:700;color:var(--ac2)}.score small{font-weight:400;color:var(--mut)}.state{margin-left:auto;color:var(--mut);font-size:.85em}
.facts{color:var(--mut);font-size:.84em;margin:4px 0 8px}.sub{color:var(--ac);margin:0 0 8px;font-size:.94em}.one{color:var(--tx2);font-size:.9em;margin:0 0 12px;flex:1}
.tags{margin-bottom:12px}.tag{display:inline-block;font-size:.74em;color:var(--mut);border:1px solid var(--bd);border-radius:6px;padding:0 6px;margin:2px 4px 2px 0}
.links{display:flex;gap:14px;align-items:center;flex-wrap:wrap;font-size:.88em}.links a{color:var(--tx2);text-decoration:none;display:inline-flex;gap:4px;align-items:center}
.links a:hover{color:var(--ac)}.links a.go{background:var(--ac);color:#fff;border-radius:8px;padding:4px 12px;font-weight:600}.links a.go:hover{opacity:.9;color:#fff}
.note{margin-top:28px;color:var(--mut);font-size:.86em;text-align:center}
"""

JS = """document.getElementById('ex').onclick=function(){document.querySelectorAll('details.group').forEach(function(d){d.open=true})};
document.getElementById('co').onclick=function(){document.querySelectorAll('details.group').forEach(function(d){d.open=false})};"""


def main() -> None:
    total = sum(len(i) for *_, i in CATALOG)
    done = sum(1 for *_, items in CATALOG for i in items if i["note"])
    body = "".join(section(*g) for g in CATALOG)
    page = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Surgical-Datasets · 论文精读</title><style>{CSS}</style></head><body>
<header><h1>🩺 Surgical-Datasets · 论文精读</h1>
<p>手术视频与内镜数据集论文的中文图文解读：背景与动机、核心观点、数据与实验、深入分析，以及论文没有说明的地方。</p>
<div class="stats"><span>{len(CATALOG)} 个类别</span><span>{total} 个数据集</span><span>{done} 篇精读</span></div>
<p style="margin-top:14px"><a href="https://github.com/CVI-yangwn/Surgical-Datasets">GitHub 仓库</a></p></header>
<div class="wrap"><div class="tools"><button id="ex" type="button">全部展开</button><button id="co" type="button">全部收起</button></div>{body}
<p class="note">每篇由 DeepPaperNote 两轮流程生成：第 1 轮为原版精读，第 2 轮为多轮追问与叙事修改。分数是模型自评，不是外部评审；数字经脚本与原文逐一核对。</p></div>
<script>{JS}</script></body></html>"""
    (ROOT / "docs" / "index.html").write_text(page, encoding="utf-8")
    print(f"docs/index.html: {len(CATALOG)} groups, {total} datasets, {done} readings")


if __name__ == "__main__":
    main()
