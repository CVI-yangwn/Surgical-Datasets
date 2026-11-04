"""Minimal Markdown to HTML for DeepPaperNote reports. No third-party packages."""
from __future__ import annotations

import html
import re
from typing import Callable

MATH_RE = re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$", re.S)


def inline(text: str) -> str:
    stash: list[tuple[str, str]] = []

    def keep(kind: str):
        def _f(m: re.Match) -> str:
            stash.append((kind, m.group(1) if kind == "code" else m.group(0)))
            return f"\x00{len(stash) - 1}\x00"
        return _f

    text = MATH_RE.sub(keep("math"), text)
    text = re.sub(r"`([^`]+)`", keep("code"), text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", text)
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        text,
    )

    def restore(m: re.Match) -> str:
        kind, raw = stash[int(m.group(1))]
        if kind == "code":
            return f"<code>{html.escape(raw, quote=False)}</code>"
        return html.escape(raw, quote=False)

    return re.sub(r"\x00(\d+)\x00", restore, text)


def _list(lines: list[str]) -> str:
    items: list[tuple[int, str, str]] = []
    for ln in lines:
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
        if m:
            items.append((len(m.group(1)), "ol" if m.group(2)[0].isdigit() else "ul", m.group(3)))
    out: list[str] = []
    stack: list[tuple[int, str]] = []
    for indent, tag, body in items:
        while stack and indent < stack[-1][0]:
            out.append(f"</li></{stack.pop()[1]}>")
        if not stack or indent > stack[-1][0]:
            out.append(f"<{tag}>")
            stack.append((indent, tag))
        else:
            out.append("</li>")
        out.append(f"<li>{inline(body)}")
    while stack:
        out.append(f"</li></{stack.pop()[1]}>")
    return "".join(out)


def _table(lines: list[str]) -> str:
    def cells(row: str) -> list[str]:
        return [c.strip() for c in row.strip().strip("|").split("|")]

    head = cells(lines[0])
    rows = [cells(r) for r in lines[2:]]
    th = "".join(f"<th>{inline(c)}</th>" for c in head)
    trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def render(md: str, resolve_img: Callable[[str], str] = lambda s: s) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    para: list[str] = []

    def flush() -> None:
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith("```"):
            flush(); j = i + 1; buf = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j]); j += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(buf))}</code></pre>")
            i = j + 1; continue
        if s == "$$":
            flush(); j = i + 1; buf = []
            while j < len(lines) and lines[j].strip() != "$$":
                buf.append(lines[j]); j += 1
            out.append(f'<div class="math">{html.escape("$$" + chr(10).join(buf) + "$$", quote=False)}</div>')
            i = j + 1; continue
        m = re.match(r"^(#{3,6})\s+(.*)$", s)
        if m:
            flush(); lvl = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", s)
        if m:
            flush(); cap = ""
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if len(nxt) > 2 and nxt.startswith("*") and nxt.endswith("*") and not nxt.startswith("**"):
                cap = nxt[1:-1]; i += 1
            alt = html.escape(m.group(1), quote=True)
            out.append(
                f'<figure class="fig"><img src="{resolve_img(m.group(2))}" alt="{alt}" '
                f'loading="lazy" onclick="openLightbox(this)"><figcaption>{inline(cap or m.group(1))}</figcaption></figure>'
            )
            i += 1; continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            flush(); j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                j += 1
            out.append(_table(lines[i:j])); i = j; continue
        if s.startswith(">"):
            flush(); j = i; buf = []
            while j < len(lines) and lines[j].strip().startswith(">"):
                buf.append(lines[j].strip().lstrip(">").strip()); j += 1
            if buf and buf[0].startswith("[!figure]"):
                body = "<br>".join(inline(b) for b in buf[1:])
                out.append(f'<div class="ph"><b>{inline(buf[0][9:].strip())}</b><br>{body}</div>')
            else:
                out.append(f"<blockquote>{inline(' '.join(buf))}</blockquote>")
            i = j; continue
        if re.match(r"^(\s*)([-*]|\d+\.)\s+", ln):
            flush(); j = i
            while j < len(lines) and (re.match(r"^(\s*)([-*]|\d+\.)\s+", lines[j]) or (lines[j].startswith("  ") and lines[j].strip())):
                j += 1
            out.append(_list(lines[i:j])); i = j; continue
        para.append(s); i += 1
    flush()
    return "\n".join(out)
