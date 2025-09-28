# Codex Meta Repo Development Container

This directory contains the configuration for a Docker-based development environment that eliminates dependency issues and provides a consistent, reproducible development experience.

## 🚀 Quick Start

### Option 1: VS Code/Cursor (Recommended)
1. **Install the Dev Containers extension** in VS Code/Cursor
2. **Open the Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`)
3. **Run "Dev Containers: Reopen in Container"**
4. The container will build automatically and set up your environment

### Option 2: Manual Setup
```bash
# Build and start the dev container
docker compose -f .devcontainer/docker-compose.yml up -d devcontainer

# Access the container
docker exec -it codex-meta-repo_devcontainer-devcontainer-1 bash

# Run the post-create setup manually (if needed)
bash .devcontainer/post-create.sh
```

## 🛠️ What's Included

### Development Tools
- **Node.js 22** with globally available **pnpm** for frontend development
- **Python 3.12** + **Poetry** for backend development
- **Docker** + **Docker Compose** for containerized services
- **Git** with pre-commit hooks
- **PostgreSQL 15** with pgvector extension
- **Redis 7** for caching

### VS Code Extensions (Auto-installed)
- Python: linting, formatting, type checking
- TypeScript: language support, linting
- ESLint, Prettier for code formatting
- Docker extension for container management
- GitLens for enhanced Git integration
- Markdown support with linting

### Services Available
- **Frontend**: React/TypeScript app (port 4173)
- **Backend**: FastAPI/Python app (port 8000)
- **PostgreSQL**: Database with pgvector (port 5432)
- **Redis**: Caching service (port 6379)

## 📁 Project Structure

```
.devcontainer/
├── devcontainer.json    # Main container configuration
├── docker-compose.yml   # Multi-service setup
├── Dockerfile          # Container image definition
├── post-create.sh      # Post-creation setup script
└── README.md           # This file
```

## 🔧 Development Workflow

### Starting Development
```bash
# Start both frontend and backend
npm run dev

# Or start individually:
cd U-DIG-IT/frontend && pnpm dev
cd U-DIG-IT/backend && poetry run uvicorn app.main:app --reload
```

### Database Operations
```bash
# Access PostgreSQL
psql -h localhost -U postgres -d u_dig_it

# Run migrations (when implemented)
cd U-DIG-IT/backend && poetry run alembic upgrade head
```

### Testing
```bash
# Frontend tests
cd U-DIG-IT/frontend && pnpm test

# Backend tests
cd U-DIG-IT/backend && poetry run pytest
```

## 🔒 Environment Variables

The dev container automatically generates secure environment variables:

- **Backend**: `.env` file with JWT secrets, database URLs, API keys
- **Frontend**: Environment variables for API endpoints

## 🚨 Troubleshooting

### Container Won't Start
```bash
# Clean up and rebuild
docker compose -f .devcontainer/docker-compose.yml down
docker system prune -f
docker compose -f .devcontainer/docker-compose.yml up --build
```

### Permission Issues
```bash
# Fix Docker socket permissions
sudo chmod 666 /var/run/docker.sock
```

### Port Conflicts
- Change ports in `.devcontainer/devcontainer.json` if needed
- Update `forwardPorts` and `portsAttributes` sections

### Extensions Not Installing
- Check VS Code/Cursor extension marketplace connectivity
- Manually install critical extensions:
  - `ms-vscode-remote.remote-containers`
  - `ms-python.python`
  - `ms-vscode.vscode-typescript-next`

## 🎯 Benefits

1. **Zero Dependency Conflicts**: All tools and versions are containerized
2. **Consistent Environment**: Same setup across all developers and CI/CD
3. **Isolated Development**: No local system pollution
4. **Easy Onboarding**: New team members get full environment in minutes
5. **Service Integration**: PostgreSQL, Redis, and other services included
6. **Development Tools**: Pre-configured linting, formatting, and testing

## 📚 Additional Resources

- [Dev Containers Specification](https://containers.dev/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
