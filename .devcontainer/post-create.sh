#!/bin/bash

set -euo pipefail

echo "🚀 Setting up Codex Meta Repo development environment..."

# Navigate to workspace
cd /workspaces/codex-meta-repo

# Install root dependencies
echo "📦 Installing root dependencies..."
if [ -f pnpm-lock.yaml ]; then
  CI=true pnpm install --frozen-lockfile
elif [ -f package-lock.json ]; then
  npm ci
elif [ -f package.json ]; then
  npm install
fi

# Set up Python backend
echo "🐍 Setting up Python backend..."
cd U-DIG-IT/backend
poetry install --with dev
cd ../..

# Set up frontend dependencies
echo "⚛️ Setting up frontend..."
cd U-DIG-IT/frontend
if [ -f pnpm-lock.yaml ]; then
  CI=true pnpm install --frozen-lockfile
else
  CI=true pnpm install
fi
cd ../..

# Set up git hooks
echo "🔗 Setting up git hooks..."
npm run prepare

echo "🔒 Setting up pre-commit hooks..."
cd /workspaces/codex-meta-repo
if command -v pre-commit >/dev/null 2>&1 && [ -f .pre-commit-config.yaml ]; then
  pre-commit install
elif [ -f U-DIG-IT/backend/.pre-commit-config.yaml ]; then
  cd U-DIG-IT/backend
  poetry run pre-commit install
  cd ../..
else
  echo "ℹ️ No pre-commit configuration found; skipping installation."
fi

echo "ℹ️ Docker services can be managed with 'docker compose -f .devcontainer/docker-compose.yml up -d' from the host or any environment that has access to the Docker daemon."

# Run database migrations and seeding
echo "🗄️ Setting up database..."
cd U-DIG-IT/backend
poetry run python scripts/generate_dev_env.py
cd ../..

echo "✅ Development environment setup complete!"
echo ""
echo "🎉 You can now:"
echo "   - Run 'npm run dev' to start both frontend and backend"
echo "   - Run 'cd U-DIG-IT/backend && poetry run uvicorn app.main:app --reload' for backend only"
echo "   - Run 'cd U-DIG-IT/frontend && pnpm dev' for frontend only"
echo "   - Use 'docker compose -f .devcontainer/docker-compose.yml up' to start all services"
echo ""
echo "🔧 Services available:"
echo "   - Frontend (container): http://localhost:4173"
echo "   - Backend API (container): http://localhost:8000"
echo "   - PostgreSQL (container network): postgres:5432"
echo "   - Redis (container network): redis:6379"
