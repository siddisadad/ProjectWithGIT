# DTTP — Task 01 · Trainee CRUD

**Project:** Trainee Management System (TMS) · Real-Time Project 01

Print: [`DTTP-TMS-TASK-01.pdf`](./DTTP-TMS-TASK-01.pdf)

---

## Start only with

```text
Python → FastAPI → MySQL → Trainee CRUD → Postman → GitHub
```

No React. No login. No dashboard.

---

## APIs

```text
POST   /trainees
GET    /trainees
GET    /trainees/{id}
PUT    /trainees/{id}
DELETE /trainees/{id}
```

Also: `GET /health` → `{ "status": "ok" }`

---

## MySQL

Database: `dttp_tms`

```sql
CREATE TABLE trainees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(190) NOT NULL UNIQUE,
  phone VARCHAR(20),
  status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
);
```

`DELETE` sets `status = 'INACTIVE'`. Do not remove the row.

---

## Example

`POST /trainees`

```json
{
  "full_name": "Rohan Deshmukh",
  "email": "rohan.deshmukh@example.com",
  "phone": "9876543210"
}
```

201 = created. 409 = email already exists. 404 = id not found.

Postman file: [`tms/DTTP-TMS-Task-01.postman_collection.json`](./tms/DTTP-TMS-Task-01.postman_collection.json)

---

## Deliverable

Working Trainee CRUD API connected to MySQL and uploaded to GitHub.

1. Five APIs work in Postman
2. The row is visible in MySQL
3. Code is on GitHub (no passwords)

Then stop. Wait for the mentor.

---

*Deshmukh Technologies · DTTP · TMS Task 01 · v1.0*
