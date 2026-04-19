#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDERS = (
    "replace-me",
    "TARGET_SEQUENCE_HERE",
    "REPLACE_ME",
    "POSITIVE_PEPTIDE_SEQUENCE_HERE",
    "NEGATIVE_PEPTIDE_SEQUENCE_HERE",
    "CANDIDATE_PEPTIDE_SEQUENCE_HERE",
)


def scan_text_file(path: Path) -> list[str]:
    text = path.read_text()
    hits = [token for token in PLACEHOLDERS if token in text]
    return [f"{path.relative_to(ROOT)} contains placeholder `{token}`" for token in hits]


def validate_json_file(path: Path) -> list[str]:
    problems = scan_text_file(path)
    try:
        json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        problems.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
    return problems


def main() -> int:
    problems: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir():
            continue
        if path.name.startswith("."):
            continue
        if path.suffix == ".json":
            problems.extend(validate_json_file(path))
        elif path.suffix in {".md", ".txt"}:
            problems.extend(scan_text_file(path))

    if problems:
        print("Preflight validation failed:")
        for item in problems:
            print(f"- {item}")
        return 1

    print("Preflight validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
