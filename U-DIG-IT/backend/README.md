# U-DIG-IT Backend

FastAPI service powering the U-DIG-IT equipment rental platform. Provides authenticated APIs for catalog browsing, availability, reservations, analytics, and health checks with Sentry instrumentation and database seeding.

## Highlights
- FastAPI application structured via modular routers (auth, catalog, reservations, analytics, health).
- SQLModel ORM with Postgres or SQLite driver support and opinionated domain models (users, equipment, reservations, reviews, maintenance logs, analytics snapshots).
- JWT authentication with password hashing (bcrypt) and configurable expiration windows.
- Sentry integration, .env driven configuration, and automatic sample data seeding on startup.

## Requirements
- Python 3.13+
- Poetry 2.x (install via pip or pipx).
- Database URL (Postgres recommended) or falls back to sqlite:///./u_dig_it.db.

## Setup
1. Install dependencies:
       poetry install
2. Configure environment variables in the repo root .env (copy from .env.example). Key values:
       DATABASE_URL=postgresql://user:password@localhost:5432/codex_meta
       JWT_SECRET=change-me
       BACKEND_SENTRY_DSN=...
3. Run the development server:
       poetry run uvicorn main:app --reload
4. Point the frontend VITE_API_BASE_URL to this service.

On first boot the service creates tables and seeds categories, equipment, locations, an admin user (admin@u-dig-it.com / ChangeMe123!), and a sample reservation.

## Key Endpoints
- GET /health – health probe.
- POST /api/auth/register – create account + bearer token.
- POST /api/auth/login – exchange credentials for JWT.
- GET /api/auth/me – current user profile.
- GET /api/catalog – categories, featured, inventory (supports category, search).
- GET /api/catalog/equipment/{slug} – equipment detail.
- GET /api/catalog/equipment/{slug}/availability – window-based availability check.
- GET /api/catalog/locations – logistics hubs.
- POST /api/reservations – create reservation (auth required).
- PATCH /api/reservations/{code} – update status/payment (admin).
- GET /api/analytics/dashboard – reservations and revenue snapshot (admin/manager).

## Testing
- poetry run python -m compileall app (basic syntax check).
- Add pytest suites under tests/ for deeper coverage (scaffold pending).

## Deployment
- Provide production database credentials, JWT secrets, and Sentry DSN via environment variables.
- Run behind uvicorn or gunicorn (e.g., gunicorn -k uvicorn.workers.UvicornWorker main:app).
- Integrate Alembic for future migrations (models are migration-ready).
