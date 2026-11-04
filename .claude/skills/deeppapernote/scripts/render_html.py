#!/usr/bin/env python3
"""Render reading_report.md (+ scorecard.json) into one self-contained HTML page."""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import html
import json
import mimetypes
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from html_theme import CSS  # noqa: E402
from lint_report import split_front_matter  # noqa: E402
from md_mini import inline, render  # noqa: E402
from record_round import overall  # noqa: E402

JS = r"""
function openLightbox(el){var b=document.getElementById('lb');b.querySelector('img').src=el.src;b.style.display='flex'}
document.getElementById('lb').onclick=function(){this.style.display='none'};
(function(){var s=localStorage.getItem('dpn-theme')||'light';document.documentElement.setAttribute('data-theme',s);
var btn=document.getElementById('tg');function lab(){btn.textContent=document.documentElement.getAttribute('data-theme')=='dark'?'日间':'夜间'}
lab();btn.onclick=function(){var n=document.documentElement.getAttribute('data-theme')=='dark'?'light':'dark';
document.documentElement.setAttribute('data-theme',n);localStorage.setItem('dpn-theme',n);lab()};
var links=[].slice.call(document.querySelectorAll('.nav a[href^="#"]'));
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){
a.classList.toggle('on',a.getAttribute('href')=='#'+e.target.id)})}})},{rootMargin:'-40% 0px -55% 0px'});
document.querySelectorAll('section.blk').forEach(function(s){io.observe(s)})})();
function dpnMath(){if(window.renderMathInElement){renderMathInElement(document.body,{delimiters:[
{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false})}}
"""

KATEX = ""  # math is loaded after page load so an offline reader is never blocked

LOAD_MATH = r"""
window.addEventListener('load',function(){var B='https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/';
var c=document.createElement('link');c.rel='stylesheet';c.href=B+'katex.min.css';document.head.appendChild(c);
var s=document.createElement('script');s.src=B+'katex.min.js';s.onload=function(){var a=document.createElement('script');
a.src=B+'contrib/auto-render.min.js';a.onload=dpnMath;document.head.appendChild(a)};document.head.appendChild(s)});
"""


def parse_list(tags: str) -> list[str]:
    return [t.strip() for t in tags.strip().strip("[]").split(",") if t.strip()]


def make_resolver(base: Path):
    def resolve(src: str) -> str:
        if src.startswith(("http://", "https://", "data:")):
            return src
        p = (base / src).resolve()
        if not p.exists():
            return html.escape(src)
        mime = mimetypes.guess_type(p.name)[0] or "image/png"
        return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
    return resolve


def split_sections(body: str) -> list[tuple[str, str]]:
    parts = re.split(r"^##\s+(.+?)\s*$", body, flags=re.M)
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts) - 1, 2)]


def pull_blocks(text: str) -> tuple[str, dict[str, list[str]]]:
    found: dict[str, list[str]] = {}

    def grab(m: re.Match) -> str:
        found[m.group(1)] = [re.sub(r"^[-*]\s+", "", ln.strip()) for ln in m.group(2).splitlines() if ln.strip()]
        return ""

    return re.sub(r"^:::(highlights|data)\s*\n(.*?)\n:::\s*$", grab, text, flags=re.M | re.S), found


def bullets(text: str) -> list[str]:
    return [re.sub(r"^[-*]\s+", "", ln.strip()) for ln in text.splitlines() if ln.strip().startswith(("-", "*"))]


def strip_num(title: str) -> tuple[str, str]:
    m = re.match(r"^(\d+)[.、]?\s*(.*)$", title)
    return (m.group(1), m.group(2)) if m else ("", title)


def strip_html(items: list[str]) -> str:
    return "".join(f'<span class="i">{inline(x)}</span>' for x in items)


def section_card(title: str, text: str, resolve) -> str:
    num, name = strip_num(title)
    body, blocks = pull_blocks(text)
    badge = f'<span class="num">{html.escape(num)}</span>' if num else ""
    out = [f'<div class="card" id="s{num or html.escape(name)}"><h3>{badge}{inline(name)}</h3>', render(body, resolve)]
    if blocks.get("highlights"):
        out.append(f'<div class="strip h"><span class="t">亮点</span>{strip_html(blocks["highlights"])}</div>')
    if blocks.get("data"):
        out.append(f'<div class="strip d"><span class="t">数据</span>{strip_html(blocks["data"])}</div>')
    out.append("</div>")
    return "".join(out)


def box(cls: str, title: str, items: list[str]) -> str:
    lis = "".join(f"<li>{inline(x)}</li>" for x in items)
    return f'<div class="box {cls}"><h4>{title}</h4><ul>{lis}</ul></div>'


STAGE_LABEL = {"baseline": "原流程笔记", "narrative_review": "叙事与多轮思考后"}


def card_problems(card: dict, report: Path, note: Path | None) -> list[str]:
    """Why the scorecard does not describe the final files, if it does not."""
    rounds = card.get("rounds", [])
    if not rounds:
        return ["没有自查记录"]
    out = []
    stages = [r.get("stage") for r in rounds]
    if stages != ["baseline", "narrative_review"]:
        out.append("轮次顺序不完整")
    last = rounds[-1]
    if last.get("report_sha256") != hashlib.sha256(report.read_bytes()).hexdigest():
        out.append("评分对应的是旧版文稿")
    if note and last.get("note_sha256") != hashlib.sha256(note.read_bytes()).hexdigest():
        out.append("评分对应的是旧版笔记")
    if last.get("dimensions") and abs(overall(last["dimensions"], last["hard_gates"]) - float(last.get("overall", 0))) > 0.05:
        out.append("分数与各维度不一致")
    return out


def history_html(card: dict) -> str:
    rounds = card.get("rounds", [])
    out = []
    for r in rounds:
        gates = " ".join(f"{k}:{v}" for k, v in r.get("hard_gates", {}).items())
        dims = "".join(f"<span>{k} <b>{v}</b></span>" for k, v in r.get("dimensions", {}).items())
        fixes = "".join(f"<li>{inline(f)}</li>" for f in r.get("fixes", []))
        out.append(
            f'<div class="round"><div class="h"><span>第 {r.get("round")} 轮 · {STAGE_LABEL.get(r.get("stage", ""), "复查")} · 笔记 {html.escape(str(r.get("note_sha256", ""))[:8])}'
            + (f' · 文稿 {html.escape(str(r.get("report_sha256", ""))[:8])}' if r.get("report_sha256") else "")
            + f'</span><span class="s">{r.get("overall")} 分</span></div>'
            f'<p>{inline(r.get("verdict", ""))}</p><div class="dims">{dims}</div>'
            f'<div class="gates">硬性检查 {html.escape(gates)}</div>'
            + (f'<ul style="margin:8px 0 0 1.2em;font-size:.86em;color:var(--tx2)">{fixes}</ul>' if fixes else "")
            + "</div>"
        )
    return "".join(out)


def checks_html(lint: dict, insight: dict) -> str:
    chips = []
    if lint:
        un = len(lint.get("unmatched_numbers", []))
        chips.append(f'数字核对 {"全部在原文中找到" if not un else str(un) + " 项未匹配"}')
        chips.append(f'结构检查 {"通过" if lint.get("passes_structure") else "未通过"}')
    if insight:
        qs = insight.get("detail_questions", [])
        gaps = sum(1 for q in qs if q.get("status") == "not_stated")
        chips.append(f'细节追问 {len(qs)} 条，其中 {gaps} 条论文未说明')
        chips.append(f'反向检验 {len(insight.get("challenges", []))} 条')
    return "".join(f'<span class="tag">{html.escape(c)}</span>' for c in chips)


def build(report: Path, scorecard: Path | None, note: Path | None, lint: dict | None = None, insight: dict | None = None) -> str:
    meta, body = split_front_matter(report.read_text(encoding="utf-8"))
    resolve = make_resolver(report.parent)
    regular, reserved = [], {}
    for title, text in split_sections(body):
        if title.startswith("@"):
            reserved[title[1:]] = bullets(text)
        else:
            regular.append((title, text))
    card = json.loads(scorecard.read_text(encoding="utf-8")) if scorecard and scorecard.exists() else {}
    last = (card.get("rounds") or [{}])[-1]
    problems = card_problems(card, report, note) if card.get("rounds") else []
    warn = f'（{"；".join(problems)}）' if problems else ""
    if problems:
        print("warning: scorecard does not match the final files: " + "; ".join(problems), file=sys.stderr)
    score = (
        f'<div class="score"><span class="v">{last.get("overall")}</span>'
        f'<span class="l">/ 10 · 模型自评 · {len(card["rounds"])} 轮{warn}</span></div>' if card.get("rounds") else ""
    )
    checks = checks_html(lint or {}, insight or {})
    tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in parse_list(meta.get("tags", "")))
    src = meta.get("source_url", "")
    note_link = f'<a class="src" href="{html.escape(note.name)}">精读笔记（Markdown）</a>' if note else ""
    nav = ['<a href="#overview">概览</a>', '<a href="#content">正文</a>', '<a href="#takeaways">核心收获</a>',
           '<a href="#analysis">批判分析</a>'] + (['<a href="#history">自查记录</a>'] if card.get("rounds") else [])
    cards = "".join(section_card(t, x, resolve) for t, x in regular)
    take = "".join(f"<div>{inline(x)}</div>" for x in reserved.get("takeaways", []))
    page = f"""<!DOCTYPE html><html lang="zh-CN" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(meta.get("title", ""))}</title>
<style>{CSS}</style>{KATEX}</head><body>
<nav class="nav"><b>图文解读</b>{"".join(nav)}<span class="sp"></span><button id="tg" type="button"></button></nav>
<div class="wrap">
<section class="blk hero" id="overview"><h1>{inline(meta.get("subtitle") or meta.get("title", ""))}</h1>
<div class="sub">{inline(meta.get("title", ""))}</div>
<div class="meta">{inline(meta.get("authors", ""))} | {html.escape(meta.get("venue", ""))}</div>
<div><span class="chip">{html.escape(meta.get("type", ""))}</span>{tags}</div>
<div class="one">{inline(meta.get("one_sentence", ""))}</div>
<div>{checks}</div>
<div>{score}<a class="src" href="{html.escape(src)}" target="_blank" rel="noopener">查看原文</a>{note_link}</div></section>
<section class="blk" id="content"><h2 class="sec">图文解读</h2><div class="desc">{len(regular)} 个主题板块，按论文的论证顺序展开</div>{cards}</section>
<section class="blk" id="takeaways"><h2 class="sec">核心收获</h2><div class="desc">读完应该记住的几点</div><div class="take">{take}</div></section>
<section class="blk" id="analysis"><h2 class="sec">批判分析</h2><div class="desc">独立于作者叙述的评价</div><div class="grid3">
{box("ok", "优点", reserved.get("strengths", []))}{box("bad", "不足", reserved.get("weaknesses", []))}{box("q", "开放问题", reserved.get("questions", []))}</div></section>
{('<section class="blk" id="history"><h2 class="sec">自查记录</h2><div class="desc">第 1 轮评原流程生成的笔记，第 2 轮评多轮思考和叙事修改之后的笔记与文稿；第 1 轮在改动前记录，两轮都附当时笔记和文稿的哈希。分数是模型自评，不是外部评审</div>' + history_html(card) + '</section>') if card.get("rounds") else ""}
</div><footer>由 DeepPaperNote 生成 | {dt.date.today().isoformat()}</footer>
<div id="lb"><img alt=""></div><script>{JS}{LOAD_MATH}</script></body></html>"""
    return page


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report", required=True)
    ap.add_argument("--scorecard", default="")
    ap.add_argument("--note", default="")
    ap.add_argument("--lint", default="", help="report_lint.json from lint_report.py")
    ap.add_argument("--insight", default="", help="insight_pass.json")
    ap.add_argument("--output", required=True)
    ap.add_argument("--strict", action="store_true", help="refuse to render when the scorecard does not match")
    a = ap.parse_args()
    load = lambda s: json.loads(Path(s).read_text(encoding="utf-8")) if s and Path(s).exists() else None
    if a.strict and a.scorecard:
        probs = card_problems(json.loads(Path(a.scorecard).read_text(encoding="utf-8")), Path(a.report),
                              Path(a.note) if a.note else None)
        if probs:
            sys.exit("scorecard check failed: " + "; ".join(probs))
    out = build(Path(a.report), Path(a.scorecard) if a.scorecard else None, Path(a.note) if a.note else None,
                load(a.lint), load(a.insight))
    Path(a.output).write_text(out, encoding="utf-8")
    print(json.dumps({"status": "ok", "output": a.output, "bytes": len(out.encode())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
