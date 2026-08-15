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
