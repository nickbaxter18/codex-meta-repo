# Integration Guides

This guide outlines how the U-DIG-IT hub project connects to the OpenAI submodules and external services. Use it as the canonical reference when wiring new features or onboarding teammates.

## Backend -> Agents SDK (Python)

1. Install dependencies: `poetry install` inside `U-DIG-IT/backend`.
2. Import agents from `core/openai-agents-python` by referencing the installed package (`from agents import Agent`).
3. Store shared prompts/guardrails in `U-DIG-IT/backend/agents/` (create the folder when needed).
4. Keep sensitive API keys in `.env` (`OPENAI_API_KEY`, `AGENTS_API_KEY`).
5. Add integration tests that exercise agent workflows and run them via `make agents-test`.

## Frontend -> OpenAI SDKs (Node)

1. Run `pnpm install` within `U-DIG-IT/frontend` (the lockfile pins compatible versions).
2. Use the official Node SDK (`sdk/openai-node`) for browser/server interactions.
3. For streaming UI, review `examples/openai-responses-starter-app` and adapt the handlers into `U-DIG-IT/frontend/src/`.
4. Use the Sentry smoke test (`make frontend-sentry`) after wiring new telemetry.

## Voice Pipeline

1. Reference `voice/whisper` for transcription and `voice/openai-voice-agent-sdk-sample` for realtime voice agents.
2. Add voice-specific logic under `U-DIG-IT/voice/` (create this directory when the feature is enabled).
3. Reuse the Agents SDK to orchestrate handoffs between text and voice agents.

## Realtime Experiences

1. Study `realtime/openai-realtime-agents` for multi-agent voice/chat flows.
2. Mirror the Next.js implementation under `U-DIG-IT/realtime/` to keep separation from the main frontend.
3. Expose webhook/API endpoints from the backend and secure them with environment-based secrets.

## Observability & Safety

- Backend Sentry is configured in `U-DIG-IT/backend/main.py`; verify with `make backend-check` after updating settings.
- Frontend Sentry runs through `scripts/sentry-smoke.mjs`.
- Guardrails and moderation patterns are documented in the Agents SDK repos.

## CI/CD Touchpoints

- `.github/workflows/ci.yaml` installs dependencies and runs:
  - `poetry install` + placeholder compile check (backend)
  - `pnpm run lint` / `pnpm run build` (frontend)
  - `pnpm test` (core/openai-agents-js)
- Extend the workflow with additional jobs when voice or realtime code moves into production.

Document new integration paths here whenever you connect another subsystem or SaaS provider.
