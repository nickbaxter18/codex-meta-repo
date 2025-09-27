#!/bin/bash
# Context extraction script for AI agents and human developers
# This script generates comprehensive context about the repository structure,
# dependencies, and key patterns for use by AI agents and new team members.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${REPO_ROOT}/docs/context"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "🔍 Extracting repository context..."

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Generate repository overview
cat > "$OUTPUT_DIR/repository-overview.md" << EOF
# Repository Overview

Generated: $TIMESTAMP

## Structure
\`\`\`
$(tree -I 'node_modules|.git|__pycache__|.pytest_cache|htmlcov|coverage|dist|build' -L 3)
\`\`\`

## Key Components
- **U-DIG-IT**: Main application (backend + frontend)
- **Core**: OpenAI agent frameworks and tools
- **SDK**: Official OpenAI language SDKs
- **Examples**: Sample applications and demos
- **Utils**: Supporting utilities and tools

## Technology Stack
- **Backend**: FastAPI + SQLModel + PostgreSQL/SQLite
- **Frontend**: React + TypeScript + Vite
- **Testing**: pytest + Vitest + React Testing Library
- **Quality**: Black + ESLint + Prettier + mypy
- **Security**: GitLeaks + Safety + Bandit
EOF

# Extract backend context
cat > "$OUTPUT_DIR/backend-context.md" << EOF
# Backend Context

## Architecture
- **Framework**: FastAPI with async support
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Database**: PostgreSQL (production) / SQLite (development)
- **Authentication**: JWT with bcrypt password hashing
- **Validation**: Pydantic models for request/response validation

## Key Models
$(cd "$REPO_ROOT/U-DIG-IT/backend" && find app -name "*.py" -exec grep -l "class.*SQLModel" {} \; | head -5)

## API Endpoints
$(cd "$REPO_ROOT/U-DIG-IT/backend" && find app/routers -name "*.py" -exec basename {} .py \; | sort)

## Dependencies
$(cd "$REPO_ROOT/U-DIG-IT/backend" && poetry show --tree | head -20)
EOF

# Extract frontend context
cat > "$OUTPUT_DIR/frontend-context.md" << EOF
# Frontend Context

## Architecture
- **Framework**: React 19 with TypeScript
- **Build Tool**: Vite for fast development
- **State Management**: React Query for server state
- **Routing**: React Router v6
- **Styling**: Utility CSS with Tailwind-like classes

## Key Components
$(cd "$REPO_ROOT/U-DIG-IT/frontend/src" && find . -name "*.tsx" -type f | head -10)

## API Integration
$(cd "$REPO_ROOT/U-DIG-IT/frontend/src" && find . -name "*.ts" -exec grep -l "axios\|fetch" {} \; | head -5)

## Dependencies
$(cd "$REPO_ROOT/U-DIG-IT/frontend" && pnpm list --depth=0 | head -20)
EOF

# Extract security context
cat > "$OUTPUT_DIR/security-context.md" << EOF
# Security Context

## Security Tools
- **Secret Scanning**: GitLeaks for detecting exposed secrets
- **Dependency Scanning**: Safety for Python vulnerabilities
- **Code Analysis**: Bandit for security issues
- **Linting**: ESLint with security plugins

## Security Measures
- JWT token authentication with configurable expiration
- Password hashing with bcrypt
- Environment variable validation
- CORS configuration
- Input validation with Pydantic

## Known Vulnerabilities
$(cd "$REPO_ROOT" && ./gitleaks detect --source . --config .gitleaks.toml 2>/dev/null | head -10 || echo "No secrets detected")
EOF

# Extract testing context
cat > "$OUTPUT_DIR/testing-context.md" << EOF
# Testing Context

## Backend Testing
- **Framework**: pytest with coverage reporting
- **Test Types**: Unit, integration, and e2e tests
- **Coverage**: Minimum 80% code coverage required
- **Fixtures**: Comprehensive test data and mocks

## Frontend Testing
- **Framework**: Vitest with React Testing Library
- **Test Types**: Component, integration, and e2e tests
- **Coverage**: Minimum 80% code coverage required
- **Mocking**: API mocking and user interaction simulation

## Test Commands
\`\`\`bash
# Backend tests
cd U-DIG-IT/backend && poetry run pytest

# Frontend tests
cd U-DIG-IT/frontend && pnpm test

# All tests
make test
\`\`\`
EOF

# Extract build context
cat > "$OUTPUT_DIR/build-context.md" << EOF
# Build Context

## Build Tools
- **Backend**: Poetry for dependency management
- **Frontend**: pnpm for package management
- **Monorepo**: Makefile for orchestration
- **CI/CD**: GitHub Actions for automation

## Build Commands
\`\`\`bash
# Install dependencies
make install

# Start development servers
make dev

# Run tests
make test

# Security scanning
make security:scan
\`\`\`

## Environment Configuration
- **Development**: Local development with hot reload
- **Testing**: Isolated test databases
- **Production**: Containerized deployment
EOF

# Generate comprehensive context index
cat > "$OUTPUT_DIR/context-index.md" << EOF
# Context Index

Generated: $TIMESTAMP

This directory contains comprehensive context about the U-DIG-IT repository for AI agents and human developers.

## Files
- \`repository-overview.md\` - High-level repository structure and technology stack
- \`backend-context.md\` - Backend architecture, models, and API details
- \`frontend-context.md\` - Frontend architecture, components, and integration
- \`security-context.md\` - Security tools, measures, and vulnerability information
- \`testing-context.md\` - Testing frameworks, strategies, and commands
- \`build-context.md\` - Build tools, commands, and environment configuration

## Usage
These files are designed to be consumed by:
- AI agents for understanding codebase structure and patterns
- New team members for onboarding and context
- Documentation generators for maintaining up-to-date information
- Code analysis tools for understanding project architecture

## Maintenance
This context is automatically generated and should be updated when:
- New dependencies are added
- Architecture changes are made
- Security tools are updated
- Build processes are modified

Run \`./scripts/fetch-context.sh\` to regenerate all context files.
EOF

echo "✅ Context extraction complete!"
echo "📁 Output directory: $OUTPUT_DIR"
echo "📄 Generated files:"
ls -la "$OUTPUT_DIR"

