# Deshmukh Technologies

**Technology · Innovation · Engineering · Growth**

> Building technology. Developing people. Solving real problems.

This repository holds the official internal document family. Each document has a Markdown source, a print-first HTML design, and a generated A4 PDF.

## Document family

| Document | Audience | Use it when | Version |
| --- | --- | --- | :---: |
| [Corporate Master Profile](docs/DESHMUKH-TECHNOLOGIES-PROFILE.pdf) | Leadership, new joiners, partners | You need identity, values, and working method | 1.2 |
| [DTTP 90-Day Handbook](docs/DTTP-PROGRAM-HANDBOOK.pdf) | Mentors and trainees | You need the timed path, project, and graduation rules | 1.5 |
| [DTTP Self-Growth Program](docs/DTTP-SELF-GROWTH-PROGRAM.pdf) | Trainees and self-directed engineers | You need the ten-level knowledge map around the 90 days | 1.6 |

The profile does **not** claim current headcount, clients, revenue, or market position. The handbook is the timed training path. The self-growth program is the deeper study map, not a second calendar.

| Format | Profile | Handbook | Self-growth |
| --- | --- | --- | --- |
| PDF | [docs/DESHMUKH-TECHNOLOGIES-PROFILE.pdf](docs/DESHMUKH-TECHNOLOGIES-PROFILE.pdf) | [docs/DTTP-PROGRAM-HANDBOOK.pdf](docs/DTTP-PROGRAM-HANDBOOK.pdf) | [docs/DTTP-SELF-GROWTH-PROGRAM.pdf](docs/DTTP-SELF-GROWTH-PROGRAM.pdf) |
| HTML | [docs/DESHMUKH-TECHNOLOGIES-PROFILE.html](docs/DESHMUKH-TECHNOLOGIES-PROFILE.html) | [docs/DTTP-PROGRAM-HANDBOOK.html](docs/DTTP-PROGRAM-HANDBOOK.html) | [docs/DTTP-SELF-GROWTH-PROGRAM.html](docs/DTTP-SELF-GROWTH-PROGRAM.html) |
| Markdown | [docs/DESHMUKH-TECHNOLOGIES-PROFILE.md](docs/DESHMUKH-TECHNOLOGIES-PROFILE.md) | [docs/DTTP-PROGRAM-HANDBOOK.md](docs/DTTP-PROGRAM-HANDBOOK.md) | [docs/DTTP-SELF-GROWTH-PROGRAM.md](docs/DTTP-SELF-GROWTH-PROGRAM.md) |

## DTTP — Trainee Program

A 90-day full-stack software development and professional development program.

**Primary outcome:** Junior Full-Stack Developer

| Track | Stack |
| --- | --- |
| Frontend | React + TypeScript |
| Backend | Java / Spring Boot **or** Python / FastAPI |
| Database | MySQL / PostgreSQL |
| Delivery | Git + GitHub + Docker + CI/CD + AWS |

## DTTP — Self-Growth Program

Ten learning levels from web fundamentals to professional engineering, with timeboxes, worked examples, stop rules, writing standards, and mentor reviews. Use full-stack reference material as a knowledge map, then apply it through the Deshmukh Technologies practice stack.

## How to rebuild a PDF

Edit the Markdown and the matching HTML, then run the builder for that document:

```bash
python3 docs/build-profile-pdf.py
python3 docs/build-handbook-pdf.py
python3 docs/build-self-growth-pdf.py
```

Each builder prints the HTML to A4 with Chrome, then adds headers, page numbers, bookmarks, and metadata.

## Writing standard for these documents

- Keep the navy / gold visual system and the same stack names across all three documents.
- Add a worked example or filled template when a rule would otherwise stay abstract.
- Do not invent company scale, clients, or revenue.
- A level, phase, or feature is complete only when the artifact exists and can be explained.

> Learn. Build. Solve. Review. Deploy. Grow.
