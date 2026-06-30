#!/usr/bin/env python3
"""Check relative links in Markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def iter_markdown_files(root: Path) -> list[Path]:
    paths = [root / "README.md", root / "CONJECTURE.md", root / "CLAIM_DISCIPLINE.md", root / "ROADMAP.md"]
    paths.extend(sorted((root / "docs").glob("*.md")))
    return [path for path in paths if path.exists()]


def target_exists(markdown_file: Path, raw_target: str) -> bool:
    target = raw_target.strip()
    if not target or target.startswith(SKIP_PREFIXES):
        return True
    if "://" in target:
        return True

    target = target.split("#", 1)[0]
    if not target:
        return True

    candidate = (markdown_file.parent / target).resolve()
    return candidate.exists()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    for markdown_file in iter_markdown_files(root):
        text = markdown_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if not target_exists(markdown_file, target):
                failures.append(f"{markdown_file.relative_to(root)} -> {target}")

    if failures:
        print("Broken Markdown links:")
        for failure in failures:
            print(f"  {failure}")
        return 1

    print("Markdown links OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

