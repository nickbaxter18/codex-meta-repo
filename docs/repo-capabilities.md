# Repository Capability Overview

This document summarizes the main systems bundled in the codex meta repository so that new operators can quickly understand the surfaces exposed to Cursor/Codex agents and human contributors.

## Core Applications and Modules

- **U-DIG-IT Hub**
  - `backend/`: FastAPI application that wires CORS, Sentry, database bootstrapping, and router registration in `main.py`. 【F:docs/CONTEXT_INDEX.md†L7-L13】【F:docs/architecture.md†L1-L6】
  - `frontend/`: Vite + React UI scaffold for the rental platform backed by pnpm tooling. 【F:docs/CONTEXT_INDEX.md†L7-L13】
  - `docs/`: Hub-specific architecture notes used when the product expands. 【F:docs/CONTEXT_INDEX.md†L7-L13】
- **OpenAI Tooling Submodules** – bundled as Git submodules that expose the latest SDKs and agent frameworks. 【F:docs/CONTEXT_INDEX.md†L15-L23】
  - `core/openai-agents-python`: Python SDK for building multi-agent orchestrations, guardrails, and session state management. 【F:docs/CONTEXT_INDEX.md†L15-L18】
  - `core/openai-agents-js`: JavaScript/TypeScript SDK with realtime extensions for browser and Node runtimes. 【F:docs/CONTEXT_INDEX.md†L15-L19】
  - `sdk/openai-python` and `sdk/openai-node`: Official REST clients that power backend and frontend integrations. 【F:docs/CONTEXT_INDEX.md†L15-L21】
  - `realtime/` and `voice/` directories: Canonical references for realtime, voice, and Whisper-based experiences. 【F:docs/CONTEXT_INDEX.md†L19-L22】
- **Support Utilities** – docker images, token counters, and sample apps that accelerate prototyping. 【F:docs/CONTEXT_INDEX.md†L24-L30】

## Development Workflow Highlights

- Clone the repository with submodules, install backend/frontend dependencies, and copy `.env` templates before starting local development. 【F:docs/DEVELOPMENT.md†L6-L35】
- Run `make dev` (or individual backend/frontend commands) to launch hot-reload servers. 【F:docs/DEVELOPMENT.md†L31-L38】
- Enforce quality through language-specific tooling:
  - Backend: Black formatting, isort, flake8, mypy, bandit, and safety checks. 【F:docs/DEVELOPMENT.md†L40-L59】
  - Frontend: Prettier formatting, ESLint, strict TypeScript, and Vitest suites. 【F:docs/DEVELOPMENT.md†L59-L66】
- Pre-commit hooks automatically run secret scanning, linting, security checks, and unit tests to maintain hygiene. 【F:docs/DEVELOPMENT.md†L68-L80】
- Testing playbooks detail backend pytest targets, frontend Vitest commands, and security scanning make targets. 【F:docs/DEVELOPMENT.md†L82-L143】
- Architecture guidance emphasizes modular FastAPI routers, Pydantic schemas, reusable React components/hooks, and async performance best practices. 【F:docs/DEVELOPMENT.md†L102-L151】

## Automation and Tooling Touchpoints

- The root `Makefile` collects frequently used workflows such as `make install`, `make backend-dev`, `make frontend-dev`, `make agents-test`, and composite smoke/test targets. 【F:Makefile†L1-L52】
- CI guidance in `docs/integration-guides.md` explains how the GitHub workflow orchestrates backend compile checks, frontend builds, and agents SDK tests. 【F:docs/integration-guides.md†L29-L37】
- Observability hooks rely on backend and frontend Sentry smoke tests plus guardrail documentation maintained alongside the Agents SDKs. 【F:docs/integration-guides.md†L21-L28】

Refer back to this overview when onboarding new capabilities or when you need to trace where a subsystem originates inside the repository.
