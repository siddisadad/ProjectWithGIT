#!/usr/bin/env python3
"""Render the DTTP handbook HTML to a finished A4 PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "DTTP-PROGRAM-HANDBOOK.html"
PDF = ROOT / "DTTP-PROGRAM-HANDBOOK.pdf"

NAVY = (0.043, 0.102, 0.173)
GOLD = (0.722, 0.537, 0.173)
MUTED = (0.42, 0.45, 0.49)


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


MARKERS = [
    (1, "Part I — Program Foundation", "Program Foundation"),
    (2, "01 Program Purpose", "Program Purpose"),
    (2, "07 90-Day Master Roadmap", "90-Day Master Roadmap"),
    (1, "Part II — Technical Curriculum", "Technical Curriculum"),
    (2, "14 Java Track", "Java Track"),
    (2, "20 REST API", "Both backend tracks implement"),
    (1, "Part III — Project & Engineering", "Project & Engineering"),
    (2, "21 Major Training Project", "Major Training Project"),
    (1, "Part IV — Assessment & Career", "Assessment & Career"),
    (2, "30 Definition of Done", "A feature is complete only when"),
    (2, "36 Weekly Score", "Weekly Score"),
    (2, "42 Final DTTP Standard", "Final DTTP Standard"),
]


def finish_pdf() -> None:
    doc = pymupdf.open(PDF)
    for i in range(doc.page_count - 1, -1, -1):
        if not doc[i].get_text("text").strip():
            doc.delete_page(i)

    total = doc.page_count

    for i, page in enumerate(doc):
        text = page.get_text("text")
        is_cover = i == 0
        is_close = i == total - 1 and "Learn. Build. Solve" in text
        if is_cover or is_close:
            continue
        width = page.rect.width
        height = page.rect.height

        page.draw_line(pymupdf.Point(36, 28), pymupdf.Point(width - 36, 28), color=GOLD, width=0.7)
        page.insert_text(
            pymupdf.Point(36, 24),
            "DESHMUKH TECHNOLOGIES",
            fontname="helv",
            fontsize=7,
            color=NAVY,
        )
        page.insert_text(
            pymupdf.Point(width - 168, 24),
            "DTTP PROGRAM HANDBOOK",
            fontname="helv",
            fontsize=7,
            color=GOLD,
        )
        page.draw_line(
            pymupdf.Point(36, height - 28),
            pymupdf.Point(width - 36, height - 28),
            color=(0.84, 0.87, 0.90),
            width=0.5,
        )
        page.insert_text(
            pymupdf.Point(36, height - 16),
            "Internal use  ·  Version 1.4",
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
        if i > 0 and "Contents" in text and "Program Purpose" in text:
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
            "title": "DTTP — Deshmukh Technologies Trainee Program",
            "author": "Deshmukh Technologies",
            "subject": "90-Day Full-Stack Trainee Program Handbook",
            "keywords": "DTTP, trainee program, full-stack, Deshmukh Technologies",
            "creator": "DTTP Handbook Builder",
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
