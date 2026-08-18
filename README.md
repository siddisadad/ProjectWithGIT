# Deshmukh Technologies

**Technology · Innovation · Engineering · Growth**

> Building technology. Developing people. Solving real problems.

This repository holds the official internal document family. Each document has a Markdown source, a print-first HTML design, and a generated A4 PDF.

## Document family

| Document | Audience | Use it when | Version |
| --- | --- | --- | :---: |
| [Corporate Master Profile](docs/DESHMUKH-TECHNOLOGIES-PROFILE.pdf) | Leadership, new joiners, partners | You need identity, values, and working method | 1.2 |
| [DTTP 90-Day Handbook](docs/DTTP-PROGRAM-HANDBOOK.pdf) | Mentors and trainees | You need the timed path, project, and graduation rules | 1.5 |
| [DTTP Software Setup](docs/DTTP-SOFTWARE-SETUP.pdf) | Trainees, mentors, coordinators | Day-1 Windows environment, GitHub SSH, and sign-off | 1.0 |
| [DTTP Self-Growth Program](docs/DTTP-SELF-GROWTH-PROGRAM.pdf) | Trainees and self-directed engineers | You need the ten-level knowledge map around the 90 days | 1.6 |
| [TMS Project Brief](docs/DTTP-TMS-BRIEF.pdf) | Python-track trainees | Full Real-Time Project 01 specification | 1.0 |
| [TMS Real-Time Project 01](docs/DTTP-TMS-PROJECT-01.pdf) | Python-track trainees | Short project outline | 1.0 |
| [TMS Project Sheet](docs/DTTP-TMS-PROJECT.pdf) | Python-track trainees | One-page project overview | 1.0 |
| [TMS Task 01](docs/DTTP-TMS-TASK-01.pdf) | Python-track trainees | Trainee CRUD — first assignment | 1.0 |

The profile does **not** claim current headcount, clients, revenue, or market position. The handbook is the timed training path. The self-growth program is the deeper study map, not a second calendar. TMS sheets are simple trainee handouts. The main TMS assignment PDF is [`docs/DTTP-TMS-BRIEF.pdf`](docs/DTTP-TMS-BRIEF.pdf).

| Format | Profile | Handbook | Setup | Self-growth | TMS Brief |
| --- | --- | --- | --- | --- | --- |
| PDF | [docs/DESHMUKH-TECHNOLOGIES-PROFILE.pdf](docs/DESHMUKH-TECHNOLOGIES-PROFILE.pdf) | [docs/DTTP-PROGRAM-HANDBOOK.pdf](docs/DTTP-PROGRAM-HANDBOOK.pdf) | [docs/DTTP-SOFTWARE-SETUP.pdf](docs/DTTP-SOFTWARE-SETUP.pdf) | [docs/DTTP-SELF-GROWTH-PROGRAM.pdf](docs/DTTP-SELF-GROWTH-PROGRAM.pdf) | [docs/DTTP-TMS-BRIEF.pdf](docs/DTTP-TMS-BRIEF.pdf) |
| HTML | [docs/DESHMUKH-TECHNOLOGIES-PROFILE.html](docs/DESHMUKH-TECHNOLOGIES-PROFILE.html) | [docs/DTTP-PROGRAM-HANDBOOK.html](docs/DTTP-PROGRAM-HANDBOOK.html) | [docs/DTTP-SOFTWARE-SETUP.html](docs/DTTP-SOFTWARE-SETUP.html) | [docs/DTTP-SELF-GROWTH-PROGRAM.html](docs/DTTP-SELF-GROWTH-PROGRAM.html) | [docs/DTTP-TMS-BRIEF.html](docs/DTTP-TMS-BRIEF.html) |
| Markdown | [docs/DESHMUKH-TECHNOLOGIES-PROFILE.md](docs/DESHMUKH-TECHNOLOGIES-PROFILE.md) | [docs/DTTP-PROGRAM-HANDBOOK.md](docs/DTTP-PROGRAM-HANDBOOK.md) | [docs/DTTP-SOFTWARE-SETUP.md](docs/DTTP-SOFTWARE-SETUP.md) | [docs/DTTP-SELF-GROWTH-PROGRAM.md](docs/DTTP-SELF-GROWTH-PROGRAM.md) | [docs/DTTP-TMS-BRIEF.md](docs/DTTP-TMS-BRIEF.md) |

## DTTP — Trainee Program

A 90-day full-stack software development and professional development program.

**Primary outcome:** Junior Full-Stack Developer

| Track | Stack |
| --- | --- |
| Frontend | React + TypeScript |
| Backend | Java / Spring Boot **or** Python / FastAPI |
| Database | MySQL / PostgreSQL |
| Delivery | Git + GitHub + Docker + CI/CD + AWS |

## DTTP — Software Setup

Windows 10/11 onboarding: Git, GitHub SSH, JDK 17, Maven, Spring Boot, Node, React, MySQL, Postman, Docker, Flutter (mobile), verification commands, troubleshooting, and Day-1 trainee/mentor sign-off.

## DTTP — Self-Growth Program

Ten learning levels from web fundamentals to professional engineering, with timeboxes, worked examples, stop rules, writing standards, and mentor reviews. Use full-stack reference material as a knowledge map, then apply it through the Deshmukh Technologies practice stack.

## DTTP — TMS trainee documents

**[`docs/DTTP-TMS-BRIEF.pdf`](docs/DTTP-TMS-BRIEF.pdf)** is the Real-Time Project 01 brief: goal, stack, roles, ten modules, database, architecture, MVP, sprints, first user story, and GitHub workflow.

## How to rebuild a PDF

Edit the Markdown and the matching HTML, then run the builder for that document:

```bash
python3 docs/build-profile-pdf.py
python3 docs/build-handbook-pdf.py
python3 docs/build-setup-pdf.py
python3 docs/build-self-growth-pdf.py
python3 docs/build-tms-pdf.py
```

Each builder prints the HTML to A4 with Chrome, then adds headers, page numbers, bookmarks, and metadata.

## Writing standard for these documents

- Keep the navy / gold visual system and the same stack names across official documents.
- Add a worked example or filled template when a rule would otherwise stay abstract.
- Do not invent company scale, clients, or revenue.
- A level, phase, or feature is complete only when the artifact exists and can be explained.

> Learn. Build. Solve. Review. Deploy. Grow.
