#!/usr/bin/env python3
"""Render the DTTP Self-Growth Program to a finished A4 PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "DTTP-SELF-GROWTH-PROGRAM.html"
PDF = ROOT / "DTTP-SELF-GROWTH-PROGRAM.pdf"

NAVY = (0.043, 0.102, 0.173)
GOLD = (0.722, 0.537, 0.173)
MUTED = (0.42, 0.45, 0.49)

MARKERS = [
    (1, "How to use this program", "How to use this program"),
    (1, "Level 1 — Web Fundamentals", "Level 1 — Web Fundamentals"),
    (1, "Level 2 — Frontend Engineering", "Level 2 — Frontend Engineering"),
    (1, "Level 3 — React & Modern Frontend", "Level 3 — React"),
    (1, "Level 4 — Web Communication & APIs", "Level 4 — Web Communication"),
    (1, "Level 5 — Backend Development", "Level 5 — Backend Development"),
    (1, "Level 6 — Database Engineering", "Level 6 — Database Engineering"),
    (1, "Level 7 — Architecture", "Level 7 — Architecture"),
    (1, "Level 8 — Testing, Security & Performance", "Level 8 — Testing"),
    (1, "Level 9 — DevOps & Deployment", "Level 9 — DevOps"),
    (1, "Level 10 — Professional Software Engineering", "Level 10 — Professional"),
    (1, "Incremental Employee Management build", "Incremental Employee Management"),
    (1, "Oral review bank", "Oral review bank"),
    (1, "Depth ladder", "Depth ladder"),
    (1, "Official progression", "Official progression"),
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
        is_close = i == total - 1 and "Self-Directed Full-Stack Developer" in text
        if is_cover or is_close:
            continue
        width, height = page.rect.width, page.rect.height
        page.draw_line(pymupdf.Point(36, 28), pymupdf.Point(width - 36, 28), color=GOLD, width=0.7)
        page.insert_text(pymupdf.Point(36, 24), "DESHMUKH TECHNOLOGIES", fontname="helv", fontsize=7, color=NAVY)
        page.insert_text(pymupdf.Point(width - 168, 24), "DTTP SELF-GROWTH PROGRAM", fontname="helv", fontsize=7, color=GOLD)
        page.draw_line(
            pymupdf.Point(36, height - 28),
            pymupdf.Point(width - 36, height - 28),
            color=(0.84, 0.87, 0.90),
            width=0.5,
        )
        page.insert_text(pymupdf.Point(36, height - 16), "Internal use  ·  Version 1.3", fontname="helv", fontsize=7, color=MUTED)
        page.insert_text(pymupdf.Point(width - 68, height - 16), f"{i + 1}  /  {total}", fontname="helv", fontsize=7, color=NAVY)

    toc = [(1, "Cover", 1)]
    contents_idx = 1
    for i, page in enumerate(doc):
        if i > 0 and "Contents" in page.get_text("text") and "Web Fundamentals" in page.get_text("text"):
            contents_idx = i
            break
    toc.append((1, "Contents", contents_idx + 1))
    found = set()
    for i in range(contents_idx + 1, total):
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
            "title": "DTTP Self-Growth Program — Deshmukh Technologies",
            "author": "Deshmukh Technologies",
            "subject": "Ten-level full-stack self-growth roadmap",
            "keywords": "DTTP, self-growth, full-stack, Deshmukh Technologies",
            "creator": "DTTP Self-Growth Builder",
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
