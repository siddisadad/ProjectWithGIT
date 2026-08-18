#!/usr/bin/env python3
"""Render TMS trainee PDFs."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
NAVY = (0.043, 0.102, 0.173)
GOLD = (0.722, 0.537, 0.173)
MUTED = (0.42, 0.45, 0.49)

BRIEF_MARKERS = [
    (1, "Project goal", "complete DTTP trainee lifecycle"),
    (1, "Technology stack", "Pydantic"),
    (1, "User roles", "Own activities"),
    (1, "Authentication", "Role-based access"),
    (1, "Trainee management", "Joining Date"),
    (1, "Batch management", "DTTP-2026-01"),
    (1, "Mentor management", "activate/deactivate a mentor"),
    (1, "Attendance", "attendance percentage"),
    (1, "Task management", "UNDER_REVIEW"),
    (1, "Assignment and submission", "Create Assignment"),
    (1, "Evaluation", "Problem Solving"),
    (1, "Feedback", "areas for improvement"),
    (1, "Dashboard", "Attendance %"),
    (1, "Database design", "User → Trainee"),
    (1, "Backend architecture", "never commit secrets"),
    (1, "Frontend architecture", "Trainee Details"),
    (1, "First MVP", "Do not build all modules"),
    (1, "Development sprints", "GitHub repo, backend"),
    (1, "First real-time requirement", "centralized trainee database"),
    (1, "Trainee development workflow", "how real software teams work"),
]

COMPLETE_MARKERS = [
    (1, "Project Overview", "replace manual trainee records"),
    (1, "Project Goals", "real software-development lifecycle"),
    (1, "User Roles", "Create users"),
    (1, "Main Modules", "User Management"),
    (1, "Authentication", "Protected APIs"),
    (1, "Trainee Management", "Date of Birth"),
    (1, "Batch Management", "view batch members"),
    (1, "Mentor Management", "Specialization"),
    (1, "Attendance", "Total Working Days"),
    (1, "Task Management", "UNDER_REVIEW"),
    (1, "Assignment Management", "Assigned Batch"),
    (1, "Submission", "Changes Required"),
    (1, "Evaluation", "Professionalism"),
    (1, "Feedback", "weekly review"),
    (1, "Dashboard", "Upcoming Deadlines"),
    (1, "Reports", "Performance Report"),
    (1, "Database Design", "Initial tables"),
    (1, "Backend Architecture", "FastAPI Router"),
    (1, "Frontend Architecture", "package.json"),
    (1, "Important APIs", "POST /api/auth/login"),
    (1, "MVP — First Release", "Do not build every feature immediately"),
    (1, "Development Plan", "MVP completion"),
    (1, "Month-End QA", "loading states"),
    (1, "GitHub Workflow", "feature/trainee-crud"),
    (1, "QA Workflow", "Bug Found?"),
    (1, "Bug Classification", "workaround exists"),
    (1, "Docker", "docker compose up"),
    (1, "CI/CD", "Docker Image"),
    (1, "Security Requirements", "Never share private SSH keys"),
    (1, "Definition of Done", "QA testing passes"),
    (1, "Final Project Flow", "Trainee Records"),
    (1, "Final DTTP Outcome", "work like a real development team"),
]

JOBS = [
    {
        "html": ROOT / "DTTP-TMS.html",
        "pdf": ROOT / "DTTP-TMS.pdf",
        "title": "DTTP — Trainee Management System — Detailed Real-Time Project Specification",
        "subject": "DTTP-TMS-001 detailed real-time project specification",
        "headers": True,
        "header_label": "DTTP-TMS-001",
        "markers": COMPLETE_MARKERS,
        "skip_first_header": True,
    },
    {
        "html": ROOT / "DTTP-TMS-BRIEF.html",
        "pdf": ROOT / "DTTP-TMS-BRIEF.pdf",
        "title": "DTTP — Trainee Management System — Real-Time Project 01",
        "subject": "Internal business application brief for DTTP trainees",
        "headers": True,
        "header_label": "DTTP TMS PROJECT 01",
        "markers": BRIEF_MARKERS,
        "skip_first_header": True,
    },
    {
        "html": ROOT / "DTTP-TMS-MVP-1.html",
        "pdf": ROOT / "DTTP-TMS-MVP-1.pdf",
        "title": "DTTP TMS — MVP-1 First Assignment — Deshmukh Technologies",
        "headers": False,
        "toc": [(1, "MVP-1 First Assignment", 1)],
    },
    {
        "html": ROOT / "DTTP-TMS-SPRINT-1.html",
        "pdf": ROOT / "DTTP-TMS-SPRINT-1.pdf",
        "title": "DTTP TMS — Sprint 1 Project Setup — Deshmukh Technologies",
        "headers": False,
        "toc": [(1, "Sprint 1 Project Setup", 1)],
    },
    {
        "html": ROOT / "DTTP-TMS-PROJECT-01.html",
        "pdf": ROOT / "DTTP-TMS-PROJECT-01.pdf",
        "title": "DTTP — Trainee Management System (TMS) — Real-Time Project 01",
        "headers": False,
        "toc": [(1, "Trainee Management System", 1)],
    },
    {
        "html": ROOT / "DTTP-TMS-PROJECT.html",
        "pdf": ROOT / "DTTP-TMS-PROJECT.pdf",
        "title": "DTTP TMS — Project Sheet — Deshmukh Technologies",
        "headers": False,
        "toc": [(1, "TMS Project Sheet", 1)],
    },
    {
        "html": ROOT / "DTTP-TMS-TASK-01.html",
        "pdf": ROOT / "DTTP-TMS-TASK-01.pdf",
        "title": "DTTP TMS — Task 01 Trainee CRUD — Deshmukh Technologies",
        "headers": False,
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
        "--virtual-time-budget=20000",
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

    if job.get("headers"):
        for i, page in enumerate(doc):
            if job.get("skip_first_header") and i == 0:
                continue
            width, height = page.rect.width, page.rect.height
            page.draw_line(pymupdf.Point(36, 28), pymupdf.Point(width - 36, 28), color=GOLD, width=0.7)
            page.insert_text(pymupdf.Point(36, 24), "DESHMUKH TECHNOLOGIES", fontname="helv", fontsize=7, color=NAVY)
            page.insert_text(
                pymupdf.Point(width - 168, 24),
                job.get("header_label", "DTTP TMS"),
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
            page.insert_text(pymupdf.Point(36, height - 16), "Internal use  ·  Version 1.0", fontname="helv", fontsize=7, color=MUTED)
            page.insert_text(pymupdf.Point(width - 68, height - 16), f"{i + 1}  /  {total}", fontname="helv", fontsize=7, color=NAVY)

    toc = [(1, "Cover", 1)] if job.get("headers") else []
    if job.get("markers"):
        found = set()
        for i in range(total):
            text = doc[i].get_text("text")
            for level, title, marker in job["markers"]:
                if title in found or marker not in text:
                    continue
                toc.append((level, title, i + 1))
                found.add(title)
    elif job.get("toc"):
        toc = job["toc"]
    if toc:
        doc.set_toc(toc)
    doc.set_metadata(
        {
            "title": job["title"],
            "author": "Deshmukh Technologies",
            "subject": job.get("subject", "DTTP TMS trainee document"),
            "keywords": "DTTP, TMS, FastAPI, MySQL, React",
            "creator": "DTTP TMS PDF Builder",
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
