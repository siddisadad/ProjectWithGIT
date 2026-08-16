# DTTP — Trainee Software Setup & Environment Verification

### Deshmukh Technologies Trainee Program

**Document type:** Trainee Onboarding  
**Version:** 1.0  
**Status:** Standard  
**Audience:** DTTP Trainees, Mentors, Technical Coordinators, Admin  
**Platform:** Windows 10 / 11  
**Primary stack:** Java, Spring Boot, React, MySQL, Git, Docker  
**Mobile track:** Flutter  
**Alternate backend (when assigned):** Python / FastAPI

A designed, print-ready version is available in [`DTTP-SOFTWARE-SETUP.pdf`](./DTTP-SOFTWARE-SETUP.pdf) and [`DTTP-SOFTWARE-SETUP.html`](./DTTP-SOFTWARE-SETUP.html).

The 90-day handbook remains in [`DTTP-PROGRAM-HANDBOOK.pdf`](./DTTP-PROGRAM-HANDBOOK.pdf).

---

## 1. Purpose

This document is the standard software and development environment for every Deshmukh Technologies trainee.

Every trainee must independently complete this path **before** assigned project work:

```text
Install → Configure → Verify → Clone → Build → Run → Test → Commit → Push
```

Day 1 of DTTP is not a lecture day. It is the day the machine becomes a working engineering station.

### Companion documents

| Document | Role |
| --- | --- |
| This setup guide | Machine, tools, GitHub, Day-1 sign-off |
| 90-Day DTTP Handbook | Timed training path, project, assessment |
| Self-Growth Program | Ten-level knowledge map |

---

## 2. Scope

This guide covers:

1. Software installation
2. Windows development environment
3. Git and GitHub
4. SSH authentication
5. Java and Spring Boot
6. Node.js and React
7. MySQL
8. Postman
9. Docker
10. Flutter for mobile trainees
11. Environment verification
12. Troubleshooting
13. Trainee sign-off
14. Mentor / admin verification
15. Day-1 completion criteria

Python / FastAPI is installed only when the trainee is assigned that backend track. JDK remains the DTTP default.

---

## 3. Standard software checklist

| Software | Purpose | Required |
| --- | --- | --- |
| Windows 10 / 11 | Operating system | Yes |
| Git | Version control | Yes |
| GitHub account | Source code | Yes |
| VS Code | General / frontend development | Yes |
| IntelliJ IDEA | Java / Spring Boot | Yes |
| JDK 17 (or 21 if the project says so) | Java development | Yes |
| Maven | Java build | Yes |
| Node.js LTS | JavaScript / React | Yes |
| npm | Node package management | Yes |
| MySQL Server | Database | Yes |
| MySQL Workbench | Database management | Yes |
| Postman | API testing | Yes |
| Google Chrome | Browser / debugging | Yes |
| Docker Desktop | Containers | Recommended |
| Flutter SDK | Mobile development | Mobile track |
| Android Studio | Android development | Mobile track |
| Python 3.11+ | FastAPI track | Python track only |

---

## 4. Hardware requirements

### Minimum

- 8 GB RAM
- 256 GB SSD
- Modern dual / quad-core processor
- Stable internet connection
- Windows 10 / 11

### Recommended

- 16 GB RAM
- 512 GB SSD
- Intel Core i5 / AMD Ryzen 5 or better
- Full HD display
- Reliable broadband

A machine below the minimum will struggle with IntelliJ + Chrome + Docker + MySQL at the same time. Tell the mentor before Day 1 if the machine is below minimum.

---

## 5. Windows preparation

### Step 1 — Update Windows

**Settings → Windows Update → Check for updates**

Install available security and system updates.

### Step 2 — Restart

Restart after major Windows updates. Do not install JDK, Docker, or Android Studio on a pending-reboot machine.

### Step 3 — Create the development directory

Recommended root:

```text
C:\Development\
```

Create:

```text
C:\Development\Projects
C:\Development\Tools
C:\Development\Documents
C:\Development\Backups
```

Do **not** keep project clones in `C:\Windows`, `C:\Program Files`, Desktop, or Downloads.

### Step 4 — Enable long paths (recommended)

Some Node and Java trees exceed the old 260-character path limit. In an **Administrator** PowerShell:

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
  -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

---

## 6. Git installation

Install **Git for Windows**. During setup:

- Git from the command line and also from 3rd-party software
- Use the bundled OpenSSH
- Override the default branch name: `main`
- Checkout as-is, commit Unix-style line endings (`core.autocrlf` = `input`) is acceptable if the team agrees; do not mix settings mid-project

Open a **new** PowerShell window:

```powershell
git --version
```

Expected:

```text
git version 2.x.x
```

Configure identity with the name and email used on GitHub:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
git config --global --list
```

A commit with a personal Gmail while the GitHub user is a company account will confuse review. Use the address on the GitHub profile.

---

## 7. GitHub account

Each trainee must have an authorized GitHub account and repository access from the DTTP mentor or admin.

Never share:

- GitHub password
- Personal access tokens
- Private SSH keys
- Company secrets

Access is granted to **named people**, not to shared logins.

---

## 8. GitHub SSH configuration

Open PowerShell.

### Generate a key

```powershell
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Press Enter to accept the default location `C:\Users\<you>\.ssh\id_ed25519`. Set a passphrase. Remember it.

### Start the SSH agent

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

If `Set-Service` is denied, open PowerShell **as Administrator** for those two service lines only, then return to a normal window for `ssh-add`.

### Copy the public key only

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

The public key starts with `ssh-ed25519` and is one line. Never copy `id_ed25519` without `.pub`.

### Add it on GitHub

**GitHub → Settings → SSH and GPG keys → New SSH key**

- Title: `DTTP-Windows-<your-name>`
- Key type: Authentication key
- Paste the public key

### Test

```powershell
ssh -T git@github.com
```

Expected (the username will be yours):

```text
Hi <github-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

First connection may ask to trust GitHub’s host key. Type `yes`.

---

## 9. VS Code installation

Install Visual Studio Code.

### Required extensions

- Prettier
- ESLint
- GitLens
- EditorConfig
- Docker
- REST Client
- Extension Pack for Java
- Spring Boot Extension Pack

React trainees also install **ES7+ React/Redux/React-Native snippets** if the mentor agrees. Prefer typing the code in training; snippets are optional.

### Settings

- Format On Save: **On**
- Auto Save: **afterDelay** or **onFocusChange**
- Default formatter: Prettier for `javascript`, `typescript`, `json`

---

## 10. IntelliJ IDEA

Install IntelliJ IDEA (Community is enough for DTTP unless the company issues Ultimate).

Use it for:

- Java
- Spring Boot
- Maven
- JUnit
- Mockito
- Hibernate / JPA
- Spring Security

Configure:

| Setting | Value |
| --- | --- |
| Project SDK | JDK 17 (or 21 if the project says so) |
| Build tool | Maven |
| Version control | Git |
| Annotation processing | Enabled for Spring projects |

Do not mix VS Code and IntelliJ on the same Java change in the same hour. Pick one editor for a given backend task.

---

## 11. Java JDK installation

DTTP default: **JDK 17 LTS**, unless the assigned project specifies another supported version (21 is acceptable when the `pom.xml` says so).

Install a full JDK, not only a JRE.

### PATH and JAVA_HOME

System environment variables:

```text
JAVA_HOME = C:\Program Files\Java\jdk-17
Path      += %JAVA_HOME%\bin
```

The exact folder name depends on the vendor (Eclipse Temurin, Microsoft Build of OpenJDK, Oracle). Point `JAVA_HOME` at the JDK root, not at `bin`.

Close **all** terminals, open a new PowerShell:

```powershell
java -version
javac -version
echo $env:JAVA_HOME
```

Both `java` and `javac` must work. `java` without `javac` means a JRE is on PATH.

Expected shape:

```text
openjdk version "17.0.x"
javac 17.0.x
```

---

## 12. Maven installation

Install Apache Maven 3.9.x, or rely on the **Maven Wrapper** in the project.

```powershell
mvn -version
```

Expected: Maven 3.8+ or 3.9+, Java 17.

For any DTTP repo that contains `mvnw.cmd`, prefer:

```powershell
.\mvnw.cmd clean install
```

The wrapper uses the Maven version the project defined. Do not “upgrade Maven globally” to fix a wrapper build.

---

## 13. Spring Boot verification

Clone the assigned backend (SSH URL, not HTTPS):

```powershell
cd C:\Development\Projects
git clone git@github.com:<org>/<backend-repo>.git
cd <backend-repo>
```

Copy local config from the example. **Never commit the copy.**

```text
src\main\resources\application-local.properties
```

Example shape (values are local only):

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/dttp_training
spring.datasource.username=dttp_dev
spring.datasource.password=use-a-local-password
```

Build and run:

```powershell
.\mvnw.cmd clean install
.\mvnw.cmd spring-boot:run
```

Pass when:

- The build finishes with `BUILD SUCCESS`
- The process stays up
- Logs show a successful MySQL connection
- `GET http://localhost:8080/api/health` returns `{ "status": "ok" }` (or the project’s health path)

If the assigned repo is not ready on Day 1, create `dttp_training` in MySQL anyway and keep the clone/build evidence from the starter the mentor names.

---

## 14. Node.js installation

Install the **current Node.js LTS** that matches the assigned frontend (check `package.json` → `engines` and `.nvmrc` if present).

```powershell
node --version
npm --version
```

Expected: Node 20.x or 22.x LTS unless the project pins another version.

Do not change Node versions to “fix” `npm install` on an existing lockfile. Match the project.

---

## 15. React environment

```powershell
cd C:\Development\Projects
git clone git@github.com:<org>/<frontend-repo>.git
cd <frontend-repo>
copy .env.example .env
npm install
npm run dev
```

Some projects use `npm start` instead of `npm run dev`. Follow `package.json` scripts.

Open the URL Vite or CRA prints (often `http://localhost:5173`). Chrome must load the app.

Trainees must be able to point to, in the cloned code:

- Components
- Props
- State
- Hooks
- Routing
- API calls in a service file
- Forms
- Error handling
- Environment variables (`VITE_` or `REACT_APP_` — never commit secrets)

---

## 16. MySQL installation

Install:

- MySQL Server 8.x
- MySQL Workbench

During server setup:

- Use a **local** root password stored in a password manager, not in chat
- Enable MySQL as a Windows service
- Port **3306**

```powershell
mysql --version
```

Standard development:

| Field | Value |
| --- | --- |
| Host | localhost |
| Port | 3306 |
| Training database | `dttp_training` |

Never use production credentials on a trainee machine.

---

## 17. MySQL verification

In Workbench, connect to the local server. Then in a SQL tab:

```sql
CREATE DATABASE IF NOT EXISTS dttp_training
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'dttp_dev'@'localhost' IDENTIFIED BY 'use-a-local-password';
GRANT ALL PRIVILEGES ON dttp_training.* TO 'dttp_dev'@'localhost';
FLUSH PRIVILEGES;

USE dttp_training;

CREATE TABLE smoke_test (
  id INT PRIMARY KEY AUTO_INCREMENT,
  label VARCHAR(80) NOT NULL
);

INSERT INTO smoke_test (label) VALUES ('DTTP Day 1');
SELECT * FROM smoke_test;
UPDATE smoke_test SET label = 'verified' WHERE id = 1;
DELETE FROM smoke_test WHERE id = 1;
```

The trainee must be able to: connect, create a database, create a table, insert, query, update, and delete.

---

## 18. Postman installation

Install Postman.

Learn: GET, POST, PUT, PATCH, DELETE.

Understand: URL, query parameters, path variables, headers, JSON body, Bearer token, status codes.

Day-1 collection (adjust host if the starter uses another port):

```text
POST /api/auth/login
        ↓
JWT in response
        ↓
Authorization: Bearer <token>
        ↓
GET /api/employees
GET /api/health
```

Save the collection in `C:\Development\Documents`. Do not put real production tokens in it.

---

## 19. Docker Desktop

Install Docker Desktop for Windows. WSL 2 backend is required. Enable virtualization in BIOS if Docker says it is off.

```powershell
docker --version
docker compose version
docker run hello-world
```

`hello-world` must print a success message once.

Useful commands:

```powershell
docker ps
docker images
docker build .
docker compose up -d
docker compose down
docker info
```

Understand: image, container, Dockerfile, volume, network, Compose.

If RAM is 8 GB, start Docker only when the day’s work needs it.

---

## 20. Flutter setup — mobile track

Mobile trainees install:

- Flutter SDK (stable)
- Android Studio
- Android SDK + command-line tools
- Android Emulator **or** an authorized physical device with USB debugging
- VS Code or IntelliJ
- Git (already required)

Add Flutter `bin` to PATH. New terminal:

```powershell
flutter --version
flutter doctor
flutter doctor -v
```

Accept Android licenses when `flutter doctor` asks.

Smoke app:

```powershell
cd C:\Development\Projects
flutter create dttp_test_app
cd dttp_test_app
flutter run
```

Pass when the counter app launches on the emulator or authorized device.

---

## 21. Chrome DevTools

Open Chrome, press **F12**.

| Panel | Use |
| --- | --- |
| Elements | Inspect HTML / CSS |
| Console | JavaScript errors |
| Network | API request, status, payload |
| Application | Local Storage, Session Storage, cookies |
| Sources | Breakpoints in JS / TS |

Day-1 check: load the React app, open Network, confirm the document request and (when the API is up) one XHR/fetch.

---

## 22. Environment verification

Run in a **new** PowerShell. Paste the output into the sign-off form.

### Core

```powershell
git --version
java -version
javac -version
mvn -version
node --version
npm --version
mysql --version
docker --version
docker compose version
```

Docker lines may be skipped only if the mentor waived Docker for an 8 GB machine, in writing.

### GitHub

```powershell
ssh -T git@github.com
```

### Mobile track

```powershell
flutter --version
flutter doctor
```

### Python track (when assigned)

```powershell
python --version
pip --version
```

Expected Python 3.11 or 3.12.

---

## 23. Project verification

```text
GitHub repository
        ↓
Clone (SSH)
        ↓
Install dependencies
        ↓
Configure local environment (not committed)
        ↓
Database connection
        ↓
Build
        ↓
Run backend
        ↓
Run frontend
        ↓
Test API in Postman
        ↓
Make a small allowed change
        ↓
Commit
        ↓
Push
```

### First commit standard

Only after the mentor names a safe file (README note or `docs/setup-notes.md`):

```powershell
git checkout -b dttp/<initials>/env-setup
git add docs/setup-notes.md
git commit -m "docs: record Day-1 environment verification"
git push -u origin dttp/<initials>/env-setup
```

Do not push secrets. Do not commit `.env` or `application-local.properties`.

---

## 24. Environment variables

Never hard-code credentials.

Sensitive names include:

```text
DB_PASSWORD
JWT_SECRET
API_KEY
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

Use:

- `.env` (frontend)
- `application-local.properties` or `application-dev.properties` (Spring)
- `.env` for FastAPI when assigned

Never commit secrets. Confirm they are listed in `.gitignore`.

---

## 25. Recommended `.gitignore`

Every project must ignore at least:

```text
.env
.env.local
application-local.properties
.idea/
.vscode/
node_modules/
build/
dist/
target/
*.log
*.jks
*.pem
*.p12
id_rsa
id_ed25519
```

Follow the technology `.gitignore` in the assigned repo. If a secret was committed by mistake, tell the mentor immediately. Do not only delete the file in a later commit.

---

## 26. Troubleshooting

### Git command not recognized

```powershell
git --version
```

If missing: reinstall Git, tick “Git from the command line”, **close and reopen** PowerShell.

### Java / javac not recognized

1. JDK installed, not JRE
2. `JAVA_HOME` points at the JDK root
3. `%JAVA_HOME%\bin` is on PATH
4. New terminal

```powershell
Get-Command java | Format-List
echo $env:JAVA_HOME
```

### Maven not recognized

Use `.\mvnw.cmd` in the project. Global `mvn` is optional.

### Node / npm not recognized

Reinstall Node LTS. New terminal. Do not mix Chocolatey and the official installer blindly.

### `npm install` fails

```powershell
node --version
npm --version
```

Read `package.json`, `package-lock.json`, `.nvmrc`. Do not delete `node_modules` and change versions at random. Delete `node_modules` and rerun `npm install` only after matching the Node version.

### MySQL connection fails

Check: service running, port 3306, username, password, database exists, `application-local.properties` host is `localhost` (not a Docker hostname unless the app runs in Compose).

Windows Services: **MySQL80** (name may vary) must be Running.

### Docker does not start

1. Docker Desktop is running
2. Virtualization enabled
3. WSL 2 healthy (`wsl --status`)
4. Restart Docker Desktop
5. `docker info`

### Flutter doctor errors

```powershell
flutter doctor -v
```

Fix the first reported Android SDK, license, emulator, or PATH issue. Do not ignore red items on the mobile track.

### SSH still asks for a password to GitHub

You cloned an **HTTPS** URL. Change remote:

```powershell
git remote -v
git remote set-url origin git@github.com:<org>/<repo>.git
ssh -T git@github.com
```

---

## 27. Security rules

- Never share passwords on WhatsApp or email.
- Never commit credentials to GitHub.
- Never expose API keys.
- Never share private SSH keys.
- Never upload company source to unauthorized locations (personal public repos, paste sites, AI tools that store code, unless the company policy allows that tool).
- Never use production credentials for training.
- Never install unauthorized software on a company machine.
- Report security incidents to the mentor or admin immediately.

---

## 28. Trainee setup checklist

### Windows

- [ ] Windows updated and restarted
- [ ] `C:\Development\` folders created
- [ ] PowerShell opens and can run `git`

### Development tools

- [ ] Git installed and identity configured
- [ ] VS Code installed with required extensions
- [ ] IntelliJ IDEA installed, SDK = JDK 17/21
- [ ] `java` and `javac` both work
- [ ] Maven or `mvnw.cmd` verified
- [ ] Node.js LTS and npm verified
- [ ] Chrome installed

### Database / API

- [ ] MySQL Server running on 3306
- [ ] Workbench connected
- [ ] `dttp_training` created and smoke SQL ran
- [ ] Postman installed
- [ ] Health or login request saved in a collection

### DevOps

- [ ] Docker Desktop installed **or** written waiver from mentor
- [ ] `docker run hello-world` succeeded (if Docker is required)

### GitHub

- [ ] Account exists
- [ ] Repository access received
- [ ] SSH key generated; **public** key added to GitHub
- [ ] `ssh -T git@github.com` succeeded
- [ ] Assigned repo cloned with SSH

### Mobile track

- [ ] Flutter on PATH
- [ ] Android Studio + SDK
- [ ] Emulator or authorized device
- [ ] `flutter doctor` reviewed
- [ ] `dttp_test_app` launched

### Python track

- [ ] Python 3.11+ and pip verified (only if assigned)

---

## 29. Alternate backend — Python / FastAPI

Install only when the mentor assigns the Python track.

```powershell
python --version
pip --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Execution policy if activation is blocked:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Health check is still `GET /api/health`. Same MySQL database. Same Git and security rules.

---

## 30. Evidence pack

Attach screenshots or a pasted log to the Day-1 report. Crop secrets.

| Evidence | What it shows |
| --- | --- |
| `git --version` and `git config --global --list` | Git identity |
| `ssh -T git@github.com` | SSH works |
| `java -version` and `javac -version` | JDK |
| `node --version` and `npm --version` | Node |
| Workbench connected to `dttp_training` | Database |
| Backend `BUILD SUCCESS` or running log | Spring Boot |
| Browser with the React app | Frontend |
| Postman `GET /api/health` | API |
| GitHub showing the setup branch | Push |
| `flutter doctor` (mobile) | Mobile track |

---

## 31. Trainee sign-off

Complete in writing. A verbal “it’s done” is not Day-1 complete.

| Field | Trainee fills |
| --- | --- |
| Full name | |
| Date | |
| GitHub username | |
| Machine (make / RAM / disk) | |
| Windows version | |
| Backend track (Java / Python) | |
| Mobile track (Yes / No) | |
| Docker (Installed / Waived) | |
| Assigned backend repo | |
| Assigned frontend repo | |

I confirm that I installed the required tools, that SSH authentication works, that I can clone, build, and run the assigned starter, that no secrets are in Git, and that the evidence pack is attached.

**Trainee signature / typed name:** ______________________ **Date:** __________

---

## 32. Mentor / admin verification

The mentor checks the machine or the evidence pack. Spot-check at least:

1. `ssh -T git@github.com`
2. `java` and `javac` (or Python, if that track)
3. MySQL `dttp_training`
4. One running app (backend or frontend)
5. `.gitignore` does not leave `.env` unignored
6. Remote URL is `git@github.com:...` not `https://`

| Result | Meaning |
| --- | --- |
| **Pass** | Day-1 complete. Trainee may start Phase 1 technical work. |
| **Conditional** | Listed gaps with a fix date within 48 hours. |
| **Fail** | Environment is not usable. Repeat setup with mentor support. |

**Mentor name:** ______________________ **Result:** Pass / Conditional / Fail  
**Notes:**  
**Date:** __________

---

## 33. Day-1 completion criteria

Day 1 is complete only when **all** of the following are true:

- [ ] Core verification commands succeed (Docker only if not waived)
- [ ] GitHub SSH authentication succeeds
- [ ] Assigned repository is cloned into `C:\Development\Projects`
- [ ] `dttp_training` exists and smoke SQL ran
- [ ] Backend **or** frontend starter runs locally (both if both repos are assigned)
- [ ] One API call is shown in Postman or Chrome Network
- [ ] One allowed commit is pushed on a feature branch
- [ ] Trainee sign-off is filled
- [ ] Mentor result is Pass or Conditional with a dated gap list

Until then, the trainee does not start Employee Management features.

> Install. Configure. Verify. Then build.

---

# DESHMUKH TECHNOLOGIES

## DTTP — Trainee Software Setup & Environment Verification

### Learn. Build. Solve. Review. Deploy. Grow.
