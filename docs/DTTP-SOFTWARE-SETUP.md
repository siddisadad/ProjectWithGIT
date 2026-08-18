# DTTP — Trainee Software Setup & Environment Verification

### Deshmukh Technologies Trainee Program

**Document type:** Trainee Onboarding  
**Version:** 1.2  
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

Day 1 of DTTP is not a lecture day. It is the day the machine becomes a working engineering station. Read this guide **before** you write Employee Management code. Follow the [Day-1 hour plan](#33-day-1-hour-plan). Mentors use the [10-minute station check](#35-mentor-10-minute-station-check).

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
15. Day-1 hour plan
16. Official installer product names
17. Mentor 10-minute station check
18. Day-1 completion criteria

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

Open Command Palette (`Ctrl+Shift+P`) → **Preferences: Open User Settings (JSON)**. This is the DTTP default for React + TypeScript:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.tabSize": 2,
  "files.eol": "\n",
  "files.insertFinalNewline": true,
  "javascript.updateImportsOnFileMove.enabled": "always",
  "typescript.updateImportsOnFileMove.enabled": "always",
  "[javascript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[javascriptreact]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[typescriptreact]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "[json]": { "editor.defaultFormatter": "esbenp.prettier-vscode" }
}
```

Create `.prettierrc` in the **frontend** folder if the starter does not ship one:

```json
{
  "singleQuote": true,
  "semi": true,
  "trailingComma": "es5",
  "printWidth": 100
}
```

Line endings stay **LF** even on Windows so Linux CI does not fight you.

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

### First open of the Maven project

1. File → Open → select the folder that contains `pom.xml` (not a parent zip).
2. Trust the project.
3. Wait for Maven import. If it hangs: click the **m** reload icon in the Maven tool window.
4. File → Project Structure (`Ctrl+Alt+Shift+S`) → Project SDK **17** → Language level **17**.
5. Settings → Build, Execution, Deployment → Build Tools → Maven → **Maven home** = Use Maven wrapper (or Bundled). Runner JRE = 17.
6. Settings → Build → Compiler → Annotation Processors → **Enable annotation processing** (needed later for MapStruct / Lombok if the starter uses them).
7. Open the class with `@SpringBootApplication`. Green arrow → Run.
8. Terminal in IntelliJ: `curl http://localhost:8080/api/health` — or use the HTTP Client.

If IntelliJ says “SDK is not defined”: Project Structure → Project SDK → **17** → Apply → Maven reload.

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

### Set JAVA_HOME in the Windows GUI

If PowerShell still cannot see Java:

1. Start → type **environment variables** → **Edit the system environment variables**
2. **Environment Variables…**
3. Under **System variables**, **New…**
   - Name: `JAVA_HOME`
   - Value: the JDK folder, for example `C:\Program Files\Eclipse Adoptium\jdk-17.0.12+7`
4. Edit **Path**, **New**, add `%JAVA_HOME%\bin`
5. OK all dialogs. Open a **new** PowerShell.

Do not point `JAVA_HOME` at `bin`. Do not add both a JRE `bin` and a JDK `bin` and hope.

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

Install the **current Node.js LTS** that matches the assigned frontend (check `package.json` → `engines` and `.nvmrc` if present). DTTP frontend is **React + TypeScript**.

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

### PostgreSQL — when the project says so

The DTTP default is MySQL. If the assigned repo uses PostgreSQL:

| Field | Value |
| --- | --- |
| Host | localhost |
| Port | 5432 |
| Training database | `dttp_training` |

Install PostgreSQL and pgAdmin (or use `psql`). Create `dttp_training` and a local user. Spring URL becomes `jdbc:postgresql://localhost:5432/dttp_training`. Do not run MySQL and PostgreSQL on the same port. Do not mix drivers.

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

Install Docker Desktop for Windows. The **Windows Subsystem for Linux 2** backend is required. Do this **before** you expect `docker run hello-world` to work.

### WSL 2

**PowerShell as Administrator:**

```powershell
wsl --install
wsl --status
wsl --set-default-version 2
```

Restart Windows when Windows asks. After reboot, complete the Ubuntu (or default distro) user prompt if it appears — you can use a simple local username; this is not the GitHub account.

**BIOS / UEFI (if `wsl --install` or Docker says virtualization is disabled):**

1. Reboot → enter firmware (often Del, F2, or F10 — laptop sticker / manual).
2. Enable **Intel VT-x** or **AMD-V** / SVM. Save and exit.
3. Company laptop: stop and ask IT. Do not share BIOS passwords in Slack.

Then install **Docker Desktop**. Settings → General → Use the WSL 2 based engine. Apply & Restart.

```powershell
wsl --status
docker --version
docker compose version
docker run hello-world
```

`hello-world` must pull and print a success message once. You do **not** need Kubernetes enabled in Docker Desktop for DTTP.

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

If RAM is 8 GB, start Docker only when the day’s work needs it. The mentor may waive Docker **in writing**.

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

### Sample `docs/setup-notes.md`

The mentor may ask for this file on the setup branch:

```markdown
# Day-1 environment

- OS: Windows 11
- RAM: 16 GB
- JDK: 17 (`javac 17.0.x`)
- Node: 22.x
- MySQL: 8.x on 3306, database dttp_training
- Docker: installed / waived
- GitHub SSH: pass (`ssh -T`)
- Backend: cloned, `mvnw spring-boot:run`, GET /api/health
- Frontend: `npm run dev`, Chrome loads
- Secrets: none committed
```

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

```powershell
Get-Service *mysql*
Start-Service MySQL80
```

The service name may be `MySQL57` or similar. Open Workbench only after the service is **Running**.

### Port 8080 already in use

```powershell
netstat -ano | findstr :8080
```

The last column is the PID. Task Manager → Details → End task, **or** run Spring Boot on 8081 and write that in `docs/setup-notes.md`.

### IntelliJ “SDK is not defined”

File → Project Structure → Project SDK → **17**. Apply. Maven reload.

### VS Code TypeScript errors on a new clone

`npm install` in `frontend/`. Reload window. Confirm `typescript` is in `devDependencies`.

### `wsl --install` says virtualization disabled

BIOS/UEFI: Intel VT-x or AMD-V **Enabled**. Save, boot, retry. Company laptops: ask IT — do not guess BIOS passwords.

### Antivirus blocks JDK / Docker

Add `C:\Development` and Docker Desktop as exceptions **only if company policy allows**. Record the ticket in `docs/setup-notes.md`.

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
- [ ] VS Code format-on-save and Prettier default formatter
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
- [ ] WSL 2 installed (`wsl --status`) if Docker is required
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

Then run the [10-minute station check](#35-mentor-10-minute-station-check). Do not sign Pass from screenshots of a different PC.

| Result | Meaning |
| --- | --- |
| **Pass** | Day-1 complete. Trainee may start Phase 1 technical work. |
| **Conditional** | Listed gaps with a fix date within 48 hours. |
| **Fail** | Environment is not usable. Repeat setup with mentor support. |

**Mentor name:** ______________________ **Result:** Pass / Conditional / Fail  
**Notes:**  
**Date:** __________

### Sample Conditional note

```text
Result: CONDITIONAL
Gaps (fix by 20 Aug, 17:00):
  1. javac not on PATH — set JAVA_HOME via System Properties, new terminal.
  2. Origin is HTTPS — set-url to git@github.com:org/repo.git and retest ssh -T.
Docker waived (8 GB RAM) until Week 10.
```

Do not write “fix environment” with no command. The trainee should know the exact remaining step.

---

## 33. Day-1 hour plan

Do **not** start Employee Management screens on Day 1. Finish this clock. If you fall behind, skip Flutter and Docker polish — finish Git, JDK, Node, MySQL, clone, health, first commit, and the sign-off table.

| Hour | Block | Done when |
| --- | --- | --- |
| **0–1** | Folders, Git identity, SSH, GitHub test | `ssh -T git@github.com` succeeds. `git config --global user.email` is your **company** address. |
| **1–2** | JDK 17 GUI `JAVA_HOME`, Maven wrapper, IntelliJ | `java -version` is 17. `.\mvnw.cmd -v` works. IntelliJ SDK is 17. |
| **2–3** | Node LTS, VS Code + ESLint + Prettier | `node -v` is 20 or 22. Settings.json has format-on-save ([§9](#9-vs-code-installation)). |
| **3–4** | MySQL 8, `dttp_training`, Postman | Smoke SQL ran. Postman GET `https://postman-echo.com/get` is 200. |
| **4–5** | Clone starter, run `/api/health`, first commit, evidence pack, sign-off | Health JSON prints. GitHub shows the commit. Mentor has the table. |

If the starter repo is late: still finish tools and `dttp_training`. Write that sentence in `docs/setup-notes.md`. Do **not** invent a private Spring project as a substitute for the official starter.

**What you will not do on Day 1:** EMS leave APIs, AWS, Kubernetes, Flutter (unless assigned), production Docker images.

---

## 34. Official product names

Download from the vendor. Do not use a random “JDK 17” zip from a blog.

| Tool | What to search / download |
| --- | --- |
| Git | Git for Windows — `https://git-scm.com/download/win` |
| JDK 17 | Eclipse Temurin 17 (x64 MSI) **or** Microsoft Build of OpenJDK 17 |
| IntelliJ | IntelliJ IDEA Community Edition |
| Node | Node.js **LTS** Windows Installer (.msi) x64 |
| VS Code | Visual Studio Code User Installer x64 |
| MySQL | MySQL Installer for Windows — MySQL Server **8.0** |
| PostgreSQL | PostgreSQL Windows x86-64 installer from EnterpriseDB (only if assigned) |
| Postman | Postman for Windows |
| Docker | Docker Desktop for Windows |
| Flutter | Flutter SDK Windows zip from Flutter docs (only if assigned) |
| Python | Python 3.12 from `https://www.python.org/downloads/` (only if assigned FastAPI) |

---

## 35. Mentor 10-minute station check

Sit at the trainee machine. Run **these** commands. Do not accept screenshots of a different PC.

**PowerShell:**

```powershell
git --version
git config --global user.name
git config --global user.email
ssh -T git@github.com
java -version
echo $env:JAVA_HOME
node -v
npm -v
Get-Service *mysql*
```

**Then:**

1. `cd` into the cloned starter. `git remote -v` must be GitHub, not a USB copy.
2. `.\mvnw.cmd -q -DskipTests spring-boot:run` (or IntelliJ Run). Wait until the process starts.
3. `curl http://localhost:8080/api/health` — JSON with a healthy status (project path may differ).
4. `mysql -u dttp_dev -p -e "USE dttp_training; SELECT 1;"` (password from the trainee’s local notes — not from chat).
5. Open `docs/setup-notes.md` in the repo. Confirm it is **committed**, not only on Desktop.
6. GitHub.com → the assigned repo → latest allowed commit author is the trainee.

**Pass in 10 minutes** means: identity, SSH, JDK 17, Node, MySQL service running, health JSON, notes file on GitHub.

**Fail immediately if:** `user.email` is Gmail/personal; `JAVA_HOME` empty; health never returns; MySQL service Stopped and trainee cannot start it; repo is missing.

---

## 36. Day-1 completion criteria

Day 1 is complete only when **all** of the following are true:

- [ ] Core verification commands succeed (Docker only if not waived)
- [ ] GitHub SSH authentication succeeds
- [ ] Git identity uses the **company email**
- [ ] JDK 17 is on PATH and `JAVA_HOME` is set (verified after a **new** terminal)
- [ ] Node LTS is on PATH. VS Code format-on-save is on ([§9](#9-vs-code-installation))
- [ ] Assigned repository is cloned into `C:\Development\Projects`
- [ ] MySQL (or assigned PostgreSQL) **service is Running** and `dttp_training` exists; smoke SQL ran
- [ ] Backend **or** frontend starter runs locally (both if both repos are assigned)
- [ ] `GET /api/health` returned JSON
- [ ] One API call is shown in Postman or Chrome Network
- [ ] One allowed commit is pushed on a feature branch with `docs/setup-notes.md`
- [ ] Trainee sign-off is filled
- [ ] Mentor result is Pass or Conditional after the [10-minute station check](#35-mentor-10-minute-station-check)
- [ ] Docker is Pass **or** Conditional with a dated next action — not silently skipped

Until then, the trainee does not start Employee Management features. A broken machine produces fake velocity.

> Install. Configure. Verify. Then build.

---

# DESHMUKH TECHNOLOGIES

## DTTP — Trainee Software Setup & Environment Verification

### Learn. Build. Solve. Review. Deploy. Grow.
