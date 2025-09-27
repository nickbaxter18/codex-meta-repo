# U-DIG-IT Architecture Overview

This document summarises the backend and frontend structure after the Codex upgrade.

## Backend
- Configuration lives in app/config.py using pydantic-settings to parse database URL, CORS origins, JWT lifetimes (supports values such as 60m, 7d), and observability toggles.
- app/database.py builds a SQLModel engine with SQLite dev defaults and Postgres production support.
- app/models.py defines the domain: users, customer profiles, categories, equipment, media, reservations, maintenance logs, reviews, analytics snapshots.
- app/schemas.py exposes response models that convert database structures into camelCase payloads expected by the frontend.
- Routers: auth (register/login/me), catalog (categories, equipment, availability, locations, landing stats), reservations (create/list/update with role checks), analytics (dashboard aggregates), health (status).
- Services package business logic: catalog_service (queries, featured assets, landing metrics, availability math), reservation_service (date validation, totals, updates), seed_data (baseline fixtures, admin user).
- Security helpers (app/security.py and app/dependencies.py) provide bcrypt hashing, JWT encode/decode, and dependency-injected current user/admin guards.

## Frontend
- src/main.tsx boots QueryClientProvider, AuthProvider, and BrowserRouter, applying global styles.
- App.tsx defines routes (home, catalog, equipment detail, solutions, about, contact, login, register, dashboard) wrapped by AppLayout and ProtectedRoute for admin dashboards.
- API layer combines api/client.ts (axios instance) and api/endpoints.ts with zod schemas to validate every response.
- AuthContext persists bearer tokens locally, refreshes session details via /api/auth/me, and clears the React Query cache on logout.
- Hooks encapsulate data fetching: useCatalog, useLandingStats, useEquipmentDetail (plus availability helper), useLocations, useDashboardSnapshot.
- UI/sections deliver the marketing experience (HeroSection, CategoryShowcase, WorkflowSection, TestimonialsSection, CTASection) while shared inputs/buttons live in components/ui.
- Styling centralises design tokens and layout utilities in src/styles/global.css.

## Integration Notes
- Shared environment: root .env provides database credentials, JWT secrets, Sentry DSNs, and VITE_API_BASE_URL.
- Seed admin credentials: admin@u-dig-it.com / ChangeMe123! (update before production use).
- Reservations require authentication; unauthenticated users are redirected to login from the equipment detail page.
- Availability checks request /api/catalog/equipment/{slug}/availability with ISO 8601 dates and surface quantity + messaging in the UI.
- Operations dashboard consumes /api/analytics/dashboard and is gated via ProtectedRoute for admin or manager roles.
- Extend this file as new modules (voice, realtime, agents) come online.
