# Development Guide

## Getting Started

### Prerequisites
- Python 3.12+ with Poetry
- Node.js 22+ with pnpm (via Corepack)
- Git with submodule support
- VS Code (recommended)

### Environment Setup

1. **Clone and initialize submodules:**
   ```bash
   git clone <repository-url>
   cd codex-meta-repo
   git submodule update --init --recursive
   ```

2. **Install dependencies:**
   ```bash
   make install
   # or manually:
   cd U-DIG-IT/backend && poetry install
   cd U-DIG-IT/frontend && pnpm install
   ```

3. **Configure environment:**
   ```bash
   cp U-DIG-IT/backend/env.example U-DIG-IT/backend/.env
   # Edit .env with your configuration
   ```

4. **Start development servers:**
   ```bash
   make dev
   # or manually:
   # Backend: cd U-DIG-IT/backend && poetry run uvicorn main:app --reload
   # Frontend: cd U-DIG-IT/frontend && pnpm dev
   ```

## Development Workflow

### Code Quality Standards

#### Python (Backend)
- **Formatting**: Black with 88-character line length
- **Import sorting**: isort with black profile
- **Linting**: flake8 with custom rules
- **Type checking**: mypy with strict mode
- **Security**: bandit and safety checks

#### TypeScript (Frontend)
- **Formatting**: Prettier (via ESLint)
- **Linting**: ESLint with security plugins
- **Type checking**: TypeScript strict mode
- **Testing**: Vitest with React Testing Library

### Pre-commit Hooks

The repository includes pre-commit hooks that run automatically:

1. **Secret scanning** with GitLeaks
2. **Frontend linting** and testing
3. **Backend security checks** with Safety
4. **Unit tests** for both frontend and backend

### Testing Strategy

#### Backend Testing
```bash
# Run all tests
cd U-DIG-IT/backend && poetry run pytest

# Run with coverage
cd U-DIG-IT/backend && poetry run pytest --cov=app --cov-report=html

# Run specific test types
cd U-DIG-IT/backend && poetry run pytest tests/unit/
cd U-DIG-IT/backend && poetry run pytest tests/integration/
```

#### Frontend Testing
```bash
# Run all tests
cd U-DIG-IT/frontend && pnpm test

# Run with coverage
cd U-DIG-IT/frontend && pnpm test:ci

# Run tests in watch mode
cd U-DIG-IT/frontend && pnpm test:watch
```

### Security Practices

#### Secret Management
- Never commit secrets to version control
- Use environment variables for all sensitive data
- Rotate secrets regularly
- Use strong, unique secrets (minimum 32 characters)

#### Security Scanning
```bash
# Run secret scanning
make security:scan

# Check for vulnerable dependencies
make security:check

# Run security linting
cd U-DIG-IT/backend && poetry run bandit -r app/
```

### Code Review Process

1. **Create feature branch** from main
2. **Write tests** for new functionality
3. **Run quality checks** locally
4. **Create pull request** with detailed description
5. **Address review feedback**
6. **Merge after approval** and CI passes

### Architecture Guidelines

#### Backend (FastAPI)
- **Models**: SQLModel for database entities
- **Schemas**: Pydantic for API validation
- **Routers**: Modular API endpoints
- **Services**: Business logic separation
- **Dependencies**: Dependency injection for database and auth

#### Frontend (React)
- **Components**: Reusable UI components
- **Hooks**: Custom hooks for data fetching
- **Context**: Global state management
- **Pages**: Route-level components
- **Types**: Shared TypeScript definitions

### Performance Considerations

#### Backend
- Database query optimization
- Connection pooling
- Caching strategies
- Async/await patterns

#### Frontend
- Code splitting
- Lazy loading
- Image optimization
- Bundle size monitoring

### Monitoring and Observability

#### Logging
- Structured logging with correlation IDs
- Different log levels for different environments
- Error tracking with Sentry

#### Metrics
- API response times
- Database query performance
- Frontend bundle size
- Test coverage metrics

### Deployment

#### Development
- Local development with hot reload
- Docker containers for consistency
- Environment-specific configurations

#### Production
- Containerized deployment
- Secret management
- Health checks
- Monitoring and alerting

## Troubleshooting

### Common Issues

#### Backend Issues
- **Database connection**: Check DATABASE_URL in .env
- **JWT errors**: Verify JWT_SECRET is set and valid
- **Import errors**: Ensure virtual environment is activated

#### Frontend Issues
- **API connection**: Check VITE_API_BASE_URL
- **Build errors**: Clear node_modules and reinstall
- **Type errors**: Run TypeScript compiler to check types

#### Testing Issues
- **Test failures**: Check test database configuration
- **Coverage issues**: Ensure all code paths are tested
- **Mock issues**: Verify mock implementations

### Getting Help

1. **Check documentation** in `/docs` directory
2. **Search existing issues** in GitHub
3. **Create new issue** with detailed description
4. **Contact team** via Slack or email

## Contributing

### Code Style
- Follow existing patterns and conventions
- Write clear, self-documenting code
- Add comments for complex logic
- Update documentation for API changes

### Testing Requirements
- Unit tests for all new functionality
- Integration tests for API endpoints
- Frontend tests for user interactions
- Security tests for authentication flows

### Documentation
- Update README files for significant changes
- Add API documentation for new endpoints
- Include examples in code comments
- Maintain architecture diagrams

