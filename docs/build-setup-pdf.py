#!/usr/bin/env python3
"""Render the DTTP Software Setup guide to a finished A4 PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "DTTP-SOFTWARE-SETUP.html"
PDF = ROOT / "DTTP-SOFTWARE-SETUP.pdf"

NAVY = (0.043, 0.102, 0.173)
GOLD = (0.722, 0.537, 0.173)
MUTED = (0.42, 0.45, 0.49)

MARKERS = [
    (1, "Purpose", "Purpose"),
    (1, "Windows preparation", "Windows preparation"),
    (1, "GitHub SSH configuration", "GitHub SSH configuration"),
    (1, "Java JDK", "Java JDK"),
    (1, "Spring Boot verification", "Spring Boot verification"),
    (1, "MySQL verification", "MySQL verification"),
    (1, "Environment verification", "Environment verification"),
    (1, "Troubleshooting", "Troubleshooting"),
    (1, "Trainee setup checklist", "Trainee setup checklist"),
    (1, "Trainee sign-off", "Trainee sign-off"),
    (1, "Mentor / admin verification", "Mentor / admin verification"),
    (1, "Day-1 hour plan", "Finish this clock"),
    (1, "Official product names", "Download from the vendor"),
    (1, "Mentor 10-minute station check", "Sit at the trainee machine"),
    (1, "Day-1 completion criteria", "Until Day 1 is complete"),
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
        is_close = i == total - 1 and "Install. Configure. Verify" in text
        if is_cover or is_close:
            continue
        width, height = page.rect.width, page.rect.height
        page.draw_line(pymupdf.Point(36, 28), pymupdf.Point(width - 36, 28), color=GOLD, width=0.7)
        page.insert_text(pymupdf.Point(36, 24), "DESHMUKH TECHNOLOGIES", fontname="helv", fontsize=7, color=NAVY)
        page.insert_text(pymupdf.Point(width - 178, 24), "DTTP SOFTWARE SETUP", fontname="helv", fontsize=7, color=GOLD)
        page.draw_line(
            pymupdf.Point(36, height - 28),
            pymupdf.Point(width - 36, height - 28),
            color=(0.84, 0.87, 0.90),
            width=0.5,
        )
        page.insert_text(pymupdf.Point(36, height - 16), "Internal use  ·  Version 1.2", fontname="helv", fontsize=7, color=MUTED)
        page.insert_text(pymupdf.Point(width - 68, height - 16), f"{i + 1}  /  {total}", fontname="helv", fontsize=7, color=NAVY)

    toc = [(1, "Cover", 1)]
    contents_idx = 1
    for i, page in enumerate(doc):
        if i > 0 and "Contents" in page.get_text("text") and "Software checklist" in page.get_text("text"):
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
            "title": "DTTP Trainee Software Setup & Environment Verification — Deshmukh Technologies",
            "author": "Deshmukh Technologies",
            "subject": "Windows onboarding and environment verification for DTTP trainees",
            "keywords": "DTTP, setup, Windows, Java, React, MySQL, Git, Docker, Flutter",
            "creator": "DTTP Setup Guide Builder",
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
