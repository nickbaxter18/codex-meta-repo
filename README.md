# Codex Meta Repository

This repository is a meta workspace that consolidates OpenAI agent tooling alongside the U-DIG-IT equipment rental platform. Submodules provide upstream SDKs, realtime demos, and reference environments so Cursor (Codex) and human developers can work with a single, well-instrumented codebase.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `core/` | First-party agent frameworks (`codex`, `openai-agents-python`, `openai-agents-js`, `agents.md`). |
| `sdk/` | Official OpenAI language SDKs (Python, Node). |
| `examples/` | Cookbook and starter applications for common agent scenarios. |
| `voice/` | Voice pipeline references (`whisper`, voice agent samples). |
| `realtime/` | Realtime agent demos and console tooling. |
| `utils/` | Supporting utilities (Codex universal container, tiktoken). |
| `specs/` | Model specification and evaluation suites. |
| `U-DIG-IT/` | **Hub project** for the equipment rental platform (backend, frontend, future agents/voice/realtime glue). |
| `docs/` | Meta documentation for navigation and integrations. |

See `docs/CONTEXT_INDEX.md` for a navigation-friendly map that Cursor can ingest.

## Quick Start

### 1. Prepare Tooling

- Git with submodule support.
- Python 3.13+ with [Poetry](https://python-poetry.org/) (`pip install poetry`).
- Node.js 22+ with Corepack enabled for pnpm (`corepack enable`).
- A POSIX-compatible shell (e.g., Git Bash, WSL) when using the Makefile on Windows.

### 2. Clone with Submodules

```bash
git clone git@github.com:your-org/codex-meta-repo.git
cd codex-meta-repo
git submodule update --init --recursive
```

### 3. Bootstrap Environments

```bash
make install           # installs backend (Poetry) and frontend (pnpm) deps
make submodules-sync   # pulls the latest upstream submodule refs
```

For granular targets (backend only, agents SDK tests, etc.), run `make help`.

### 4. Launch Local Components

```bash
make backend-dev       # uvicorn reload server with .env loaded
make frontend-dev      # vite dev server with HMR
```

Additional integration flows (realtime, voice, agents) are documented in `docs/integration-guides.md`.

## Working with Cursor (Codex)

- Keep `docs/CONTEXT_INDEX.md` updated so the agent can jump directly to relevant code.
- Use `.cursorignore` to prevent large artifacts (`node_modules`, build outputs, datasets) from inflating the assistant context.
- AGENTS.md guidance for interactive development lives in `core/agents.md`.

## Submodule Management

Submodules track upstream OpenAI repositories but do not update automatically. Recommended workflows:

```bash
# Update to the latest recorded commit
make submodules

# Rebase to each upstream repo's default branch
make submodules-refresh
```

If you add new submodules, register them in `.gitmodules` and extend the Makefile targets.

## Continuous Integration

`.github/workflows/ci.yaml` runs three focused jobs:

1. Python backend checks (`poetry install`, optional pytest).
2. Frontend lint/build using pnpm.
3. `core/openai-agents-js` vitest suite to validate critical SDK tooling.

Extend the workflow as new packages (voice, realtime agents, etc.) mature.

## Environment Configuration

The repo ships with `.env.example`; copy it to `.env` and populate real credentials (OpenAI, Sentry, Stripe, feature flag providers, etc.). Backend/Frontend tooling already loads the root `.env` automatically.

## Contributing Guidelines

1. Update relevant docs when adding modules or flows.
2. Keep lockfiles in sync (Poetry `poetry.lock`, pnpm `pnpm-lock.yaml`).
3. Ensure `make lint` and `make test` pass before opening a PR.
4. Use the CI workflow as a reference when adding new language stacks.

Happy building - the more context we feed Codex, the smarter our automation becomes.
