# DTTP Self-Growth Program

### Deshmukh Technologies Full-Stack Developer Self-Growth Roadmap

Ten detailed learning levels that turn full-stack reference material into a practical Deshmukh Technologies growth path.

A designed, print-ready version is available in [`DTTP-SELF-GROWTH-PROGRAM.pdf`](./DTTP-SELF-GROWTH-PROGRAM.pdf) and [`DTTP-SELF-GROWTH-PROGRAM.html`](./DTTP-SELF-GROWTH-PROGRAM.html).

The 90-day program handbook remains in [`DTTP-PROGRAM-HANDBOOK.pdf`](./DTTP-PROGRAM-HANDBOOK.pdf).

---

## How to use this program

Full-stack reference material provides a strong foundation. It is **not** the entire DTTP curriculum.

Use it as the **Full-Stack Knowledge Reference**, then combine it with:

**Java / Spring Boot or Python / FastAPI + React / TypeScript + SQL + GitHub + Docker + CI/CD + AWS + real Deshmukh Technologies projects.**

Do not ask trainees to study the reference as one large syllabus. Organize growth into ten levels. Complete one level before treating the next as the main focus.

### Relationship to the 90-day handbook

| Document | Role |
| --- | --- |
| 90-Day DTTP Handbook | Timed training path, project, assessment, and graduation |
| Self-Growth Program | Deeper knowledge map for study before, during, and after the 90 days |
| Full-Stack Reference | Topic encyclopedia — not a replacement for practice |

### Study method

For every topic:

1. Read the concept.
2. Explain it in your own words.
3. Build a small example.
4. Break it, then debug it.
5. Commit the work.
6. Ask a mentor to review it.

### Weekly habit

- 20% theory
- 30% exercises
- 40% project work
- 10% review and notes

> A trainee completes this program when they can independently build, test, debug, explain, document, and maintain a full-stack application.

### Mapping to the 90-day handbook

| Self-growth level | Typical 90-day phase |
| :---: | --- |
| 1–2 | Days 1–25 · orientation, programming, web foundation |
| 3–4 | Days 26–35 · React and API thinking |
| 5–6 | Days 36–55 · backend specialization and database |
| 7 | Throughout the project, made explicit in design reviews |
| 8 | Days 66–78 · security, testing, debugging |
| 9 | Days 79–86 · Docker, CI/CD, AWS |
| 10 | Entire program, assessed at the end |

A trainee may be ahead or behind the calendar. The level checklist matters more than the day number.

### Suggested timebox

These are focus windows, not deadlines. A trainee who finishes early should deepen the same level with a harder artifact, not skip ahead casually.

| Level | Suggested focus | Minimum artifact |
| :---: | --- | --- |
| 1 | 3–5 days | Request-path diagram + static page |
| 2 | 7–10 days | Responsive page, form, DOM app, fetch demo |
| 3 | 8–12 days | Typed React app with layout, routes, and one form |
| 4 | 4–6 days | API contract + Network notes + Postman collection |
| 5 | 10–14 days | Authenticated CRUD API on one track |
| 6 | 7–10 days | Schema, seed data, join report, transaction example |
| 7 | 3–5 days | Layered architecture diagram and module map |
| 8 | 7–10 days | Tests, one security write-up, one measured improvement |
| 9 | 5–8 days | Compose file, CI workflow, deploy notes |
| 10 | Continuous | Stories, reviews, daily reports, demo |

### Daily notebook

Every study day, write:

1. Topic studied
2. What I can now explain
3. What I built
4. What broke
5. What I still cannot explain
6. Commit hash or PR link
7. Tomorrow’s one objective

If there is no notebook entry and no Git artifact, the day does not count as self-growth.

### Commit standard

```text
level-03: add protected employee list route
```

A useful commit is small, named after the level, and reviewable. Do not store a week of mixed work in one commit.

### Writing standard

Notes are part of the work. Write so a mentor can review the day without a meeting.

- Be specific: name the file, endpoint, status code, or error.
- Prefer evidence over adjectives. “409 on duplicate email” is useful. “Improved backend” is not.
- Record what is still unclear. Hidden confusion becomes a skipped level.
- Keep one idea per note. Long essays are harder to review than a short table.

### Sample notebook entry

| Field | Example |
| --- | --- |
| Topic studied | Protected routes and service layer |
| What I can now explain | Why employee list state does not belong inside JSX |
| What I built | `/employees` route, `employeeService.ts`, empty state |
| What broke | Redirect loop when the token was an empty string |
| What I still cannot explain | When Context is better than lifting state |
| Commit / PR | `level-03: add protected employee list route` |
| Tomorrow | Create-employee form with typed validation |

### Documentation artifact by level

| Level | Written artifact the mentor reviews |
| :---: | --- |
| 1 | Request-path diagram and URL parts |
| 2 | Accessibility and fetch-error notes |
| 3 | Component map and where state lives |
| 4 | API contract and Network-tab notes |
| 5 | Endpoint notes for each implemented route |
| 6 | Schema, seed notes, and the SQL behind one ORM call |
| 7 | Architecture diagram and three “not yet services” reasons |
| 8 | Test list, security note, before/after measurement |
| 9 | Compose runbook and CI failure explanation |
| 10 | User story, PR walkthrough notes, daily reports |

### Feature note and decision note

Use a **feature note** when behavior changes:

```text
Feature: Create employee
Done when: ADMIN/HR can create; EMPLOYEE cannot; duplicate email is 409
Tests: service duplicate-email; API 401/403/409
Docs: README run steps unchanged; api.md updated
```

Use a **decision note** when the choice is not obvious:

```text
Decision: keep leave in the same service as employees
Why: one team, one database, one deployable
Not chosen: leave microservice — no independent scale or ownership yet
Revisit when: a second team owns leave or the data must be isolated
```

---

## Official progression

```text
LEVEL 1  Web Fundamentals
   ↓
LEVEL 2  Frontend Fundamentals
   ↓
LEVEL 3  React + TypeScript
   ↓
LEVEL 4  HTTP + REST + Web APIs
   ↓
LEVEL 5  Java / Python Backend
   ↓
LEVEL 6  Databases
   ↓
LEVEL 7  Architecture
   ↓
LEVEL 8  Testing + Security + Performance
   ↓
LEVEL 9  Git + Docker + CI/CD + Cloud
   ↓
LEVEL 10 Agile + Professional Engineering
   ↓
SELF-DIRECTED FULL-STACK DEVELOPER
```

| Level | Focus | Outcome |
| :---: | --- | --- |
| 1 | Web Fundamentals | Can explain how a browser request becomes a response |
| 2 | Frontend Engineering | Can build accessible pages and DOM interactions |
| 3 | React + TypeScript | Can build a structured SPA with routing and forms |
| 4 | HTTP + REST + Web APIs | Can reason about frontend–backend traffic |
| 5 | Java or Python backend | Can implement a secure REST API |
| 6 | Databases | Can design and query SQL independently |
| 7 | Architecture | Can choose structure for a reason |
| 8 | Testing, security, performance | Can protect, verify, and measure software |
| 9 | Git, Docker, CI/CD, cloud | Can deliver a running system |
| 10 | Agile + professional engineering | Can work as a team engineer |

---

## Level 1 — Web Fundamentals

**Purpose:** give the trainee a mental model of the web before frameworks.

### Study

- Client and server roles
- Browser, DNS, domain, IP address, port
- URL structure: protocol, host, path, query, fragment
- HTTP as request/response, not as “magic”
- Static page vs dynamic application
- HTML as structure, CSS as presentation, JavaScript as behavior
- What server-side logic is for
- What “full-stack” actually means
- Editor, browser DevTools, terminal, package manager, Git

### Must be able to explain

- What happens after a user types a URL
- Difference between frontend and backend
- Difference between a file server and an application server
- Why JavaScript runs in the browser and Java/Python run on the server

### Practice

- Draw the request path: browser → DNS → server → response
- Build a three-file page: `index.html`, `styles.css`, `app.js`
- Inspect a live page in DevTools: Elements, Network, Console
- Host a static folder locally and reload after edits

### DTTP application

Do not start React, Spring Boot, or FastAPI until this level is solid.

### Level complete

- [ ] Can explain client, server, URL, DNS, and HTTP
- [ ] Can build and style a simple page
- [ ] Can use DevTools to inspect HTML, CSS, and network calls
- [ ] Can describe what a full-stack application contains

> A trainee who cannot explain how a browser request reaches a server is not ready for React or Spring Boot.

### Worked example

Explain this URL in writing:

`https://app.deshmukh.local:5173/employees?status=active#list`

Identify protocol, host, port, path, query, and fragment. Then open any website, find one document request and one API request in the Network tab, and write the difference.

### Stop rule

Do not start Level 2 until the trainee can narrate a request without using the words “it just loads.”

---

## Level 2 — Frontend Engineering

**Purpose:** make the trainee fluent in the browser before React abstractions.

### Structure and style

- Semantic HTML: headings, lists, tables, landmarks
- Forms: input types, labels, validation attributes, submit behavior
- CSS cascade, selectors, specificity, inheritance
- Box model, margin, padding, border
- Flexbox for one-dimensional layout
- CSS Grid for two-dimensional layout
- Responsive units and media queries

### Behavior

- Variables, types, scope, equality
- Functions, parameters, return values
- Objects, arrays, and common methods
- Conditionals, loops, and errors
- `try / catch` and useful error messages
- DOM selection, events, create/update/remove nodes
- Fetch API: GET/POST, JSON, error states, loading states
- Common Web APIs: storage, timers, history
- Accessibility: labels, contrast, keyboard, alt text, focus

### Must be able to explain

- Why semantic HTML matters
- Why a CSS rule did or did not apply
- How an event travels through the DOM
- How `fetch` differs from a page reload

### Practice

- Build a responsive landing page with Flexbox and Grid
- Build a form with client-side validation
- Build a todo list using only DOM APIs
- Call a public JSON API and render the result
- Make the page usable with keyboard only

### DTTP application

This level is the foundation for React forms, validation, loading states, and accessible UI in the Employee Management System.

### Level complete

- [ ] Can layout a page with Flexbox and Grid
- [ ] Can handle form input and validation
- [ ] Can update the DOM from JavaScript
- [ ] Can fetch JSON and render success/error/loading states
- [ ] Can name at least three accessibility checks

### Worked example

Build a “New Employee” HTML form with name, email, department, and joining date. Validate empty fields before submit. After submit, append a row to a table using the DOM. Then fetch a public user list and render names. Make the form usable with Tab and Enter only.

### Stop rule

Do not start React until the trainee can do this without a framework.

---

## Level 3 — React & Modern Frontend

**Purpose:** build maintainable UI with React and TypeScript.

The common DTTP frontend path is **React + TypeScript**.

### Study

- Components as functions
- Props vs state
- Rendering and re-rendering
- Lifecycle through effects
- Controlled forms and validation
- Component hierarchy and composition
- Lifting state vs Context API
- Routing and protected routes
- Responsive design in a component tree
- SPA architecture: pages, layouts, services, hooks, types
- Error boundaries and empty states
- TypeScript types for props, API responses, and form values

### Recommended structure

```text
src/
├── components/
├── pages/
├── layouts/
├── services/
├── hooks/
├── types/
├── utils/
├── routes/
└── assets/
```

### Must be able to explain

- When state belongs in a component, a parent, or context
- Why a component re-rendered
- How a route maps to a page
- How the UI calls a backend service without mixing API code into JSX

### Practice

- Build a multi-page React app with a shared layout
- Implement login and a protected route
- Build a form that posts JSON to an API
- Show loading, empty, success, and error states
- Extract a reusable table or card component

### DTTP application

Use this level to start the Employee Management System frontend: dashboard, employee list, forms, and profile.

### Level complete

- [ ] Can create typed React components
- [ ] Can manage local and shared state
- [ ] Can implement routing and a protected page
- [ ] Can integrate an API through a service layer
- [ ] Can keep UI responsive and readable

### Worked example

Build:

- `/login`
- `/dashboard` (protected)
- `/employees` (protected list + create form)

Put API calls in `services/employeeService.ts`. Types go in `types/employee.ts`. If the token is missing, redirect to login. Show an empty state when the list is `[]`.

### Stop rule

Do not start backend specialization until the trainee can explain props, state, effects, and a service layer.

---

## Level 4 — Web Communication & APIs

**Purpose:** teach what actually happens between frontend and backend.

### HTTP

- Request line, headers, body
- Response status, headers, body
- Methods: GET, POST, PUT, PATCH, DELETE
- Idempotency and safe methods
- Status families: 2xx, 3xx, 4xx, 5xx
- Common codes: 200, 201, 204, 400, 401, 403, 404, 409, 422, 500
- Cookies, sessions, and `Set-Cookie`
- Content-Type and Accept
- CORS preflight at a high level

### Realtime

- Short polling and long polling
- Server-Sent Events
- WebSockets
- When each model is the right choice

### API styles

- JSON as a data contract
- REST resources, nouns, and status codes
- Pagination, filtering, and error payloads
- GraphQL as a query API, not a replacement for all REST
- OpenAPI / Swagger as documentation

### Must be able to explain

- Why GET should not change server state
- Difference between 401 and 403
- Why a browser blocks a cross-origin request
- Difference between REST and GraphQL

### Practice

- Inspect every request in DevTools Network
- Call the same API with browser, Postman, and `fetch`
- Design the Employee Management endpoints on paper
- Write positive and negative API test cases

### DTTP application

Both backend tracks implement the same business API:

```text
POST   /api/auth/login
GET    /api/employees
POST   /api/employees
GET    /api/employees/{id}
PUT    /api/employees/{id}
DELETE /api/employees/{id}
GET    /api/departments
POST   /api/departments
GET    /api/attendance
POST   /api/attendance
GET    /api/leaves
POST   /api/leaves
PUT    /api/leaves/{id}/approve
```

### Level complete

- [ ] Can read a network trace and explain each part
- [ ] Can choose the correct HTTP method and status code
- [ ] Can describe REST resource design
- [ ] Can say when polling, SSE, or WebSockets is appropriate

### Worked example

For `POST /api/employees`, write the expected:

- request JSON
- 201 response JSON
- 400/422 validation response
- 401 response when the token is missing
- 403 response when an EMPLOYEE tries to create another employee

Then capture the same calls in Postman.

### Error payload standard

```json
{
  "error": "VALIDATION_FAILED",
  "message": "Email is required",
  "field": "email"
}
```

Use one error shape across Java and Python tracks.

### Stop rule

Do not start backend specialization until the trainee can choose method, status, and error shape for create, read, update, delete, unauthorized, and forbidden without guessing.

---

## Level 5 — Backend Development

**Purpose:** implement server-side business logic on one DTTP track.

Specialize the reference’s server-side concepts. Trainees are not required to learn every backend language.

### Shared backend skills

- Request validation
- DTO / request and response models
- Service layer vs controller / router
- Repository / data access
- Error handling and logging
- Authentication and authorization
- Environment configuration
- Layered folder structure

### Java track

- Java language and OOP
- Spring Boot application structure
- REST controllers
- Dependency injection
- DTO, entity, validation
- Spring Data JPA and Hibernate
- Exception handling
- Spring Security and JWT
- Testing with JUnit, Mockito, and Spring tests

```text
Controller → Service → Repository → JPA / Hibernate → Database
```

### Python track

- Python language, typing, modules
- FastAPI routes
- Pydantic models
- Dependency injection
- SQLAlchemy
- Middleware and exceptions
- Authentication
- Async where it is useful
- Testing with Pytest

```text
Router → Service → Repository → SQLAlchemy → Database
```

### Must be able to explain

- Why business rules do not belong only in the controller
- How a request becomes a database write
- How validation failures become 400/422 responses
- How a role is checked before a leave is approved

### Practice

- Implement login
- Implement employee CRUD
- Implement department list/create
- Implement attendance create/list
- Implement leave apply/approve
- Return consistent error JSON
- Write at least one unit test per service

### DTTP application

Both tracks satisfy the same Employee Management business requirements.

### Level complete

- [ ] Can implement a validated REST endpoint
- [ ] Can separate controller, service, and repository
- [ ] Can persist and read data through the ORM
- [ ] Can protect at least one endpoint with authentication
- [ ] Can explain a request through every backend layer

### Worked example

Implement `POST /api/employees` on the chosen track:

1. Controller / router accepts a DTO and returns HTTP status only.
2. Service rejects a missing name or email, rejects a duplicate email, and assigns a valid department.
3. Repository persists the employee.
4. Missing email returns `400` / `422` with the standard error payload.
5. Duplicate email returns `409`.
6. Missing token returns `401`.
7. An `EMPLOYEE` caller returns `403`.
8. A successful create returns `201` and the new employee JSON.
9. One unit test proves the service rejects a duplicate email without talking to the controller.

Then implement `GET`, `PUT`, and `DELETE` with the same layering.

### Stop rule

If the trainee cannot walk one request through controller → service → repository → database, stay here. Fat controllers do not complete this level.

---

## Level 6 — Database Engineering

**Purpose:** make SQL a first-class skill.

This is a major self-growth area. **SQL + MySQL / PostgreSQL is mandatory.** NoSQL is introduced later.

### Relational — mandatory

- Tables, columns, types
- Primary keys, foreign keys, unique constraints
- One-to-one, one-to-many, many-to-many
- `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`
- Indexes and when they help
- Transactions: begin, commit, rollback
- Isolation at a practical level
- Normalization vs practical denormalization
- Query plans at a basic level
- ORM mapping: entity, relationship, lazy/eager loading

### Non-relational — later

- Key-value stores
- Document databases
- Graph databases
- Column-oriented databases
- When SQL is still the better default

### Must be able to explain

- Why a foreign key exists
- Difference between inner and left join
- What a transaction protects
- Why an N+1 query is expensive
- Why ORM is not a substitute for SQL

### Practice

- Design tables for employees, departments, attendance, and leave
- Write joins that list employees with department names
- Write a report query: leave count by department
- Add an index and justify it
- Perform a transaction that must fully succeed or fully fail
- Recreate the same query in SQL and in the ORM

### DTTP application

The Employee Management System depends on this level. Do not hide all data work behind generated ORM calls.

### Level complete

- [ ] Can design a normalized schema for the training project
- [ ] Can write joins and aggregations by hand
- [ ] Can use transactions correctly
- [ ] Can explain an ORM query in SQL
- [ ] Can name one valid later use of NoSQL

> ORM knowledge must not replace SQL knowledge.

### Worked example

Design and seed this minimum schema:

```text
departments(id, name UNIQUE)
employees(id, name, email UNIQUE, department_id FK, joining_date, role)
attendance(id, employee_id FK, work_date, status)
leaves(id, employee_id FK, start_date, end_date, type, status)
```

Then write, by hand:

1. Employees with department names (`INNER JOIN`).
2. Employees with or without a department (`LEFT JOIN`).
3. Leave count by department (`GROUP BY`).
4. A transaction that approves a leave and writes the related attendance change. If the second write fails, both roll back.

Show the SQL that the ORM would generate for the leave-count report.

### Stop rule

If the trainee cannot write the join and the transaction without the ORM, stay here.

---

## Level 7 — Architecture

**Purpose:** move from developer thinking to engineer thinking.

Study architectural models, but understand **why** architecture changes.

### Study

- Client-server
- Layered / n-tier architecture
- Monolith
- Modular monolith
- Service-oriented architecture
- Microservices
- Component-based architecture
- Microfrontends
- Messaging and async boundaries
- MVC, MVP, MVVM
- Separation of concerns
- Coupling and cohesion
- When distribution adds cost

### DTTP principle

Do **not** teach microservices first.

```text
Monolith
   ↓
Layered Architecture
   ↓
Modular Monolith
   ↓
Distributed Systems
   ↓
Microservices
```

### Must be able to explain

- Why a trainee project should start as a layered monolith
- What problem microservices solve
- What problem microservices create
- Why UI patterns (MVC/MVVM) are not the same as deployment architecture

### Practice

- Draw the Employee Management System as a layered monolith
- Identify modules: auth, employees, attendance, leave, reports
- List three reasons not to split those modules into services yet
- Review a mentor diagram and explain trade-offs

### DTTP application

Java and Python implementations use the same layered shape:

```text
React → REST → Service → Persistence → MySQL / PostgreSQL
```

### Level complete

- [ ] Can draw the current training system
- [ ] Can name each layer and its responsibility
- [ ] Can explain monolith vs microservices without slogans
- [ ] Can justify the DTTP architecture sequence

### Worked example

Draw one diagram with these layers and one sentence of ownership for each:

```text
React pages / services
        ↓
REST controllers or routers
        ↓
Domain services (leave rules, role checks)
        ↓
Repositories / ORM
        ↓
MySQL or PostgreSQL
```

Mark modules: auth, employees, departments, attendance, leave, reports. Write three reasons this training system should remain a layered monolith. Example: one database, one team, one deployable, and no independent scaling need yet.

### Stop rule

If the trainee says “microservices scale better” without naming a concrete problem the current system has, stay here.

---

## Level 8 — Testing, Security & Performance

**Purpose:** make quality a permanent habit, not a late phase.

### Testing

- Why automated tests exist
- Unit tests for business rules
- Integration tests for API and database
- TDD as a discipline, not a religion
- Coverage as a signal, not a target
- Test doubles: dummy, stub, spy, mock, fake
- Positive, negative, and edge cases
- Frontend: component, form, API-state, and error-state tests
- Postman collections for the business API

### Security

- Injection, especially SQL injection
- XSS and output encoding
- Authentication vs authorization
- Password hashing
- JWT and token storage risks
- Roles and permissions
- Sensitive data and secrets
- Environment variables
- TLS / HTTPS
- CORS and same-origin policy
- CSP
- Least privilege
- Security headers and configuration

### Performance

- Measure before optimizing
- Time to first byte, payload size, query time
- Connection optimization
- Server-side caching
- Client-side caching
- Image optimization
- Minification and compression
- Lazy loading and preloading
- Slow SQL and N+1 queries
- Avoiding premature optimization

### Must be able to explain

- What a unit test should not talk to
- Why 80% coverage can still miss the important bug
- Why secrets never belong in Git
- Why a faster page starts with a measurement

### Practice

- Write service tests for employee create and leave approve
- Write API tests for 401, 403, and 422
- Attempt a safe demonstration of validation blocking injection
- Run a simple performance check on a list endpoint
- Fix one slow query or missing index

### DTTP application

Security and tests are part of the Definition of Done in the 90-day handbook. This level makes those checks a self-growth habit.

### Level complete

- [ ] Can write unit and API tests
- [ ] Can explain authn vs authz
- [ ] Can keep secrets out of source control
- [ ] Can measure one performance number and improve it
- [ ] Can name the main OWASP-style risks that apply to the project

> Never commit passwords, API keys, tokens, private keys, or production credentials to GitHub.

### Worked example

For leave approval, write:

1. A service unit test: HR can approve a pending leave.
2. A service unit test: an ordinary employee cannot approve leave.
3. API tests for `401` (no token), `403` (wrong role), and `409` (already decided).
4. A short security note: where the JWT is stored, why `localStorage` is risky, and how secrets stay out of Git.
5. One measured improvement: time `GET /api/employees` before and after an index or query change. Record both numbers.

### Stop rule

If the trainee cannot show a failing test first, or cannot show a measured number, stay here. “It feels faster” does not complete this level.

---

## Level 9 — DevOps & Deployment

**Purpose:** connect code to a running, repeatable delivery path.

### Git

- Repository, working tree, staging, commit
- Meaningful commit messages
- Branch per task
- Push, pull, fetch
- Merge vs rebase at a practical level
- Pull request and review
- Conflict resolution
- Revert and stash

### Docker

- Image vs container
- Dockerfile
- Volumes and networks
- Environment variables
- Docker Compose for frontend, backend, and database

### Deployment

- Build artifacts
- Hosting and servers
- Container deployment
- Health checks
- Logs
- Rollback thinking

### DTTP delivery path

```text
Git → GitHub → GitHub Actions → Docker → AWS
```

Pipeline shape:

```text
Developer → GitHub → Build → Lint → Unit Tests
   → Integration Tests → Docker Build → Artifact
   → Deployment → Health Check
```

AWS introduction: IAM, EC2, S3, RDS, CloudFront, Route 53, Security Groups, CloudWatch. Understand the purpose of each service before using it.

### Must be able to explain

- Why main/master is protected
- Difference between an image and a container
- Why CI should fail on a broken test
- What IAM is for

### Practice

- Use the standard DTTP Git workflow on every task
- Write a Dockerfile for backend and frontend
- Compose app + database locally
- Add a GitHub Actions workflow for lint and tests
- Deploy a simple environment and hit a health endpoint

### Level complete

- [ ] Can complete a branch / PR / review / merge cycle
- [ ] Can run the project with Docker Compose
- [ ] Can describe a CI pipeline
- [ ] Can explain the purpose of the core AWS services
- [ ] Can diagnose a failed deploy from logs

### Worked example

Deliver the Employee Management System as a repeatable path:

1. Feature branch named after the task.
2. Dockerfile for frontend and backend.
3. `docker-compose.yml` that starts frontend, backend, and database.
4. GitHub Actions workflow: lint, unit tests, then image build.
5. A health endpoint the trainee can hit after compose starts.
6. A one-page deploy note: what ran, what failed, what the logs said, and how they recovered.

### Stop rule

If the trainee cannot start the stack with Compose and explain a failed CI log, stay here. Pushing straight to `main` / `master` does not complete this level.

---

## Level 10 — Professional Software Engineering

**Purpose:** move beyond technology into how professional teams work.

### Agile and Scrum

- Agile principles
- Scrum roles: Product Owner, Scrum Master, Developers
- Events: planning, daily, review, retrospective
- Artifacts: product backlog, sprint backlog, increment
- User stories and acceptance criteria
- Estimation as a conversation
- Review as a demo of working software
- Retrospective as process improvement

### Work breakdown

| Level | Example |
| --- | --- |
| Epic | Employee Management |
| Feature | Leave |
| User story | As an HR user, I want to approve leave so that attendance stays accurate. |
| Task | Create leave approve API |
| Subtasks | Entity, DTO, service rule, controller, test, PR |

### Professional skills

- Communication in stand-up and written updates
- Requirement analysis: what, why, whose, what “done” means
- Documentation: README, API notes, decisions
- Code review: clarity, correctness, security, tests
- Estimation and saying what is uncertain
- Ownership of a task until it is production-ready
- Teamwork and asking for help early
- Technical presentation
- Mentoring a peer on one topic

### Daily report habit

Objective, completed work, learning, problems, investigation, resolution, Git activity, next plan.

### Must be able to explain

- The difference between a task and a user story
- How a feature meets the Definition of Done
- How to give review feedback that improves the code, not the person

### Practice

- Write user stories for attendance and leave
- Break one story into backend and frontend tasks
- Present a 10-minute walkthrough of a pull request
- Review a peer PR using a checklist
- Keep daily reports for two consecutive weeks

### DTTP application

This level is how the trainee becomes eligible for Junior Full-Stack Developer responsibilities, not merely how they finish a course.

### Level complete

- [ ] Can write a user story with acceptance criteria
- [ ] Can break work into tasks and subtasks
- [ ] Can review code with specific comments
- [ ] Can present a feature to a mentor
- [ ] Can describe their own skill gaps honestly

### Worked example

Write this story and the work under it:

> As an HR user, I want to approve or reject a pending leave request so that attendance stays accurate.

Acceptance criteria:

- Only HR or ADMIN can approve or reject.
- A pending leave can be decided once.
- The employee can see the new status.
- A rejected request does not change attendance.
- Tests, review, and notes exist before the story is called done.

Break it into backend, frontend, test, and documentation tasks. Present a 10-minute pull-request walkthrough. Keep daily reports for ten consecutive training days.

### Stop rule

If the trainee cannot state acceptance criteria without saying “it works,” stay here.

---

## Incremental Employee Management build

The same project grows through the ten levels. Do not wait until Level 5 to start it, and do not rebuild a new app at every level.

| Level | What to add to the same Employee Management System |
| :---: | --- |
| 1 | Static employee table page and a request-path diagram |
| 2 | New-employee form, DOM table, public fetch demo |
| 3 | React login, protected list, create form, service layer, mocked API |
| 4 | Written API contract, error shape, Postman collection |
| 5 | Real authenticated CRUD on the chosen backend track |
| 6 | Schema, seed data, join report, leave transaction |
| 7 | Layered diagram and module map attached to the repo |
| 8 | Service tests, API tests, security note, one measured query |
| 9 | Compose file, CI workflow, health check, deploy notes |
| 10 | Stories, PR walkthrough, daily reports, mentor demo |

### Role matrix the trainee must implement

| Action | ADMIN | HR | EMPLOYEE |
| --- | :---: | :---: | :---: |
| Manage users and roles | Yes | No | No |
| Create / update employees | Yes | Yes | No |
| View own profile | Yes | Yes | Yes |
| Record / view attendance | Yes | Yes | Own only |
| Apply for leave | Yes | Yes | Yes |
| Approve / reject leave | Yes | Yes | No |

---

## Oral review bank

A mentor can close a level with these questions. The trainee answers without reading notes. A vague answer means the level is not closed.

| Level | Ask this |
| :---: | --- |
| 1 | What happens after a user types a URL? What is the difference between a file server and an application server? |
| 2 | Why did this CSS rule not apply? How is `fetch` different from reloading the page? |
| 3 | Where should employee-list state live? Why is the API call not inside the JSX? |
| 4 | When is the answer `401` instead of `403`? What JSON do you return for a missing email? |
| 5 | Which layer owns “email must be unique”? What does the controller return if the service throws a conflict? |
| 6 | Write the SQL for employees with department names. What does a rollback protect in leave approval? |
| 7 | Why is this system still a monolith? What would have to be true before leave becomes its own service? |
| 8 | What did you measure? What test proves an employee cannot approve leave? |
| 9 | Why did CI fail? What is the difference between an image and a container? |
| 10 | What is the acceptance criteria for leave approval? What would you tell a peer in a review? |

---

## Depth ladder

Use this when a trainee finishes a level early. Do not skip ahead. Deepen the same level.

| Level | Minimum | Expected | Stretch |
| :---: | --- | --- | --- |
| 1 | Static page + URL parts | Request-path diagram + DevTools notes | Compare static hosting vs an application server |
| 2 | Form + table | Keyboard-only use + fetch error state | Accessible date field and validation messages |
| 3 | Login + one list | Protected routes + service layer | Empty, loading, and error states on every page |
| 4 | Method/status table | Postman collection + error contract | Pagination and filter query design |
| 5 | One CRUD resource | Authn + one role check + one service test | Attendance and leave on the same layering |
| 6 | Schema + one join | Report query + transaction | Explain an `EXPLAIN` / query plan |
| 7 | Layer diagram | Module map + three “not yet services” reasons | Sketch a later modular-monolith split |
| 8 | Two tests | 401/403/409 tests + security note | Before/after timing on one query |
| 9 | Branch + PR | Compose + failing-then-passing CI | Health check and rollback note |
| 10 | One user story | Ten daily reports + PR walkthrough | Mentor a peer on one topic |

---

## Complete reference answers

These are passing answers and contracts. A trainee who cannot produce something this specific is not finished, even if the checklist is ticked.

### Model oral answers

**Level 1.** The browser reads the URL, asks DNS for the host, opens a TCP connection to the host and port, sends an HTTP request for the path, and renders the response. A file server returns `index.html`. An application server runs Java or Python and may read a database before it responds. JavaScript in the page runs in the browser after the document arrives.

**Level 2.** `fetch` sends an HTTP request and leaves the current page in place. A form submit without `preventDefault` reloads the page. If a CSS rule does not apply, check selector match, specificity, inheritance, and whether a later rule overrides it. Keyboard use means every control is reachable with Tab and activated with Enter or Space.

**Level 3.** Employee-list data is fetched in a service, stored in page state or a hook, and passed to a table as props. The token lives in auth context. If the token is missing, the route redirects to `/login`. JSX does not contain `fetch` URLs.

**Level 4.** `401` means the server does not know who the caller is. `403` means the server knows the caller and refuses the action. `GET` must not create an employee. Create is `POST` and success is `201`.

**Level 5.** The unique-email rule lives in the service and in a database unique constraint. The controller only translates the result to HTTP. A conflict is `409`, not `500`.

**Level 6.** `INNER JOIN` returns employees who have a department. `LEFT JOIN` also returns employees with a null department. A transaction around leave approval means the status change and any attendance write both commit or both roll back.

**Level 7.** This training system is a layered monolith because one team, one database, and one deployable are enough. Microservices would add network, data, and ownership cost before there is an independent scale problem.

**Level 8.** A unit test for leave approval must fail when an EMPLOYEE calls it. Coverage percentage is not proof. A performance claim needs two measured numbers.

**Level 9.** An image is the packaged filesystem. A container is a running instance of that image. CI must run the same tests as the trainee and fail the merge when they fail.

**Level 10.** Acceptance criteria are testable statements: who can act, what status changes, and what must not happen. “It works” is not a criterion.

### Login contract

```json
POST /api/auth/login
{ "email": "hr@deshmukh.local", "password": "correct-password" }

201/200
{ "token": "<jwt>", "role": "HR", "employeeId": 12, "name": "Asha Patil" }

401
{ "error": "INVALID_CREDENTIALS", "message": "Email or password is wrong" }
```

### Create employee contract

```json
POST /api/employees
Authorization: Bearer <hr-or-admin-token>
{
  "name": "Rohan Deshmukh",
  "email": "rohan@deshmukh.local",
  "departmentId": 3,
  "joiningDate": "2026-08-18",
  "role": "EMPLOYEE"
}

201
{
  "id": 41,
  "name": "Rohan Deshmukh",
  "email": "rohan@deshmukh.local",
  "departmentId": 3,
  "departmentName": "Engineering",
  "joiningDate": "2026-08-18",
  "role": "EMPLOYEE"
}
```

| Case | Status | Error code |
| --- | :---: | --- |
| Missing email | 400 / 422 | `VALIDATION_FAILED` |
| No token | 401 | `UNAUTHENTICATED` |
| EMPLOYEE caller | 403 | `FORBIDDEN` |
| Email already used | 409 | `CONFLICT` |
| Department missing | 404 | `NOT_FOUND` |

### Leave approve contract

```json
PUT /api/leaves/18/approve
Authorization: Bearer <hr-token>
{ "decision": "APPROVED" }

200
{ "id": 18, "employeeId": 41, "status": "APPROVED", "decisionBy": 12 }

409 already decided
{ "error": "CONFLICT", "message": "Leave is already APPROVED" }
```

Sequence the trainee must narrate: apply (`PENDING`) → HR approves (`APPROVED`) → second approve (`409`) → employee sees the new status. Reject uses the same endpoint with `"REJECTED"` and must not write attendance.

### SQL the trainee must be able to write

```sql
SELECT e.id, e.name, d.name AS department
FROM employees e
INNER JOIN departments d ON d.id = e.department_id
WHERE e.role = 'EMPLOYEE'
ORDER BY e.name;

SELECT d.name, COUNT(l.id) AS leave_count
FROM departments d
LEFT JOIN employees e ON e.department_id = d.id
LEFT JOIN leaves l ON l.employee_id = e.id AND l.status = 'APPROVED'
GROUP BY d.name
ORDER BY leave_count DESC;
```

### Wrong answers that fail the level

| Level | Fails if the trainee says |
| :---: | --- |
| 1 | “The browser just loads it.” |
| 2 | “I used a div for the form because it was easier.” |
| 3 | “I called fetch inside the button JSX.” |
| 4 | “401 and 403 are the same — the user cannot enter.” |
| 5 | “The controller checks the duplicate email and talks to the table.” |
| 6 | “The ORM writes the join. I do not need SQL.” |
| 7 | “We should start with microservices so it scales.” |
| 8 | “I did not write a failing test. Coverage is 90%.” |
| 9 | “I pushed to master because the change was small.” |
| 10 | “Done means it worked on my laptop.” |

---

## Mentor checkpoints and common mistakes

| Level | Mentor asks | Common mistake | Required artifact |
| :---: | --- | --- | --- |
| 1 | What happens after a URL is entered? | Jumping to React immediately | Request-path diagram + static page |
| 2 | Why did this CSS rule not apply? | Ignoring accessibility and errors | Responsive page + fetch demo |
| 3 | Where does this state belong? | Putting API calls inside JSX | Typed React feature with routes |
| 4 | Why is this 403, not 401? | Treating all failures as 500 | Network notes + API contract |
| 5 | Which layer owns this rule? | Fat controllers, no tests | CRUD API with one service test |
| 6 | Show the SQL behind this ORM call | Using only generated queries | Schema + join report query |
| 7 | Why is this still a monolith? | Copying microservices slogans | Architecture diagram |
| 8 | What did you measure? | Optimizing before measuring | Tests + one security note |
| 9 | Why did CI fail? | Committing to main directly | Compose file + Actions workflow |
| 10 | What is the acceptance criteria? | “It works on my machine” | Story, PR walkthrough, daily reports |

### Evidence rule

A level is not complete because the trainee attended a session. It is complete when the artifact exists in Git, the trainee can explain it, and a mentor has reviewed it.

---

## Most important improvement

Do **not** make the uploaded reference material itself the entire DTTP curriculum.

Use it as the **Full-Stack Knowledge Reference**, then combine it with the Deshmukh Technologies practice stack and real projects.

That creates a practical **Deshmukh Technologies Full-Stack Developer Self-Growth Program** while preserving the strong topic progression in the reference.

The transformation remains:

```text
STUDENT
   ↓
TRAINEE
   ↓
PRACTITIONER
   ↓
PROJECT CONTRIBUTOR
   ↓
INDEPENDENT TRAINEE
   ↓
PRODUCTION-READY
   ↓
JUNIOR FULL-STACK DEVELOPER
```

---

# DESHMUKH TECHNOLOGIES

## DTTP — Self-Growth Program

### Learn. Build. Solve. Review. Deploy. Grow.

**Program outcome:** a self-directed full-stack developer.
