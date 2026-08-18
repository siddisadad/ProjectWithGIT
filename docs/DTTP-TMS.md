# DTTP — Trainee Management System (TMS)

**Detailed Real-Time Project Specification**

| | |
| --- | --- |
| **Organization** | Deshmukh Technologies |
| **Program** | DTTP — Deshmukh Technologies Trainee Program |
| **Project** | Trainee Management System |
| **Project code** | DTTP-TMS-001 |
| **Version** | 1.0 |
| **Type** | Real-Time Full-Stack Project |
| **Backend** | Python + FastAPI |
| **Frontend** | React + TypeScript |
| **Database** | MySQL |

Print: [`DTTP-TMS.pdf`](./DTTP-TMS.pdf)

---

## 1. Project Overview

The Trainee Management System (TMS) is a real-world internal application for managing trainees throughout the DTTP program.

The system will replace manual trainee records and provide a centralized platform for:

- Trainee registration
- Batch management
- Mentor assignment
- Attendance
- Tasks
- Assignments
- Submissions
- Evaluation
- Feedback
- Progress tracking
- Reports

**Main objective**

```text
Register
   ↓
Assign Batch
   ↓
Assign Mentor
   ↓
Training
   ↓
Attendance
   ↓
Tasks
   ↓
Assignments
   ↓
Evaluation
   ↓
Feedback
   ↓
Completion
```

---

## 2. Project Goals

The project should achieve four goals.

**Business goal** — Provide Deshmukh Technologies with a simple system to manage DTTP trainees.

**Technical goal** — Teach trainees how to develop a complete full-stack application.

**Professional goal** — Teach the real software-development lifecycle.

**Learning goal** — Trainees should understand:

```text
Requirement → Design → Development → Testing
→ Git → Code Review → QA → Deployment
```

---

## 3. User Roles

### 3.1 Admin

Admin has complete access.

Admin can: login, create users, add trainees, edit trainees, deactivate trainees, create batches, assign mentors, assign trainees, view attendance, view tasks, view evaluations, view reports.

### 3.2 Mentor

Mentor manages assigned trainees.

Mentor can: login, view assigned trainees, mark attendance, create tasks, assign tasks, review submissions, evaluate trainees, give feedback, view trainee progress.

### 3.3 Trainee

Trainees have limited access.

Trainee can: login, view profile, view batch, view mentor, view attendance, view tasks, submit assignments, view feedback, view evaluation, track progress.

---

## 4. Main Modules

```text
TMS
│
├── Authentication
├── User Management
├── Trainee Management
├── Mentor Management
├── Batch Management
├── Attendance
├── Task Management
├── Assignment Management
├── Submission Management
├── Evaluation
├── Feedback
├── Dashboard
└── Reports
```

---

## 5. Module 1 — Authentication

**Features:** login, logout, password hashing, JWT authentication, role-based authorization, protected APIs.

**Login flow**

```text
Username / Email → Password → Authentication → JWT Token → Dashboard
```

**Roles:** `ADMIN` · `MENTOR` · `TRAINEE`

---

## 6. Module 2 — Trainee Management

This is the first major module.

**Trainee information:** Trainee ID, Full Name, Email, Mobile, Date of Birth, Gender, Education, Address, Joining Date, Batch, Mentor, Status.

**Status:** `ACTIVE` · `INACTIVE` · `COMPLETED` · `DROPPED`

**Features**

- **Add trainee** — Admin enters trainee details.
- **View trainees** — Name, ID, Batch, Mentor, Status.
- **Search** — Name, Trainee ID, Email, Mobile.
- **Filter** — Batch, Mentor, Status.
- **Edit** — Admin can update trainee information.
- **Deactivate** — Do not immediately delete important records. Prefer `ACTIVE` → `INACTIVE`.

---

## 7. Module 3 — Batch Management

A batch represents a group of trainees.

**Batch information:** Batch ID, Batch Name, Start Date, End Date, Mentor, Capacity, Status.

**Examples:** `DTTP-2026-01` · `DTTP-2026-02` · `DTTP-2026-03`

**Features:** create batch, edit batch, view batch, assign mentor, add trainees, remove trainee, view batch members.

---

## 8. Module 4 — Mentor Management

**Mentor information:** Mentor ID, Name, Email, Mobile, Department, Specialization, Status.

**Features:** add mentor, edit mentor, view mentor, assign trainees, view assigned trainees, activate/deactivate mentor.

---

## 9. Module 5 — Attendance

Mentors record trainee attendance.

**Attendance status:** `PRESENT` · `ABSENT` · `LATE` · `LEAVE`

**Attendance record:** Date, Trainee, Batch, Status, Marked By, Remarks.

**Features:** mark attendance, edit attendance, view daily attendance, view monthly attendance, view individual attendance, calculate attendance percentage.

**Example**

```text
Total Working Days = 25
Present = 23
Attendance = 92%
```

---

## 10. Module 6 — Task Management

Mentors create tasks for trainees.

**Task information:** Task ID, Title, Description, Assigned To, Created By, Priority, Deadline, Status.

**Priority:** `LOW` · `MEDIUM` · `HIGH`

**Status:** `TODO` · `IN_PROGRESS` · `SUBMITTED` · `UNDER_REVIEW` · `COMPLETED`

**Task workflow**

```text
Mentor → Create Task → Trainee → Start Task → Submit
→ Mentor Review → Feedback → Completed
```

---

## 11. Module 7 — Assignment Management

Assignments are larger learning activities.

**Example:** Build a FastAPI CRUD API for trainee management.

**Assignment information:** Assignment ID, Title, Description, Instructions, Start Date, Deadline, Assigned Batch, Created By, Status.

---

## 12. Module 8 — Submission

Trainee submits completed work.

**Submission can contain:** description, GitHub repository, branch name, pull request, file/document, comments, submission date.

**Submission workflow**

```text
Assignment → Trainee Work → Submission → Mentor Review
→ Approved / Changes Required
```

---

## 13. Module 9 — Evaluation

Mentors evaluate trainee performance.

| Category | Score |
| --- | --- |
| Technical Skills | /10 |
| Problem Solving | /10 |
| Coding Quality | /10 |
| Git/GitHub | /10 |
| Communication | /10 |
| Teamwork | /10 |
| Professionalism | /10 |

**Evaluation result:** Total Score, Percentage, Grade, Mentor Remarks.

---

## 14. Module 10 — Feedback

Mentors can provide feedback after: task, assignment, project, weekly review, monthly review.

**Feedback:** Strengths, Areas for Improvement, Recommendations, General Comments.

---

## 15. Module 11 — Dashboard

**Admin dashboard:** Total Trainees, Active Trainees, Total Mentors, Active Batches, Today's Attendance, Pending Tasks, Pending Reviews.

**Mentor dashboard:** My Trainees, Today's Attendance, Pending Tasks, Pending Submissions, Upcoming Deadlines, Recent Feedback.

**Trainee dashboard:** My Profile, My Batch, My Mentor, Attendance %, Pending Tasks, Completed Tasks, Assignments, Performance, Feedback.

---

## 16. Module 12 — Reports

**Trainee report:** Trainee, Batch, Mentor, Status, Joining Date.

**Attendance report:** Trainee, Total Days, Present, Absent, Leave, Percentage.

**Task report:** Task, Trainee, Deadline, Status.

**Performance report:** Trainee, Score, Grade, Feedback.

---

## 17. Database Design

**Initial tables:** `users` · `roles` · `trainees` · `mentors` · `batches` · `attendance` · `tasks` · `assignments` · `submissions` · `evaluations` · `feedback`

**Basic relationship**

```text
USER
 ├── ADMIN
 ├── MENTOR
 └── TRAINEE
BATCH
 └── TRAINEES
MENTOR
 └── TRAINEES
TRAINEE
 ├── ATTENDANCE
 ├── TASKS
 ├── ASSIGNMENTS
 ├── SUBMISSIONS
 ├── EVALUATIONS
 └── FEEDBACK
```

---

## 18. Backend Architecture

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
├── .env          ← never commit secrets
└── README.md
```

**Request flow**

```text
React → FastAPI Router → Validation → Service → SQLAlchemy → MySQL → Response
```

---

## 19. Frontend Architecture

```text
frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── layouts/
│   ├── services/
│   ├── hooks/
│   ├── routes/
│   ├── types/
│   └── utils/
├── public/
└── package.json
```

---

## 20. Important APIs

**Authentication**

```text
POST /api/auth/login
```

**Trainees**

```text
POST   /api/trainees
GET    /api/trainees
GET    /api/trainees/{id}
PUT    /api/trainees/{id}
DELETE /api/trainees/{id}
```

**Batches**

```text
POST /api/batches
GET  /api/batches
GET  /api/batches/{id}
PUT  /api/batches/{id}
```

**Attendance**

```text
POST /api/attendance
GET  /api/attendance
```

**Tasks**

```text
POST /api/tasks
GET  /api/tasks
PUT  /api/tasks/{id}
```

**Assignments**

```text
POST /api/assignments
GET  /api/assignments
POST /api/assignments/{id}/submit
```

**Evaluation**

```text
POST /api/evaluations
GET  /api/evaluations/{trainee_id}
```

`DELETE /api/trainees/{id}` deactivates the row (`ACTIVE` → `INACTIVE`). Do not remove important records from MySQL.

---

## 21. MVP — First Release

Do not build every feature immediately.

**MVP Version 1**

```text
Login → Dashboard → Trainees → Batches → Mentors
```

**Then Version 2:** Attendance, Tasks, Assignments.

**Then Version 3:** Evaluation, Feedback, Reports.

---

## 22. Development Plan

**Week 1 — Foundation:** Python, FastAPI, Git, GitHub, MySQL, project setup.

**Week 2 — Backend:** Database, SQLAlchemy, Trainee CRUD, Batch CRUD, Mentor CRUD, Postman.

**Week 3 — Frontend:** React, Login, Dashboard, Trainee screens, API integration.

**Week 4 — MVP completion:** Authentication, Roles, Validation, Testing, Bug fixing, QA review.

---

## 23. Month-End QA

At the end of one month, QA checks:

**Functional:** login, trainee CRUD, batch CRUD, mentor management, attendance, tasks, assignments.

**API:** status codes, validation, authentication, authorization, error handling.

**UI:** forms, navigation, responsive design, error messages, loading states.

**Database:** data creation, data updates, relationships, duplicate records, constraints.

---

## 24. GitHub Workflow

Every trainee follows:

```text
Requirement → GitHub Issue → Feature Branch → Development → Testing
→ Commit → Push → Pull Request → Mentor Review → Fix → Approval → Merge
```

Example branch: `feature/trainee-crud`

Example commit: `feat: add trainee CRUD APIs`

---

## 25. QA Workflow

```text
Developer → Developer Testing → Pull Request → Mentor Review → QA Testing
→ Bug Found?
     / \
   Yes  No
    ↓    ↓
   Fix  Approve
    ↓    ↓
 Retest  Release
```

---

## 26. Bug Classification

| Severity | Meaning |
| --- | --- |
| **Critical** | System cannot operate. |
| **High** | Major feature does not work. |
| **Medium** | Feature works incorrectly but a workaround exists. |
| **Low** | Minor UI or usability issue. |

---

## 27. Docker

After local development is stable:

```text
React Container → FastAPI Container → MySQL Container
```

Use `Dockerfile` and `docker-compose.yml`.

Basic command: `docker compose up`

---

## 28. CI/CD

Later introduce:

```text
GitHub → GitHub Actions → Lint → Tests → Build → Docker Image → Deployment
```

---

## 29. Security Requirements

Trainees must:

- Never commit passwords.
- Never commit `.env`.
- Never commit API keys.
- Never share private SSH keys.
- Hash passwords.
- Protect private APIs.
- Validate user input.
- Use role-based authorization.
- Use environment variables for secrets.

---

## 30. Definition of Done

A feature is DONE only when:

- Code is complete.
- Validation is implemented.
- API is tested.
- UI is tested where applicable.
- No critical errors remain.
- Git commit is created.
- Pull Request is submitted.
- Mentor review is completed.
- QA testing passes.
- Documentation is updated.

---

## 31. Final Project Flow

```text
                    TMS
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
     Admin         Mentor       Trainee
       │             │             │
       └─────────────┼─────────────┘
                     ↓
              Trainee Records
                     ↓
                 Attendance
                     ↓
                   Tasks
                     ↓
                Assignments
                     ↓
                Submissions
                     ↓
                Evaluation
                     ↓
                  Feedback
                     ↓
                 Progress
                     ↓
                  Reports
```

---

## 32. Final DTTP Outcome

At completion, trainees should have experience with:

```text
Python → FastAPI → REST API → MySQL → React → GitHub → Testing → QA → Docker → CI/CD
```

More importantly, they should be able to work like a real development team:

```text
Understand → Design → Develop → Test → Review → Fix → Deliver
```

This TMS should be treated as the first production-style DTTP training project, with the scope expanded gradually rather than trying to build the entire system at once.

---

*Deshmukh Technologies · DTTP · DTTP-TMS-001 · Detailed Real-Time Project Specification · v1.0*
