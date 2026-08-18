#!/usr/bin/env python3
"""Render the simple TMS trainee handouts to A4 PDFs."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
NAVY = (0.043, 0.102, 0.173)
MUTED = (0.42, 0.45, 0.49)

JOBS = [
    {
        "html": ROOT / "DTTP-TMS-PROJECT.html",
        "pdf": ROOT / "DTTP-TMS-PROJECT.pdf",
        "title": "DTTP TMS — Project Sheet — Deshmukh Technologies",
        "toc": [(1, "TMS Project Sheet", 1)],
    },
    {
        "html": ROOT / "DTTP-TMS-TASK-01.html",
        "pdf": ROOT / "DTTP-TMS-TASK-01.pdf",
        "title": "DTTP TMS — Task 01 Trainee CRUD — Deshmukh Technologies",
        "toc": [(1, "Task 01 Trainee CRUD", 1)],
    },
]


def render(html: Path, pdf: Path) -> None:
    cmd = [
        "google-chrome-stable",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        "--virtual-time-budget=12000",
        f"--print-to-pdf={pdf}",
        html.as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def finish(job: dict) -> None:
    pdf = job["pdf"]
    doc = pymupdf.open(pdf)
    for i in range(doc.page_count - 1, -1, -1):
        if not doc[i].get_text("text").strip():
            doc.delete_page(i)
    total = doc.page_count
    for i, page in enumerate(doc):
        width, height = page.rect.width, page.rect.height
        page.insert_text(
            pymupdf.Point(width - 68, height - 14),
            f"{i + 1}  /  {total}",
            fontname="helv",
            fontsize=7,
            color=NAVY,
        )
        page.insert_text(
            pymupdf.Point(36, height - 14),
            "Deshmukh Technologies  ·  Internal use",
            fontname="helv",
            fontsize=7,
            color=MUTED,
        )
    doc.set_toc(job["toc"])
    doc.set_metadata(
        {
            "title": job["title"],
            "author": "Deshmukh Technologies",
            "subject": "Simple DTTP trainee handout",
            "keywords": "DTTP, TMS, FastAPI, MySQL",
            "creator": "DTTP TMS Handout Builder",
        }
    )
    tmp = pdf.with_suffix(".tmp.pdf")
    doc.save(tmp, deflate=True, garbage=4)
    doc.close()
    tmp.replace(pdf)
    print(f"Wrote {pdf} ({total} page{'s' if total != 1 else ''})")


def main() -> None:
    for job in JOBS:
        render(job["html"], job["pdf"])
        finish(job)


if __name__ == "__main__":
    main()
