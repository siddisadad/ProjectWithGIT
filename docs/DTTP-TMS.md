# DTTP — Trainee Management System

**Real-Time Project 01 | Deshmukh Technologies Trainee Program**  
**Version:** 1.0 · Complete project guide (single PDF)

Print: [`DTTP-TMS.pdf`](./DTTP-TMS.pdf)

TMS is the first real project for DTTP trainees. Build it as a genuine internal business application, not as a tutorial.

**How to use this document**

| Part | Sections | Use |
| --- | --- | --- |
| I Product | 1–3 | Read once: goal, stack, roles |
| II Ten modules | 4–13 | Full product map |
| III Architecture | 14–17 | MySQL, FastAPI, React, error JSON |
| IV Build now | 18–19 | MVP-1 APIs and Sprint 1 setup |
| V Path | 20–22 | Sprints, first user story, GitHub workflow |

Build only Part IV now. Later modules are the map, not permission to skip ahead.

---

## 1. Project goal

Build a web application to manage the complete DTTP trainee lifecycle:

```text
Registration → Batch Assignment → Training → Attendance
→ Tasks & Assignments → Evaluation → Feedback → Completion
```

---

## 2. Technology stack

**Backend:** Python · FastAPI · SQLAlchemy · MySQL · JWT · Pydantic · Pytest  
**Frontend:** React · TypeScript · HTML/CSS · REST API  
**Tools:** VS Code · Git · GitHub · Postman · MySQL Workbench · Docker · GitHub Actions

---

## 3. User roles

| Role | Can manage |
| --- | --- |
| **ADMIN** | Trainees, mentors, batches, projects, users, reports — the complete system |
| **MENTOR** | Assigned trainees: attendance, tasks, assignments, reviews, feedback, performance |
| **TRAINEE** | Own profile, attendance, tasks, assignments, submissions, feedback, progress |

---

## 4. Module 1 — Authentication

Login, logout, JWT, role-based access, password management.

Roles: `ADMIN` · `MENTOR` · `TRAINEE`

```json
POST /api/auth/login
{ "email": "admin@deshmukh.local", "password": "use-a-local-password" }
```

| Result | HTTP |
| --- | --- |
| Success + token | 200 |
| Wrong email or password | 401 |
| Protected route, no token | 401 |
| Wrong role | 403 |

Passwords are hashed. Never store plaintext. Never commit secrets.

---

## 5. Module 2 — Trainee management

Admin can add, view, edit, search, filter, activate/deactivate, assign batch, assign mentor.

| Field | Rule |
| --- | --- |
| Trainee ID | Server-assigned |
| Name | Required |
| Email | Required, unique, lowercase |
| Mobile | Optional |
| Address | Optional |
| Education | Optional |
| Joining date | Required |
| Batch | Optional until assigned |
| Mentor | Optional until assigned |
| Status | `ACTIVE` or `INACTIVE`. New rows are ACTIVE |

`DELETE /api/trainees/{id}` **deactivates**. Do not `DELETE FROM trainees`.

Search: `GET /api/trainees?q=rohan&status=ACTIVE`

---

## 6. Module 3 — Batch management

Admin creates batches such as `DTTP-2026-01`, `DTTP-2026-02`, `DTTP-2026-03`.

| Field | Rule |
| --- | --- |
| Batch name | Required, unique |
| Start date | Optional until the batch is ACTIVE |
| End date | Optional; must not be before start date |
| Mentor | Optional until assigned |
| Capacity | Optional positive integer |
| Status | `PLANNED` / `ACTIVE` / `CLOSED` |

A trainee belongs to at most one active batch. A second active assign is `409`.

---

## 7. Module 4 — Mentor management

Admin can add, update, assign, view assigned trainees, activate/deactivate a mentor.

| Field | Rule |
| --- | --- |
| Mentor ID | Server-assigned |
| Name | Required |
| Email | Required, unique, lowercase |
| Status | `ACTIVE` or `INACTIVE` |

---

## 8. Module 5 — Attendance

Mentor marks Present, Absent, Late, or Leave.

| Date | Trainee | Status |
| --- | --- | --- |
| 19-Aug | Rahul | Present |
| 19-Aug | Amit | Absent |
| 19-Aug | Sana | Present |

Same trainee + same date twice: `409`. Reports: daily, monthly, individual, percentage.

---

## 9. Module 6 — Task management

Fields: Title, Description, Priority, Deadline, Assigned To.

Status: `TODO` → `IN_PROGRESS` → `SUBMITTED` → `UNDER_REVIEW` → `COMPLETED`. Illegal jumps `409`.

---

## 10. Module 7 — Assignment and submission

```text
Mentor → Create Assignment → Trainee → Complete Work → Submit → Mentor Review → Feedback
```

Submission: description, GitHub repository, file/document, submission date, comments.

Unique pair: `(trainee_id, task_id)`. A second assign of the same task to the same trainee is `409`.

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

Mentor: technical, task, project, strengths, areas for improvement, recommendations. Trainee reads this on the dashboard.

---

## 13. Module 10 — Dashboard

**Admin:** total trainees, active trainees, total batches, total mentors, today’s attendance, pending tasks, pending reviews.  
**Mentor:** my trainees, today’s attendance, pending tasks, pending submissions, performance.  
**Trainee:** profile, attendance %, pending/completed tasks, assignments, performance, feedback.

---

## 14. Database

Tables: `users`, `roles`, `trainees`, `mentors`, `batches`, `attendance`, `tasks`, `assignments`, `submissions`, `evaluations`, `feedback`.

```text
User → Trainee | Mentor
Batch → Trainees
Mentor → Trainees
Trainee → Attendance, Tasks, Assignments, Submissions, Evaluations, Feedback
```

MVP tables (Sprint 1–2). Database name: `dttp_tms`.

```sql
CREATE DATABASE IF NOT EXISTS dttp_tms
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(190) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
);

CREATE TABLE batches (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL UNIQUE,
  start_date DATE NULL,
  end_date DATE NULL,
  capacity INT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'PLANNED'
);

CREATE TABLE trainees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(190) NOT NULL UNIQUE,
  mobile VARCHAR(20) NULL,
  address VARCHAR(255) NULL,
  education VARCHAR(120) NULL,
  joining_date DATE NOT NULL,
  batch_id INT NULL,
  mentor_id INT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_trainee_batch FOREIGN KEY (batch_id) REFERENCES batches(id)
);
```

---

## 15. Backend architecture

```text
FastAPI → Routers / Schemas / Services / Models / Database / Auth / Exceptions
                ↓
           SQLAlchemy → MySQL
```

Router does not write raw SQL. Service does not return HTTP objects. Model is the table. Schema is the JSON.

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
├── .env.example
└── README.md
```

Never commit `.env`.

---

## 16. Frontend architecture

React: Pages, Components, Layouts, Services, Hooks, Routes, Types, Utils.

Screens: Login, Dashboard, Trainees, Trainee Details, Batches, Mentors, Attendance, Tasks, Assignments, Submissions, Evaluation, Feedback, Profile.

MVP-1 screens only: Login, Admin Dashboard, Trainees (list / add / edit), Batches (list / add / edit).

---

## 17. Error shape

Use one JSON error for the whole project:

```json
{ "error": "VALIDATION_FAILED", "message": "Email is required", "field": "email" }
```

| error | HTTP | When |
| --- | --- | --- |
| VALIDATION_FAILED | 400 | Missing or invalid field |
| UNAUTHORIZED | 401 | Bad login or missing token |
| FORBIDDEN | 403 | Wrong role |
| NOT_FOUND | 404 | Unknown id |
| CONFLICT | 409 | Duplicate email, duplicate attendance, illegal status jump |

Empty list is `200 []`, not `404`. Duplicate email is `409`.

---

## 18. First MVP — build only this

```text
Login → Admin Dashboard → Trainee Management → Batch Management
```

Do **not** build attendance, tasks, assignments, evaluation, feedback, Docker, or CI/CD yet.

| Method | Path | Success | Notes |
| --- | --- | --- | --- |
| POST | `/api/auth/login` | 200 | Token in body |
| POST | `/api/trainees` | 201 | Duplicate email 409 |
| GET | `/api/trainees` | 200 | Empty list is `[]` |
| GET | `/api/trainees/{id}` | 200 | Unknown id 404 |
| PUT | `/api/trainees/{id}` | 200 | Unknown id 404 |
| DELETE | `/api/trainees/{id}` | 200 | Sets `INACTIVE` |
| POST | `/api/batches` | 201 | Duplicate name 409 |
| GET | `/api/batches` | 200 | Empty list is `[]` |
| GET | `/api/batches/{id}` | 200 | Unknown id 404 |
| PUT | `/api/batches/{id}` | 200 | Unknown id 404 |
| GET | `/api/health` | 200 | `{ "status": "ok" }` |

Create example:

```json
{
  "full_name": "Rohan Deshmukh",
  "email": "rohan.deshmukh@example.com",
  "mobile": "9876543210",
  "joining_date": "2026-08-19",
  "batch_id": 1
}
```

Sprints 1–4 finish this MVP. Stop after Sprint 4 until the mentor opens Sprint 5.

---

## 19. Sprint 1 — project setup

Do this **before** Trainee CRUD. Branch: `tms/sprint-1-setup`.

1. Create the GitHub repo (or use the one the mentor assigned). Clone with SSH.
2. Create branch `tms/sprint-1-setup`.
3. Create this layout:

```text
tms/
├── backend/
│   ├── app/main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/          Vite React + TypeScript
├── README.md
└── .gitignore
```

4. Create MySQL database `dttp_tms` and user `tms_dev` (local password, not in chat).
5. FastAPI `GET /api/health` returns `{ "status": "ok" }`.
6. React `npm run dev` loads in Chrome.
7. README: Python version, how to create the database, install, run backend, run frontend.
8. Commit, push, open a pull request.

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=tms_dev
MYSQL_PASSWORD=use-a-local-password
MYSQL_DATABASE=dttp_tms
```

Never commit `.env`.

**Done when**

- Repo is on GitHub
- `GET /api/health` works
- MySQL `dttp_tms` exists
- React app opens in Chrome
- README is enough for another trainee
- Mentor reviewed the pull request

Then start **Sprint 2** (trainee and batch CRUD). Not before.

---

## 20. Development sprints

| Sprint | Work | Start |
| :---: | --- | --- |
| 1 | Repo, FastAPI, React, MySQL, README | **Now** |
| 2 | Trainee + batch models, CRUD APIs, validation, Postman | After Sprint 1 |
| 3 | React login, dashboard, trainee list, add/edit | After Sprint 2 |
| 4 | JWT, roles, protected APIs | After Sprint 3 |
| 5 | Batch polish, mentor, assignment | After MVP-1 Pass |
| 6 | Attendance + reports | After Sprint 5 |
| 7 | Tasks, submit, review | After Sprint 6 |
| 8 | Evaluation, feedback, progress | After Sprint 7 |
| 9 | Unit, API, frontend tests | After Sprint 8 |
| 10 | GitHub Actions → Tests → Build → Docker → Deploy | After Sprint 9 |

---

## 21. First real-time requirement

> As an Admin, I want to register DTTP trainees and assign them to a batch so that I can maintain a centralized trainee database.

**Acceptance criteria**

- Admin can log in
- Admin can create a trainee
- Required fields are validated
- Email cannot be duplicated
- Admin can view and search trainees
- Admin can edit trainee details
- Admin can deactivate a trainee
- Admin can assign a batch
- Data is stored in MySQL
- APIs are tested in Postman
- Frontend works
- Code is committed through Git
- Pull request is reviewed by the mentor

---

## 22. Trainee development workflow

```text
Requirement → GitHub Issue → Feature Branch → Design → Code → Test
→ Commit → Push → Pull Request → Mentor Review → Fix → Approval → Merge
```

The first project should teach how real software teams work, not merely how to write Python.

**First milestone:** build and deploy a working TMS MVP using Python + FastAPI + MySQL + React, with GitHub-based code review.

---

*Deshmukh Technologies · DTTP · Trainee Management System · Real-Time Project 01 · Complete guide v1.0*
