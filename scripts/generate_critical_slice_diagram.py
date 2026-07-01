#!/usr/bin/env python3
"""Generate a small SVG diagram for the critical line / critical slice model."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_OUTPUT = Path("figures/critical_slice.svg")


def build_svg(width: int = 920, height: int = 520) -> str:
    left_x = 110
    left_y = 92
    left_w = 300
    left_h = 320
    right_x = 535
    right_y = 92
    right_w = 275
    right_h = 320
    critical_x = left_x + left_w // 2
    slice_x = right_x + right_w // 2

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Critical line and quaternionic critical slice</title>
  <desc id="desc">A schematic showing Re(s)=1/2 as the complex projection of Re(q)=1/2.</desc>
  <rect width="100%" height="100%" fill="#f8fafc"/>
  <text x="{width // 2}" y="42" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="700" fill="#0f172a">Quaternionic Critical Slice Projection</text>

  <g aria-label="complex plane panel">
    <rect x="{left_x}" y="{left_y}" width="{left_w}" height="{left_h}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="{left_x + 38}" y1="{left_y + left_h - 44}" x2="{left_x + left_w - 34}" y2="{left_y + left_h - 44}" stroke="#475569" stroke-width="2"/>
    <line x1="{left_x + 58}" y1="{left_y + left_h - 24}" x2="{left_x + 58}" y2="{left_y + 34}" stroke="#475569" stroke-width="2"/>
    <line x1="{critical_x}" y1="{left_y + left_h - 44}" x2="{critical_x}" y2="{left_y + 45}" stroke="#2563eb" stroke-width="5"/>
    <text x="{critical_x}" y="{left_y + 74}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="700" fill="#1d4ed8">Re(s)=1/2</text>
    <text x="{left_x + left_w - 38}" y="{left_y + left_h - 18}" font-family="Arial, sans-serif" font-size="14" fill="#334155">Re(s)</text>
    <text x="{left_x + 18}" y="{left_y + 44}" font-family="Arial, sans-serif" font-size="14" fill="#334155">Im(s)</text>
    <circle cx="{critical_x}" cy="{left_y + 123}" r="5" fill="#0f766e"/>
    <circle cx="{critical_x}" cy="{left_y + 185}" r="5" fill="#0f766e"/>
    <circle cx="{critical_x}" cy="{left_y + 250}" r="5" fill="#0f766e"/>
    <text x="{left_x + left_w // 2}" y="{left_y + left_h + 38}" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#0f172a">complex critical line</text>
  </g>

  <g aria-label="quaternionic slice panel">
    <rect x="{right_x}" y="{right_y}" width="{right_w}" height="{right_h}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
    <ellipse cx="{slice_x}" cy="{right_y + 195}" rx="112" ry="54" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/>
    <ellipse cx="{slice_x}" cy="{right_y + 195}" rx="62" ry="30" fill="none" stroke="#60a5fa" stroke-width="2"/>
    <line x1="{slice_x}" y1="{right_y + 65}" x2="{slice_x}" y2="{right_y + 305}" stroke="#1d4ed8" stroke-width="5"/>
    <line x1="{right_x + 52}" y1="{right_y + 265}" x2="{right_x + right_w - 34}" y2="{right_y + 119}" stroke="#64748b" stroke-width="2"/>
    <line x1="{right_x + 56}" y1="{right_y + 118}" x2="{right_x + right_w - 42}" y2="{right_y + 272}" stroke="#64748b" stroke-width="2"/>
    <text x="{slice_x}" y="{right_y + 54}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="700" fill="#1d4ed8">Re(q)=1/2</text>
    <text x="{right_x + right_w - 62}" y="{right_y + 108}" font-family="Arial, sans-serif" font-size="14" fill="#334155">Im(q)</text>
    <text x="{right_x + 26}" y="{right_y + 278}" font-family="Arial, sans-serif" font-size="14" fill="#334155">slice directions</text>
    <circle cx="{slice_x}" cy="{right_y + 145}" r="5" fill="#0f766e"/>
    <circle cx="{slice_x}" cy="{right_y + 195}" r="5" fill="#0f766e"/>
    <circle cx="{slice_x}" cy="{right_y + 245}" r="5" fill="#0f766e"/>
    <text x="{right_x + right_w // 2}" y="{right_y + right_h + 38}" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#0f172a">quaternionic equilibrium slice</text>
  </g>

  <path d="M 430 248 C 462 218, 494 218, 525 248" fill="none" stroke="#0f172a" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="477" y="205" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#0f172a">projection</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L7,3 z" fill="#0f172a"/>
    </marker>
  </defs>

  <text x="{width // 2}" y="478" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#334155">Conjectural direction: zeta symmetry -> classical scale-stability defect -> optional quaternionic lift</text>
</svg>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="SVG output path",
    )
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_svg(), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
