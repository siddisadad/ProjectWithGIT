# DTTP — TMS Sprint 1 · Project Setup

**Real-Time Project 01 | After MVP-1**

Print: [`DTTP-TMS-SPRINT-1.pdf`](./DTTP-TMS-SPRINT-1.pdf)

Do this before Trainee CRUD. No feature APIs yet.

---

## Goal

A GitHub repository that runs FastAPI, connects to MySQL, and has a React app folder. Another trainee can follow the README.

---

## Do this

1. Create the GitHub repo (or use the one the mentor assigned). Clone with SSH.
2. Create branch `tms/sprint-1-setup`.
3. Create this layout:

```text
tms/
├── backend/
│   ├── app/main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── (Vite React + TypeScript)
├── README.md
└── .gitignore
```

4. Create MySQL database `dttp_tms` and user `tms_dev` (local password, not in chat).
5. FastAPI `GET /api/health` returns `{ "status": "ok" }`.
6. React `npm run dev` loads in Chrome.
7. README: Python version, how to create the database, install, run backend, run frontend.
8. Commit, push, open a pull request.

---

## `.env.example`

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=tms_dev
MYSQL_PASSWORD=use-a-local-password
MYSQL_DATABASE=dttp_tms
```

Never commit `.env`.

---

## Done when

- [ ] Repo is on GitHub
- [ ] `GET /api/health` works
- [ ] MySQL `dttp_tms` exists
- [ ] React app opens in Chrome
- [ ] README is enough for another trainee
- [ ] Mentor reviewed the pull request

Then start **Sprint 2** (trainee and batch CRUD). Not before.

---

*Deshmukh Technologies · DTTP · TMS Sprint 1 · v1.0*
