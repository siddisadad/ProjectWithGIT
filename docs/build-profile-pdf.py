#!/usr/bin/env python3
"""Render the Deshmukh Technologies corporate profile to a finished A4 PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "DESHMUKH-TECHNOLOGIES-PROFILE.html"
PDF = ROOT / "DESHMUKH-TECHNOLOGIES-PROFILE.pdf"

NAVY = (0.043, 0.102, 0.173)
GOLD = (0.722, 0.537, 0.173)
MUTED = (0.42, 0.45, 0.49)

MARKERS = [
    (1, "01 Introduction", "Introduction"),
    (1, "02 Our Vision", "Our Vision"),
    (1, "04 Technology Focus", "Technology Focus"),
    (1, "05 Development Philosophy", "Development Philosophy"),
    (1, "07 Trainee Program", "Deshmukh Technologies Trainee Program"),
    (1, "09 Core Values", "Our Core Values"),
    (1, "10 Development Culture", "Our Development Culture"),
    (1, "11 Long-Term Direction", "Our Long-Term Direction"),
]


def render_html() -> None:
    cmd = [
        "google-chrome-stable",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        "--virtual-time-budget=20000",
        f"--print-to-pdf={PDF}",
        HTML.as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def finish_pdf() -> None:
    doc = pymupdf.open(PDF)
    for i in range(doc.page_count - 1, -1, -1):
        if not doc[i].get_text("text").strip():
            doc.delete_page(i)

    total = doc.page_count

    for i, page in enumerate(doc):
        text = page.get_text("text")
        is_cover = i == 0
        is_close = i == total - 1 and "Building technology" in text
        if is_cover or is_close:
            continue
        width = page.rect.width
        height = page.rect.height
        page.draw_line(pymupdf.Point(36, 28), pymupdf.Point(width - 36, 28), color=GOLD, width=0.7)
        page.insert_text(pymupdf.Point(36, 24), "DESHMUKH TECHNOLOGIES", fontname="helv", fontsize=7, color=NAVY)
        page.insert_text(pymupdf.Point(width - 148, 24), "CORPORATE PROFILE", fontname="helv", fontsize=7, color=GOLD)
        page.draw_line(
            pymupdf.Point(36, height - 28),
            pymupdf.Point(width - 36, height - 28),
            color=(0.84, 0.87, 0.90),
            width=0.5,
        )
        page.insert_text(
            pymupdf.Point(36, height - 16),
            "Internal use  ·  Version 1.0",
            fontname="helv",
            fontsize=7,
            color=MUTED,
        )
        page.insert_text(
            pymupdf.Point(width - 68, height - 16),
            f"{i + 1}  /  {total}",
            fontname="helv",
            fontsize=7,
            color=NAVY,
        )

    toc = [(1, "Cover", 1)]
    contents_idx = 1
    for i, page in enumerate(doc):
        text = page.get_text("text")
        if i > 0 and "Contents" in text and "Introduction" in text:
            contents_idx = i
            break
    toc.append((1, "Contents", contents_idx + 1))
    found = set()
    for i in range(contents_idx + 1, total):
        text = doc[i].get_text("text")
        for level, title, marker in MARKERS:
            if title in found:
                continue
            if marker in text:
                toc.append((level, title, i + 1))
                found.add(title)
    toc.append((1, "Closing", total))
    doc.set_toc(toc)
    doc.set_metadata(
        {
            "title": "Deshmukh Technologies — Corporate Master Profile",
            "author": "Deshmukh Technologies",
            "subject": "Corporate master profile: vision, mission, technology, people, and DTTP",
            "keywords": "Deshmukh Technologies, corporate profile, DTTP",
            "creator": "Deshmukh Profile Builder",
        }
    )
    tmp = PDF.with_suffix(".tmp.pdf")
    doc.save(tmp, deflate=True, garbage=4)
    doc.close()
    tmp.replace(PDF)


if __name__ == "__main__":
    render_html()
    finish_pdf()
    print(f"Wrote {PDF}")
