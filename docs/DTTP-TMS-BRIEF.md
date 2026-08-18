# DTTP — Trainee Management System (TMS)

**Real-Time Project 01 | Deshmukh Technologies Trainee Program**

Print: [`DTTP-TMS-BRIEF.pdf`](./DTTP-TMS-BRIEF.pdf)

The Trainee Management System (TMS) is the first real project for DTTP trainees. Build it as a genuine internal business application, not as a tutorial project.

---

## 1. Project goal

Build a web application to manage the complete DTTP trainee lifecycle:

```text
Registration
    ↓
Batch Assignment
    ↓
Training
    ↓
Attendance
    ↓
Tasks & Assignments
    ↓
Evaluation
    ↓
Feedback
    ↓
Completion
```

---

## 2. Technology stack

**Backend:** Python, FastAPI, SQLAlchemy, MySQL, JWT Authentication, Pydantic, Pytest

**Frontend:** React, TypeScript, HTML/CSS, REST API

**Tools:** VS Code, Git, GitHub, Postman, MySQL Workbench, Docker, GitHub Actions

---

## 3. User roles

**Admin** — complete system: trainees, mentors, batches, projects, users, reports.

**Mentor** — assigned trainees: attendance, tasks, assignments, reviews, feedback, performance.

**Trainee** — own activities: profile, attendance, tasks, assignments, submissions, feedback, progress.

---

## 4. Module 1 — Authentication

Login, logout, JWT, role-based access, password management.

Roles: `ADMIN` · `MENTOR` · `TRAINEE`

---

## 5. Module 2 — Trainee management

Admin can: add, view, edit, search, filter, activate/deactivate, assign batch, assign mentor.

Trainee fields: Trainee ID, Name, Email, Mobile, Address, Education, Joining Date, Batch, Mentor, Status.

---

## 6. Module 3 — Batch management

Admin creates and manages batches, for example `DTTP-2026-01`, `DTTP-2026-02`, `DTTP-2026-03`.

Batch fields: Batch Name, Start Date, End Date, Mentor, Capacity, Status.

---

## 7. Module 4 — Mentor management

Admin can: add mentor, update mentor, assign mentor, view assigned trainees, activate/deactivate mentor.

---

## 8. Module 5 — Attendance

Mentor marks: Present, Absent, Late, Leave.

Example:

| Date | Trainee | Status |
| --- | --- | --- |
| 19-Aug | Rahul | Present |
| 19-Aug | Amit | Absent |
| 19-Aug | Sana | Present |

Reports: daily, monthly, individual, attendance percentage.

---

## 9. Module 6 — Task management

Mentor creates tasks: Title, Description, Priority, Deadline, Assigned To.

Status: `TODO` · `IN_PROGRESS` · `SUBMITTED` · `UNDER_REVIEW` · `COMPLETED`

---

## 10. Module 7 — Assignment and submission

```text
Mentor → Create Assignment → Trainee → Complete Work → Submit → Mentor Review → Feedback
```

Submission: description, GitHub repository, file/document, submission date, comments.

---

## 11. Module 8 — Evaluation

| Skill | Score |
| --- | --- |
| Python | 8/10 |
| FastAPI | 7/10 |
| MySQL | 8/10 |
| React | 7/10 |
| Git | 9/10 |
| Problem Solving | 8/10 |
| Communication | 8/10 |

---

## 12. Module 9 — Feedback

Mentor provides: technical, task, project, strengths, areas for improvement, recommendations.

Trainee views feedback from their dashboard.

---

## 13. Module 10 — Dashboard

**Admin:** total trainees, active trainees, total batches, total mentors, today’s attendance, pending tasks, pending reviews.

**Mentor:** my trainees, today’s attendance, pending tasks, pending submissions, performance.

**Trainee:** my profile, attendance %, pending tasks, completed tasks, assignments, performance, feedback.

---

## 14. Database design

Tables: `users`, `roles`, `trainees`, `mentors`, `batches`, `attendance`, `tasks`, `assignments`, `submissions`, `evaluations`, `feedback`.

```text
User
 ├── Trainee
 └── Mentor
Batch → Trainees
Mentor → Trainees
Trainee → Attendance, Tasks, Assignments, Submissions, Evaluations, Feedback
```

---

## 15. Backend architecture

```text
FastAPI → Routers / Schemas / Services / Models / Database / Auth / Exceptions
                ↓
           SQLAlchemy
                ↓
             MySQL
```

```text
backend/
├── app/
│   ├── main.py
│   ├── config/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   ├── auth/
│   └── exceptions/
├── tests/
├── requirements.txt
├── .env
└── README.md
```

Do not commit real `.env` secrets.

---

## 16. Frontend architecture

React: Pages, Components, Layouts, Services, Hooks, Routes, Types, Utils.

Screens: Login, Dashboard, Trainees, Trainee Details, Batches, Mentors, Attendance, Tasks, Assignments, Submissions, Evaluation, Feedback, Profile.

---

## 17. First MVP

Do not build all modules at once.

```text
Login → Admin Dashboard → Trainee Management → Batch Management
```

```text
POST   /api/auth/login
POST   /api/trainees
GET    /api/trainees
GET    /api/trainees/{id}
PUT    /api/trainees/{id}
DELETE /api/trainees/{id}
POST   /api/batches
GET    /api/batches
GET    /api/batches/{id}
PUT    /api/batches/{id}
```

---

## 18. Development sprints

| Sprint | Work |
| :---: | --- |
| 1 | GitHub repo, backend, frontend, MySQL, structure, README |
| 2 | Trainee model, CRUD APIs, validation, Postman |
| 3 | React: login, dashboard, trainee list, add/edit, API integration |
| 4 | Login, JWT, roles, protected APIs |
| 5 | Batch, mentor, assignment |
| 6 | Mark attendance, reports, percentage |
| 7 | Tasks, assign, submission, review |
| 8 | Evaluation, feedback, progress |
| 9 | Unit, API, frontend tests, bug fixing |
| 10 | GitHub → Actions → Tests → Build → Docker → Deployment |

---

## 19. First real-time requirement

> As an Admin, I want to register DTTP trainees and assign them to a batch so that I can maintain a centralized trainee database.

**Acceptance criteria**

- Admin can log in
- Admin can create a trainee
- Required fields are validated
- Email cannot be duplicated
- Admin can view trainees
- Admin can search trainees
- Admin can edit trainee details
- Admin can deactivate a trainee
- Admin can assign a batch
- Data is stored in MySQL
- APIs are tested
- Frontend works
- Code is committed through Git
- Pull request is reviewed by mentor

---

## 20. Trainee development workflow

```text
Requirement → GitHub Issue → Feature Branch → Design → Code → Test
    → Commit → Push → Pull Request → Mentor Review → Fix → Approval → Merge
```

The first project should teach how real software teams work, not merely how to write Python.

**First milestone:** build and deploy a working Trainee Management System MVP using Python + FastAPI + MySQL + React, with GitHub-based code review.

---

*Deshmukh Technologies · DTTP · TMS Real-Time Project 01 · v1.0*
