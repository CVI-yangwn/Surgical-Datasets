#!/usr/bin/env python3
"""Record one reading round: note/report snapshots, hashes, weighted score.

Exactly two rounds (see references/report-scorecard.md):
  round 1  stage=baseline          the note saved by the original DeepPaperNote flow;
                                   record it BEFORE any edit, so it describes what was scored
  round 2  stage=narrative_review  the note and report after the user's method (Insight Pass
                                   with its three passes, then the narrative revision);
                                   record it on the final files
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

WEIGHTS = {"D1": .15, "D2": .15, "D3": .15, "D4": .15, "D5": .10, "D6": .10, "D7": .05, "D8": .05, "D9": .10}
GATES = ("H1", "H2", "H3", "H4")
STAGES = ("baseline", "narrative_review")
MAX_ROUNDS = 2


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def overall(dims: dict[str, float], gates: dict[str, str]) -> float:
    score = round(sum(WEIGHTS[k] * float(v) for k, v in dims.items()) + 1e-9, 1)
    return min(score, 6.0) if any(v == "fail" for v in gates.values()) else score


def expected_stage(n: int) -> str:
    return STAGES[n - 1]


def snapshot(src: Path, snap_dir: Path, n: int) -> tuple[str, str]:
    dest = snap_dir / f"round{n}_{src.name}"
    shutil.copyfile(src, dest)
    return sha256(src), f"{snap_dir.name}/{dest.name}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", required=True, choices=STAGES)
    ap.add_argument("--note", required=True, help="The saved Markdown note")
    ap.add_argument("--report", default="", help="reading_report.md; required from round 2 on")
    ap.add_argument("--scorecard", required=True)
    ap.add_argument("--dimensions", required=True, help='JSON, e.g. {"D1":8,...,"D9":8}')
    ap.add_argument("--gates", default='{"H1":"pass","H2":"pass","H3":"pass","H4":"pass"}')
    ap.add_argument("--verdict", required=True)
    ap.add_argument("--fixes", default="[]",
                    help="round 1: JSON list of edits round 2 will make; round 2: must stay empty")
    a = ap.parse_args()

    note, card_path = Path(a.note), Path(a.scorecard)
    report = Path(a.report) if a.report else None
    dims, gates, fixes = json.loads(a.dimensions), json.loads(a.gates), json.loads(a.fixes)
    if set(dims) != set(WEIGHTS):
        sys.exit(f"dimensions must be exactly {sorted(WEIGHTS)}")
    if set(gates) != set(GATES) or any(v not in ("pass", "fail", "unknown") for v in gates.values()):
        sys.exit("gates must be H1..H4 with pass, fail, or unknown")
    if not isinstance(fixes, list):
        sys.exit("--fixes must be a JSON list")

    card = json.loads(card_path.read_text(encoding="utf-8")) if card_path.exists() else {
        "kind": "model_self_review", "rubric": "references/report-scorecard.md", "rounds": []}
    rounds = card["rounds"]
    n = len(rounds) + 1
    if n > MAX_ROUNDS:
        sys.exit("both rounds are recorded; fix problems before recording round 2, not after")
    if a.stage != expected_stage(n):
        sys.exit(f"round {n} must be stage={expected_stage(n)}, got {a.stage}")
    if n == 1 and report:
        sys.exit("round 1 scores the original note only; write reading_report.md in round 2")
    if n >= 2 and not (report and report.exists()):
        sys.exit("from round 2 on, --report must point to an existing reading_report.md")
    if n == 1 and not fixes:
        sys.exit("round 1 must list the fixes round 2 will make; the narrative review always has work")
    if n == 2 and fixes:
        sys.exit("round 2 scores the final files: apply the fixes first, then record. Put limits that "
                 "cannot be fixed in the verdict")

    snap_dir = card_path.parent / "review_rounds"
    snap_dir.mkdir(exist_ok=True)
    note_sha, note_snap = snapshot(note, snap_dir, n)
    rep_sha, rep_snap = snapshot(report, snap_dir, n) if report else ("", "")
    prev = rounds[-1] if rounds else {}
    entry = {
        "round": n, "stage": a.stage,
        "note_sha256": note_sha, "note_snapshot": note_snap,
        "report_sha256": rep_sha, "report_snapshot": rep_snap,
        "changed_since_previous": bool(prev) and (note_sha != prev.get("note_sha256")
                                                  or rep_sha != prev.get("report_sha256")),
        "hard_gates": gates, "dimensions": dims, "overall": overall(dims, gates),
        "verdict": a.verdict, "fixes": fixes,
    }
    rounds.append(entry)
    card_path.write_text(json.dumps(card, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"round": n, "stage": a.stage, "overall": entry["overall"],
                      "note_sha256": note_sha[:12], "report_sha256": rep_sha[:12],
                      "changed_since_previous": entry["changed_since_previous"],
                      "closed": n == 2}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
