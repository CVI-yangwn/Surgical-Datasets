#!/usr/bin/env python3
"""Publish one finished DeepPaperNote reading into docs/papers/<slug>/.

The skill writes its output under DeepPaperNote_output/ (ignored by git). This
copies the parts worth sharing into a short, fixed layout and renders the web
page with linked images instead of embedded ones:

    docs/papers/<slug>/
      index.html     web page (images linked from images/)
      note.md        Markdown reading note
      report.md      source of the web page
      images/
      review/        scorecard.json, review_rounds/, insight_pass.json, lint and number checks

Refuses to publish when the scorecard does not match the note and report
(the same check as render_html.py --strict).

Usage: python3 tools/publish_paper.py <paper output dir> --slug <slug>
"""
import argparse
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / ".claude" / "skills" / "deeppapernote" / "scripts"
REPO_BLOB = "https://github.com/CVI-yangwn/Surgical-Datasets/blob/main/"
REVIEW_FILES = ("scorecard.json", "insight_pass.json", "report_lint.json",
                "number_exceptions.json", "save_log.jsonl")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paper_dir", type=Path)
    ap.add_argument("--slug", required=True)
    a = ap.parse_args()

    src = a.paper_dir.resolve()
    notes = [p for p in src.glob("*.md") if p.name != "reading_report.md"]
    if len(notes) != 1:
        sys.exit(f"expected one note .md in {src}, found {[p.name for p in notes]}")
    for need in ("reading_report.md", "scorecard.json", "review_rounds", "images"):
        if not (src / need).exists():
            sys.exit(f"{src} has no {need}; finish the reading first")

    sys.path.insert(0, str(SCRIPTS))
    import json
    from render_html import build, card_problems

    problems = card_problems(json.loads((src / "scorecard.json").read_text(encoding="utf-8")),
                             src / "reading_report.md", notes[0])
    if problems:
        sys.exit("not published: " + "; ".join(problems))

    dest = ROOT / "docs" / "papers" / a.slug
    if dest.exists():
        shutil.rmtree(dest)
    (dest / "review").mkdir(parents=True)
    shutil.copyfile(notes[0], dest / "note.md")
    shutil.copyfile(src / "reading_report.md", dest / "report.md")
    shutil.copytree(src / "images", dest / "images")
    for name in REVIEW_FILES:
        if (src / name).exists():
            shutil.copyfile(src / name, dest / "review" / name)
    shutil.copytree(src / "review_rounds", dest / "review" / "review_rounds")

    load = lambda name: (json.loads((dest / "review" / name).read_text(encoding="utf-8"))
                         if (dest / "review" / name).exists() else None)
    page = build(dest / "report.md", dest / "review" / "scorecard.json", dest / "note.md",
                 load("report_lint.json"), load("insight_pass.json"), embed=False,
                 note_href=REPO_BLOB + quote(f"docs/papers/{a.slug}/note.md"))
    (dest / "index.html").write_text(page, encoding="utf-8")
    size = sum(p.stat().st_size for p in dest.rglob("*") if p.is_file())
    print(f"docs/papers/{a.slug}/  {size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
