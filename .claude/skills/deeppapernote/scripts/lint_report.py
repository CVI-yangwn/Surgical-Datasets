#!/usr/bin/env python3
"""Lint a DeepPaperNote reading_report.md (or, with --mode note, the Markdown note):
structure, paragraph length, and numeric grounding against the paper text."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_META = ("title", "subtitle", "authors", "venue", "type", "tags", "source_url", "one_sentence")
RESERVED = ("takeaways", "strengths", "weaknesses", "questions")
NUM_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+\.\d+|\d{3,}|\d+(?=\s?%))(?![\w])")


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\n(.*?)\n---\n?", text, flags=re.S)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            v = v.strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            meta[k.strip()] = v
    return meta, text[m.end():]


def strip_non_prose(body: str) -> str:
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)
    body = re.sub(r"https?://\S+", " ", body)
    body = re.sub(r"^#{1,6}\s+[\d.]+\s", "", body, flags=re.M)
    return body


def normalize_numbers(source: str) -> set[str]:
    found = set()
    for tok in re.findall(r"\d[\d,]*\.?\d*", source):
        tok = tok.rstrip(".,")
        found.add(tok)
        found.add(tok.replace(",", ""))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report", required=True)
    ap.add_argument("--source-text", required=True, help="Full text Markdown of the paper")
    ap.add_argument("--min-sections", type=int, default=6)
    ap.add_argument("--max-para-chars", type=int, default=220)
    ap.add_argument("--mode", choices=("report", "note"), default="report",
                    help="note: skip report-only structure checks, keep number and paragraph checks")
    ap.add_argument("--number-exceptions", default="",
                    help='JSON file {"value": "reason"} for derived numbers (sums, differences)')
    ap.add_argument("--output", default="")
    args = ap.parse_args()

    report_path = Path(args.report)
    text = report_path.read_text(encoding="utf-8")
    source = Path(args.source_text).read_text(encoding="utf-8")
    meta, body = split_front_matter(text)

    issues: list[dict] = []
    exceptions = json.loads(Path(args.number_exceptions).read_text(encoding="utf-8")) if args.number_exceptions else {}
    if args.mode == "note":
        body = re.sub(r"^## (引用|References)\s*$.*", "", body, flags=re.M | re.S)
    for key in (REQUIRED_META if args.mode == "report" else ()):
        if not meta.get(key):
            issues.append({"code": "meta_missing", "field": key})

    headings = re.findall(r"^##\s+(.+?)\s*$", body, flags=re.M)
    regular = [h for h in headings if not h.startswith("@")]
    reserved = [h[1:] for h in headings if h.startswith("@")]
    if args.mode == "report" and len(regular) < args.min_sections:
        issues.append({"code": "too_few_sections", "count": len(regular), "min": args.min_sections})
    for name in (RESERVED if args.mode == "report" else ()):
        if name not in reserved:
            issues.append({"code": "reserved_section_missing", "section": name})

    lines = body.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^!\[[^\]]*\]\(([^)]+)\)\s*$", line.strip())
        if not m:
            continue
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        if not (nxt.startswith("*") and nxt.endswith("*")):
            issues.append({"code": "figure_missing_caption", "line": i + 1})
        target = m.group(1)
        if not target.startswith(("http://", "https://", "data:")):
            if not (report_path.parent / target).exists():
                issues.append({"code": "image_missing", "path": target})

    long_paras = []
    for block in re.split(r"\n\s*\n", strip_non_prose(body)):
        s = block.strip()
        if not s or s.startswith(("-", "*", "|", "#", ":::", "$$", "1.")) or re.match(r"^\d+\.", s):
            continue
        n = len(re.findall(r"[\u4e00-\u9fff]", s))
        if n > args.max_para_chars:
            long_paras.append({"chars": n, "start": s[:30]})

    known = normalize_numbers(source)
    unmatched: dict[str, int] = {}
    for tok in NUM_RE.findall(strip_non_prose(body)):
        plain = tok.replace(",", "")
        if tok not in known and plain not in known and tok not in exceptions and plain not in exceptions:
            unmatched[tok] = unmatched.get(tok, 0) + 1

    result = {
        "status": "ok",
        "script": "lint_report.py",
        "report": str(report_path),
        "mode": args.mode,
        "report_sha256": hashlib.sha256(report_path.read_bytes()).hexdigest(),
        "number_exceptions": exceptions,
        "section_count": len(regular),
        "unmatched_numbers": [{"value": k, "count": v} for k, v in sorted(unmatched.items())],
        "issues": issues,
        "long_paragraphs": long_paras,
        "passes_concision": not long_paras,
        "passes_structure": not issues,
        "passes_number_grounding": not unmatched,
    }
    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
