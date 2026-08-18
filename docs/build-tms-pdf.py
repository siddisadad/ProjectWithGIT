#!/usr/bin/env python3
"""Render the DTTP TMS Trainee Task Sheet to a finished A4 PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "DTTP-TMS-TASK-PACK.html"
PDF = ROOT / "DTTP-TMS-TASK-PACK.pdf"

NAVY = (0.043, 0.102, 0.173)
GOLD = (0.722, 0.537, 0.173)
MUTED = (0.42, 0.45, 0.49)

MARKERS = [
    (1, "Purpose", "Build a simple system"),
    (1, "Technology", "Task 01 uses Python"),
    (1, "Main features", "Main features"),
    (1, "Task 01", "No React. No login"),
    (1, "First APIs", "First APIs"),
    (1, "First deliverable", "Working Trainee CRUD API"),
]


def render_html() -> None:
    cmd = [
        "google-chrome-stable",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        "--virtual-time-budget=15000",
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
        is_close = i == total - 1 and "Start with Trainee CRUD" in text
        if is_cover or is_close:
            continue
        width, height = page.rect.width, page.rect.height
        page.draw_line(pymupdf.Point(36, 28), pymupdf.Point(width - 36, 28), color=GOLD, width=0.7)
        page.insert_text(pymupdf.Point(36, 24), "DESHMUKH TECHNOLOGIES", fontname="helv", fontsize=7, color=NAVY)
        page.insert_text(pymupdf.Point(width - 148, 24), "DTTP TMS TASK SHEET", fontname="helv", fontsize=7, color=GOLD)
        page.draw_line(
            pymupdf.Point(36, height - 28),
            pymupdf.Point(width - 36, height - 28),
            color=(0.84, 0.87, 0.90),
            width=0.5,
        )
        page.insert_text(pymupdf.Point(36, height - 16), "Internal use  ·  Version 1.0", fontname="helv", fontsize=7, color=MUTED)
        page.insert_text(pymupdf.Point(width - 68, height - 16), f"{i + 1}  /  {total}", fontname="helv", fontsize=7, color=NAVY)

    toc = [(1, "Cover", 1)]
    found = set()
    for i in range(1, total):
        text = doc[i].get_text("text")
        for level, title, marker in MARKERS:
            if title in found or marker not in text:
                continue
            toc.append((level, title, i + 1))
            found.add(title)
    toc.append((1, "Closing", total))
    doc.set_toc(toc)
    doc.set_metadata(
        {
            "title": "DTTP Real-Time Project 01 — TMS Trainee Task Sheet — Deshmukh Technologies",
            "author": "Deshmukh Technologies",
            "subject": "Simple trainee task sheet: Trainee CRUD first",
            "keywords": "DTTP, TMS, FastAPI, MySQL, trainee, CRUD",
            "creator": "DTTP TMS Task Sheet Builder",
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
