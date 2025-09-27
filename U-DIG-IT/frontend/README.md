# U-DIG-IT Frontend

A production-ready React + TypeScript interface for the U-DIG-IT equipment rental platform. The application ships with a polished marketing site, live catalog, equipment detail workflows, authenticated reservations, and an operations dashboard for managers.

## Tech Stack

- React 19 with Vite for lightning-fast builds.
- TypeScript with zod runtime validation for API responses.
- React Query for data fetching, caching, and optimistic UX.
- React Router v6 for nested layouts and protected routes.
- Lightweight design system (utility CSS + reusable components) tailored to the U-DIG-IT brand.

## Getting Started

1. Install Node.js 22 or newer and enable pnpm via corepack.
2. Install dependencies:
       pnpm install
3. Set API configuration in the repository root .env. The frontend reads:
       VITE_API_BASE_URL=http://localhost:8000
       VITE_FRONTEND_ENVIRONMENT=development
       VITE_FRONTEND_SENTRY_DSN=...
4. Launch the dev server:
       pnpm dev
5. Build for production:
       pnpm build
       pnpm preview

## Feature Overview

- Marketing landing with hero, value props, testimonials, and call-to-action modules.
- Catalog explorer with search, category filters, pricing highlights, and equipment tags.
- Equipment detail pages featuring image gallery, specifications, live availability checks, and authenticated reservation flow.
- Account onboarding with login/registration backed by API tokens.
- Operations dashboard (protected) summarising reservations, revenue trends, and top-performing assets.

## Code Organization

- src/api – Axios client, typed endpoints, zod schemas.
- src/components – UI atoms, layouts, marketing sections.
- src/contexts – Auth provider with token persistence.
- src/hooks – React Query hooks for catalog, landing stats, dashboard.
- src/pages – Route-level screens.
- src/styles – Global design tokens and utility classes.
- src/types – Shared domain models.
- src/utils – Formatters and helpers.

## Quality

- pnpm lint runs ESLint (configured via eslint.config.js).
- Component tests can be added with Vitest (pnpm test).

## Deployment Notes

- pnpm build outputs static assets in dist/ for any CDN or static host.
- Ensure VITE_API_BASE_URL targets the deployed FastAPI backend.
- Sentry and analytics environment variables propagate automatically when present.
