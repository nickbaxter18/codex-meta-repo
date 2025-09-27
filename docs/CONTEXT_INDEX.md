# Context Index

This document acts as a navigation map for Cursor (Codex) and human contributors. It highlights where core logic lives and how the OpenAI submodules relate to the U-DIG-IT application.

## Hub Application (U-DIG-IT)

- `U-DIG-IT/backend/main.py` - FastAPI entrypoint, Sentry wiring, environment loading.
- `U-DIG-IT/backend/pyproject.toml` - Poetry configuration and Python dependencies.
- `U-DIG-IT/frontend/src/` - Vite + React UI scaffold for the rental platform.
- `U-DIG-IT/frontend/scripts/sentry-smoke.mjs` - Frontend Sentry smoke test harness.
- `U-DIG-IT/docs/` - Hub-specific architecture notes (expand as features grow).

## OpenAI Tooling Submodules

- `core/codex/` - Codex CLI source, sandbox docs, MCP configuration guidance.
- `core/openai-agents-python/` - Python Agents SDK (multi-agent orchestration, sessions, guardrails, examples).
- `core/openai-agents-js/` - JavaScript/TypeScript Agents SDK with realtime extensions.
- `sdk/openai-python/` - Official Python REST SDK (OpenAPI generated, sync + async clients).
- `sdk/openai-node/` - Official Node SDK supporting Responses, Realtime, and extensions.
- `realtime/openai-realtime-agents/` - Advanced realtime/voice agent patterns and Next.js demo.
- `voice/whisper/` - Whisper speech-to-text reference implementation.
- `specs/model_spec/` - Model spec markdown and evaluation prompts.

## Support Utilities

- `utils/codex-universal/` - Reference Docker image for Codex environments.
- `utils/tiktoken/` - Token counting tools for analytics and cost projections.
- `examples/` - Sample applications for customer support, quickstarts, and agent demos.

## Automation & Configuration

- `Makefile` - Common workflows: submodule sync, dependency installation, smoke tests.
- `.github/workflows/ci.yaml` - CI pipeline orchestrating backend, frontend, and agents SDK checks.
- `.cursorignore` - Exclusion patterns that keep large artifacts out of Codex context windows.
- `.editorconfig` - Formatting defaults across languages.
- `.env` / `.env.example` - Centralized environment configuration consumed by both backend and frontend.

Keep this index fresh whenever you add new packages, major directories, or significant automation. It is the fastest way for Codex (and teammates) to understand where to work.
