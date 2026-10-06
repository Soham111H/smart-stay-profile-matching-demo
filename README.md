# Smart Stay – Profile Matching Demo

A Django + MariaDB college-project demo for **Smart Stay**, focused on roommate profile matching and explainable compatibility scoring.

> **GitHub-ready version:** this repository is prepared for public sharing. No database password, `.env` file, Python virtual environment, compiled Python files, or local database is included.

## What the demo does

- Create/update a roommate profile
- Store profile data in MariaDB
- Load demo profiles
- Compare roommate lifestyle preferences
- Calculate a weighted compatibility score from 0–100
- Rank potential roommate matches
- Filter matches by minimum score
- Show factor-by-factor scoring
- Explain strongest similarities and potential differences
- Show dashboard statistics
- Display the scoring methodology and weights

## Technology stack

- **Frontend:** HTML, CSS, Django Templates
- **Backend:** Python + Django 4.2.30
- **Database:** MariaDB 10.4.x through XAMPP
- **Database access:** Django ORM + PyMySQL
- **Matching:** Custom weighted compatibility algorithm
- **Environment:** Windows + XAMPP + Python 3.10+

## Compatibility algorithm

The demo compares 10 lifestyle factors:

| Factor | Weight |
|---|---:|
| Budget | 15% |
| Sleep schedule | 15% |
| Cleanliness | 15% |
| Smoking | 15% |
| Food preference | 10% |
| Social style | 10% |
| Noise tolerance | 10% |
| Guests | 5% |
| Cooking | 5% |
| Study/work routine | 5% |

The weighted contributions are combined into a final **0–100 compatibility score**. Higher scores represent stronger lifestyle compatibility.

## Project structure

```text
Smart_Stay/
├── manage.py
├── requirements.txt
├── database_setup.sql
├── .gitignore
├── .env.example
├── README.md
│
├── smart_stay_demo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── matching/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── matching_engine.py
│   └── management/commands/seed_demo.py
│
├── templates/
└── static/
```

## Run locally with the existing XAMPP MariaDB 10.4 setup

This repository keeps the same environment used by the working demo. **Do not upgrade XAMPP or install another database server just to run this project.**

### 1. Start MariaDB in XAMPP

Open XAMPP Control Panel and start **MySQL**.

### 2. Create the database

Open XAMPP Shell or the MariaDB client and run:

```sql
CREATE DATABASE IF NOT EXISTS smart_stay
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
```

The default local configuration expects:

```text
Host: 127.0.0.1
Port: 3306
Database: smart_stay
User: root
Password: empty
```

If your local MariaDB root account has a password, set `SMART_STAY_DB_PASSWORD` in the operating-system environment before starting Django.

### 3. Install Python packages

```bash
python -m pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Load demo profiles

```bash
python manage.py seed_demo
```

**Warning:** `seed_demo` deletes the existing profiles in the selected `smart_stay` database and recreates the seven demo profiles.

### 6. Start Django

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Optional environment variables

The project does not require a `.env` package. Django reads these values from the operating-system environment.

```text
SMART_STAY_DB_NAME
SMART_STAY_DB_USER
SMART_STAY_DB_PASSWORD
SMART_STAY_DB_HOST
SMART_STAY_DB_PORT
SMART_STAY_SECRET_KEY
SMART_STAY_DEBUG
SMART_STAY_ALLOWED_HOSTS
```

A template is provided in `.env.example`. **Do not rename it to `.env` and commit the real file.**

### Windows CMD example

```cmd
set SMART_STAY_DB_PASSWORD=your_password
python manage.py runserver
```

### Windows PowerShell example

```powershell
$env:SMART_STAY_DB_PASSWORD="your_password"
python manage.py runserver
```

## Important GitHub safety rules

Never commit:

- `.env`
- database passwords
- API keys or secret tokens
- `venv/` or `.venv/`
- `__pycache__/`
- `*.pyc`
- private database dumps
- real user personal information

The repository's `.gitignore` already blocks common local/secrets files.

## Demo data

The included `seed_demo` command creates fictional demo roommate profiles. Do not replace them with real people's private information before publishing the repository.

## Backend flow

```text
Browser
  ↓
Django URL routing (urls.py)
  ↓
View (views.py)
  ↓
Form validation (forms.py)
  ↓
Django ORM / Model (models.py)
  ↓
MariaDB
  ↓
Matching Engine (matching_engine.py)
  ↓
Compare 10 factors
  ↓
Weighted compatibility score
  ↓
Rank profiles
  ↓
Generate strengths/differences
  ↓
Django template
  ↓
Browser
```

## GitHub upload

From the project folder:

```bash
git init
git add .
git status
git commit -m "Initial Smart Stay profile matching demo"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Before `git add .`, check that no password, `.env`, database dump, or private data is present.

## Suggested repository name

`smart-stay-profile-matching-demo`

## Project note

This is a college-project demonstration. It is designed for local development with the existing XAMPP MariaDB 10.4 environment and is not a production deployment configuration.
