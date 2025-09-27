SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

POETRY ?= poetry
PNPM ?= pnpm

help:
	@echo "Available targets:"
	@echo "  make submodules          # init/update submodules"
	@echo "  make submodules-refresh  # pull latest remote refs"
	@echo "  make install             # install backend + frontend deps"
	@echo "  make backend-dev         # run uvicorn with reload"
	@echo "  make frontend-dev        # run vite dev server"
	@echo "  make agents-test         # run openai-agents-js vitest suite"
	@echo "  make lint                # run linting across surfaces"
	@echo "  make test                # aggregate tests"

submodules:
	git submodule update --init --recursive

submodules-refresh:
	git submodule update --init --recursive --remote

install: backend-install frontend-install core-agents-install

backend-install:
	cd U-DIG-IT/backend && $(POETRY) install --sync

backend-dev:
	cd U-DIG-IT/backend && $(POETRY) run uvicorn main:app --reload --host 0.0.0.0 --port 8000

backend-check:
	cd U-DIG-IT/backend && $(POETRY) run python -m compileall .

frontend-install:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd U-DIG-IT/frontend && $(PNPM) install --frozen-lockfile

frontend-dev:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd U-DIG-IT/frontend && $(PNPM) run dev

frontend-lint:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd U-DIG-IT/frontend && $(PNPM) run lint

frontend-build:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd U-DIG-IT/frontend && $(PNPM) run build

frontend-sentry:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd U-DIG-IT/frontend && $(PNPM) run sentry:test

core-agents-install:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd core/openai-agents-js && $(PNPM) install --frozen-lockfile

agents-test:
	if command -v corepack >/dev/null 2>&1; then corepack enable; fi
	cd core/openai-agents-js && $(PNPM) test

lint: frontend-lint

smoke: backend-check frontend-build agents-test frontend-sentry

test: agents-test

.PHONY: help submodules submodules-refresh install backend-install backend-dev backend-check frontend-install frontend-dev frontend-lint frontend-build frontend-sentry core-agents-install agents-test lint smoke test
