#!/usr/bin/env python3
"""Run smoke checks for the repository."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OVERCLAIM_RE = re.compile(
    r"proves RH|solves RH|Clay solution|CMI-recognized|final proof|completed proof",
    re.IGNORECASE,
)
OVERCLAIM_PATHS = [
    ROOT / "README.md",
    ROOT / "CLAIM_DISCIPLINE.md",
    ROOT / "ROADMAP.md",
    ROOT / "docs",
]


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def iter_markdown(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(files)


def check_overclaims() -> int:
    failures: list[str] = []
    for path in iter_markdown(OVERCLAIM_PATHS):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if OVERCLAIM_RE.search(line):
                rel = path.relative_to(ROOT)
                failures.append(f"{rel}:{line_number}: {line.strip()}")

    if failures:
        print("Overclaim scan found matches:")
        for failure in failures:
            print(f"  {failure}")
        return 1

    print("Overclaim scan OK")
    return 0


def main() -> int:
    run([sys.executable, "scripts/check_markdown_links.py"])
    if check_overclaims() != 0:
        return 1
    print("Smoke checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
