#!/usr/bin/env python3
"""Check an insight_pass.json: required rounds, evidence ids, honest gaps."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

STATUS = {"resolved", "partly", "not_stated"}
VERDICT = {"supported", "partly_supported", "not_separated"}


def section_ids(manifest: dict) -> set[str]:
    ids = {s.get("section_id", "") for s in manifest.get("sections", [])}
    for page in manifest.get("pages", []):
        ids.update(page.get("section_ids", []) or [])
    return {i for i in ids if i}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--insight", required=True)
    ap.add_argument("--source-manifest", required=True)
    ap.add_argument("--output", default="")
    a = ap.parse_args()

    data = json.loads(Path(a.insight).read_text(encoding="utf-8"))
    ids = section_ids(json.loads(Path(a.source_manifest).read_text(encoding="utf-8")))
    issues: list[dict] = []

    kps = data.get("knowledge_points", [])
    if len(kps) < 4:
        issues.append({"code": "too_few_knowledge_points", "count": len(kps)})
    for i, k in enumerate(kps):
        for f in ("term", "plain", "where", "needed_for"):
            if not str(k.get(f, "")).strip():
                issues.append({"code": "knowledge_point_field_empty", "index": i, "field": f})
        if k.get("where") and k["where"] not in ids:
            issues.append({"code": "unknown_section_id", "index": i, "value": k["where"]})

    qs = data.get("detail_questions", [])
    if len(qs) < 6:
        issues.append({"code": "too_few_detail_questions", "count": len(qs)})
    for i, q in enumerate(qs):
        if q.get("status") not in STATUS:
            issues.append({"code": "bad_status", "index": i, "value": q.get("status")})
        if not str(q.get("answer", "")).strip():
            issues.append({"code": "answer_empty", "index": i})
        ev = q.get("evidence", [])
        if q.get("status") in ("resolved", "partly") and not ev:
            issues.append({"code": "resolved_without_evidence", "index": i})
        for e in ev:
            if e not in ids:
                issues.append({"code": "unknown_section_id", "index": i, "value": e})

    ch = data.get("challenges", [])
    if not ch:
        issues.append({"code": "no_challenges"})
    for i, c in enumerate(ch):
        if c.get("verdict") not in VERDICT:
            issues.append({"code": "bad_verdict", "index": i, "value": c.get("verdict")})
        for f in ("claim", "alternative", "separating_evidence"):
            if not str(c.get(f, "")).strip():
                issues.append({"code": "challenge_field_empty", "index": i, "field": f})

    warnings = []
    if not data.get("revisions"):
        warnings.append("no_revisions_recorded")
    if not any(q.get("status") == "not_stated" for q in qs):
        warnings.append("no_gap_named")

    result = {
        "status": "ok", "script": "lint_insight.py",
        "counts": {"knowledge_points": len(kps), "detail_questions": len(qs), "challenges": len(ch)},
        "issues": issues, "warnings": warnings, "passes_insight": not issues,
    }
    out = json.dumps(result, ensure_ascii=False, indent=2)
    if a.output:
        Path(a.output).write_text(out, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
