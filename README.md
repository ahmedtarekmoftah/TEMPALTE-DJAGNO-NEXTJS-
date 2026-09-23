# Django + Next.js Starter

Full-stack template with:
- Django 6.1 + DRF + SimpleJWT
- Next.js 15 (App Router)
- CORS + JWT auth ready
- Email (console dev / SMTP prod)
- `.env`-driven dev/prod settings

## Structure

```
.
├── back/          # Django backend
│   ├── api/       # Main app (models, views, serializers, urls)
│   └── back/      # Project settings
└── front/         # Next.js frontend
    └── app/       # App Router pages
```

## Setup

### 1. Backend

```bash
cd back
python -m venv ../venv
..\venv\Scripts\activate           # Windows
# source ../venv/bin/activate      # Mac/Linux
pip install -r requirements.txt
copy .env.example .env              # create .env from example
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 2. Frontend

```bash
cd front
npm install
copy .env.local.example .env.local
npm run dev
```

### 3. URLs

- Backend: http://127.0.0.1:8000
- Admin:   http://127.0.0.1:8000/admin/
- API:     http://127.0.0.1:8000/api/
- Frontend: http://localhost:3000

## Endpoints (example)

| Method | URL                   | Auth             |
| ------ | --------------------- | ---------------- |
| POST   | `/api/token/`         | ❌                |
| POST   | `/api/token/refresh/` | ❌                |


## Dev vs Prod

Only `.env` changes — no code changes.

| Setting | Dev     | Prod       |
| ------- | ------- | ---------- |
| `DEBUG` | True    | False      |
| DB      | SQLite  | PostgreSQL |
| Email   | console | SMTP       |
| HTTPS   | off     | on         |

## License

MIT