# Django + Next.js Starter Template

A production-ready full-stack starter with:

- **Backend**: Django 6.1 + Django REST Framework + SimpleJWT
- **Frontend**: Next.js 15 (App Router) + TypeScript + Tailwind
- **Auth**: JWT (access + refresh tokens)
- **Email**: Console in dev, SMTP in prod (via `MAILERS`)
- **Env-driven**: Switch dev → prod by editing `.env` only
- **CORS**: Pre-configured for Next.js on `:3000`

---

## 📁 Project Structure

```
.
├── back/                       # Django backend
│   ├── manage.py
│   ├── .env.example            # template — copy to .env
│   ├── requirements.txt
│   ├── api/                    # main Django app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   └── back/                   # Django project
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── front/                      # Next.js frontend
│   ├── .env.local.example      # template — copy to .env.local
│   ├── package.json
│   ├── next.config.ts
│   └── app/
├── .gitignore
├── README.md
└── venv/                       # created by you (not committed)
```

---

## 🚀 Quick Start

### 1. Clone (or copy) the template

```bash
git clone https://github.com/YOUR-USER/YOUR-TEMPLATE.git myproject
cd myproject
```

### 2. Backend setup

```bash
cd back
python -m venv ..\venv
..\venv\Scripts\activate           # Windows
# source ../venv/bin/activate      # Mac/Linux

pip install -r requirements.txt

copy .env.example .env             # Windows
# cp .env.example .env             # Mac/Linux

# Generate a fresh SECRET_KEY for this project
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# → paste output into back/.env as SECRET_KEY

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend → **http://127.0.0.1:8000**

### 3. Frontend setup (new terminal)

```bash
cd front
copy .env.local.example .env.local   # Windows
# cp .env.local.example .env.local   # Mac/Linux

npm install
npm run dev
```

Frontend → **http://localhost:3000**

---

## 🔧 Make It a Fresh Repo for a New App

When you clone the template, Git still points to the **template's remote**. To start a brand-new project with its own repo, follow this workflow.

### Method A — Clean Fresh Start (Recommended)

This wipes the template's history entirely — perfect for a brand-new project.

#### 1. Remove old Git history

```bash
# Windows (PowerShell)
Remove-Item -Recurse -Force .git

# Mac/Linux
rm -rf .git
```

#### 2. Initialize fresh Git

```bash
git init
git branch -M main
```

#### 3. Set up backend and frontend

Follow the **Quick Start** section above (venv, `.env`, npm install, etc.).

#### 4. First commit

```bash
git add .
git commit -m "Initial commit"
```

#### 5. Create the new repo on GitHub

Go to **https://github.com/new** and:

- Enter a repo name (e.g. `myproject`)
- ❌ **Do NOT** initialize with README, `.gitignore`, or license
- Click **Create repository**

#### 6. Link the new remote and push

```bash
git remote add origin https://github.com/YOUR-USER/myproject.git
git push -u origin main
```

Done ✅ — you now have a fresh, independent repo with one clean commit.

---

### Method B — Use GitHub's "Use this template"

If this repo is marked as a **Template repository**:

1. Go to the template repo on GitHub
2. Click **"Use this template"** → **"Create a new repository"**
3. Give it a name, choose visibility, click **Create**

GitHub creates the new repo with a single fresh commit — no template history carried over.

Then locally:

```bash
git clone https://github.com/YOUR-USER/myproject.git
cd myproject

# Then follow Quick Start (setup .env, venv, npm)
```

---

### Method C — Preserve Template History (Not recommended)

If you want to keep the template's commits for reference:

```bash
# Rename the existing remote
git remote rename origin template

# Add your new origin
git remote add origin https://github.com/YOUR-USER/myproject.git

# Push the current branch
git push -u origin main
```

Downside: The new repo shows the template's full commit history, which can be confusing.

---

### Verify Git Setup After Cloning

```bash
git remote -v
```

Should show **your new repo**, not the template:

```
origin  https://github.com/YOUR-USER/myproject.git (fetch)
origin  https://github.com/YOUR-USER/myproject.git (push)
```

If it still shows the template remote:

```bash
git remote set-url origin https://github.com/YOUR-USER/myproject.git
```

Check the working tree is clean:

```bash
git status
# → On branch main
# → nothing to commit, working tree clean
```

---

## 🔑 Environment Files

The template ships with **example env files** (safe to commit) but **not** the real ones (never commit).

| File                       | Committed? | Purpose                             |
| -------------------------- | :--------: | ----------------------------------- |
| `back/.env.example`        |     ✅      | Template for backend env            |
| `back/.env`                |     ❌      | Real secrets (secret key, DB, SMTP) |
| `front/.env.local.example` |     ✅      | Template for frontend env           |
| `front/.env.local`         |     ❌      | Real API URL for this machine       |

### `back/.env.example`

```env
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
EMAIL_BACKEND_KIND=console
DEFAULT_FROM_EMAIL=no-reply@example.com
SERVER_EMAIL=no-reply@example.com
```

### `front/.env.local.example`

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## 🌐 Endpoints

| Method | URL                   | Auth     | Description     |
| ------ | --------------------- | -------- | --------------- |
| GET    | `/api/hello/`         | ❌        | Health check    |
| POST   | `/api/send-email/`    | ❌        | Send test email |
| GET    | `/api/me/`            | ✅ Bearer | Current user    |
| POST   | `/api/token/`         | ❌        | Get JWT (login) |
| POST   | `/api/token/refresh/` | ❌        | Refresh JWT     |
| POST   | `/api/token/verify/`  | ❌        | Verify JWT      |
| GET    | `/admin/`             | session  | Django admin    |

Test with curl:

```bash
# Hello
curl http://127.0.0.1:8000/api/hello/

# Get JWT
curl -X POST http://127.0.0.1:8000/api/token/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"admin\",\"password\":\"yourpass\"}"

# Use JWT
curl http://127.0.0.1:8000/api/me/ ^
  -H "Authorization: Bearer PASTE_ACCESS_TOKEN"
```

---

## 🔀 Dev vs Prod

Only `.env` changes — **no code changes**.

| Setting       | Dev (local PC)          | Prod (Ubuntu)            |
| ------------- | ----------------------- | ------------------------ |
| `DEBUG`       | `True`                  | `False`                  |
| Database      | SQLite                  | PostgreSQL               |
| Email backend | console                 | SMTP                     |
| CORS          | `http://localhost:3000` | `https://yourdomain.com` |
| Server        | `runserver`             | gunicorn + nginx         |
| HTTPS         | off                     | on                       |

Switch by editing `.env`:

```env
# Dev
DEBUG=True
EMAIL_BACKEND_KIND=console

# Prod
DEBUG=False
EMAIL_BACKEND_KIND=smtp
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
```

---

## 🧪 Sending Email Locally

With `EMAIL_BACKEND_KIND=console`, all emails print to the terminal running `runserver`.

```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail("Test", "Hello", None, ["a@b.com"])
```

Expected: email body printed in the terminal ✅

---

## 📦 Requirements

```txt
Django>=6.1,<6.2
djangorestframework
djangorestframework-simplejwt
django-cors-headers
python-dotenv
```

Update after adding packages:

```bash
pip freeze > requirements.txt
```

---

## 🧰 Useful Commands

| Task             | Command                                    |
| ---------------- | ------------------------------------------ |
| Start backend    | `python manage.py runserver`               |
| Start frontend   | `cd front && npm run dev`                  |
| Make migrations  | `python manage.py makemigrations`          |
| Apply migrations | `python manage.py migrate`                 |
| Create superuser | `python manage.py createsuperuser`         |
| Django shell     | `python manage.py shell`                   |
| Check settings   | `python manage.py check`                   |
| Deploy check     | `python manage.py check --deploy`          |
| Collect static   | `python manage.py collectstatic --noinput` |

---

## 🐛 Common Issues

| Problem                                  | Fix                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------- |
| `ModuleNotFoundError: corsheaders`       | Activate venv + `pip install -r requirements.txt`                     |
| Email tries to connect to `localhost:25` | Ensure Django ≥6.1 + `MAILERS` configured (not old `EMAIL_BACKEND`)   |
| `ConnectionRefusedError` on port 25      | Use `EMAIL_BACKEND_KIND=console` locally                              |
| CORS error in browser                    | Add `corsheaders.middleware.CorsMiddleware` **first** in `MIDDLEWARE` |
| `400 Bad Request`                        | Set `ALLOWED_HOSTS` correctly in `.env`                               |
| Static files 404                         | Run `collectstatic`; in prod, serve via Nginx                         |
| `.env` not loaded                        | Place it next to `manage.py`, restart server                          |

---

## 🧑‍💻 Development Workflow

Run both servers in **two terminals**:

**Terminal 1 — Backend**

```bash
cd back
..\venv\Scripts\activate
python manage.py runserver
```

**Terminal 2 — Frontend**

```bash
cd front
npm run dev
```

Open:

- Backend → http://127.0.0.1:8000
- Frontend → http://localhost:3000
- Admin → http://127.0.0.1:8000/admin/

---

## 📄 License

MIT — free to use for personal and commercial projects.