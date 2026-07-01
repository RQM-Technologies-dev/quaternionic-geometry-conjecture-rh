#!/usr/bin/env python3
"""Run smoke checks for the repository."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figures" / "critical_slice.svg"


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    run([sys.executable, "scripts/generate_critical_slice_diagram.py"])
    svg = FIGURE.read_text(encoding="utf-8")
    required = ["Re(s)=1/2", "Re(q)=1/2", "projection", "scale-stability"]
    missing = [item for item in required if item not in svg]
    if missing:
        print(f"Figure is missing expected labels: {', '.join(missing)}")
        return 1

    run([sys.executable, "scripts/check_markdown_links.py"])
    print("Smoke checks OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
