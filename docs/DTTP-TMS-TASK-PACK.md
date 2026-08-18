# DTTP — Trainee Management System (TMS)

### Real-Time Project 01 · Trainee Task Sheet

**Version:** 1.0  
**Audience:** DTTP trainees (Python track)  
**Stack:** Python · FastAPI · MySQL · React · Git & GitHub · Postman  

Print version: [`DTTP-TMS-TASK-PACK.pdf`](./DTTP-TMS-TASK-PACK.pdf)

---

## Purpose

Build a simple system to manage Deshmukh Technologies trainees.

---

## Technology

- Python
- FastAPI
- MySQL
- React
- Git & GitHub
- Postman

---

## Main features

| Area | What it does |
| --- | --- |
| **Login** | Admin, Mentor, Trainee |
| **Trainee management** | Add, view, edit, deactivate |
| **Batch management** | Create batch, assign trainees, assign mentor |
| **Attendance** | Present, Absent, Leave |
| **Tasks** | Create, assign, submit, review |
| **Performance** | Evaluation, feedback, progress |
| **Dashboard** | Total trainees, attendance, pending tasks, performance |

Do **not** build all of this now. Start with Task 01 only.

---

## Task 01 — start here

```text
Python
   ↓
FastAPI
   ↓
MySQL
   ↓
Trainee CRUD
   ↓
Postman testing
   ↓
GitHub
```

No React. No login. No dashboard.

---

## First APIs

```text
POST   /trainees
GET    /trainees
GET    /trainees/{id}
PUT    /trainees/{id}
DELETE /trainees/{id}
```

Also add `GET /health` → `{ "status": "ok" }`.

### Database

MySQL database: `dttp_tms`

```sql
CREATE TABLE trainees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(190) NOT NULL UNIQUE,
  phone VARCHAR(20),
  status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
);
```

`DELETE /trainees/{id}` sets `status = INACTIVE`. Do not remove the row.

### Create example

`POST /trainees`

```json
{
  "full_name": "Rohan Deshmukh",
  "email": "rohan.deshmukh@example.com",
  "phone": "9876543210"
}
```

Success: **201**. Duplicate email: **409**. Missing id: **404**.

Import Postman: [`tms/DTTP-TMS-Task-01.postman_collection.json`](./tms/DTTP-TMS-Task-01.postman_collection.json)

---

## First deliverable

Working Trainee CRUD API connected to MySQL and uploaded to GitHub.

Done when:

1. All five endpoints work in Postman.
2. You can see the row in MySQL.
3. Code is on GitHub (no passwords in Git).

Then wait for the mentor before Task 02 (Login).

---

*Deshmukh Technologies · DTTP · Real-Time Project 01 · TMS*
