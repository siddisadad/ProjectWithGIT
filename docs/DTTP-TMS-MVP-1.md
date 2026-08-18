# DTTP — TMS MVP-1

**Real-Time Project 01 | First assignment**

Print: [`DTTP-TMS-MVP-1.pdf`](./DTTP-TMS-MVP-1.pdf)

Read the full brief first: [`DTTP-TMS-BRIEF.pdf`](./DTTP-TMS-BRIEF.pdf). This sheet is what you build **now**.

---

## Requirement

> As an Admin, I want to register DTTP trainees and assign them to a batch so that I can maintain a centralized trainee database.

---

## Build only

```text
Login → Admin Dashboard → Trainee Management → Batch Management
```

Do **not** build attendance, tasks, assignments, evaluation, feedback, Docker, or CI/CD yet.

---

## APIs

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

`DELETE` on a trainee **deactivates** the row. Do not remove it from MySQL.

---

## Sprints for this MVP

| Sprint | Work |
| :---: | --- |
| 1 | GitHub repo, FastAPI + React folders, MySQL, README |
| 2 | Trainee and batch models, CRUD APIs, validation, Postman |
| 3 | React: login, dashboard, trainee list, add/edit, API calls |
| 4 | JWT login, roles, protected APIs |

Stop after Sprint 4 until the mentor opens Sprint 5.

---

## Acceptance criteria

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
- Code is on GitHub
- Pull request is reviewed by the mentor

---

## Workflow

```text
Issue → Feature branch → Design → Code → Test → Commit → Push → PR → Mentor review → Fix → Merge
```

This project teaches how a real team works, not only how to write Python.

**Done:** a working TMS MVP on Python + FastAPI + MySQL + React, with GitHub code review.

---

*Deshmukh Technologies · DTTP · TMS MVP-1 · v1.0*
