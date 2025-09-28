FROM mcr.microsoft.com/devcontainers/python:3.12

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        wget \
        git \
        build-essential \
        libssl-dev \
        libffi-dev \
        postgresql-client \
        redis-tools \
        docker.io \
        docker-compose \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI and expose compose plugin to the new CLI
ARG DOCKER_CLI_VERSION=27.1.1
RUN curl -fsSL "https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_CLI_VERSION}.tgz" -o /tmp/docker.tgz \
    && tar -xz -C /usr/local/bin --strip-components=1 -f /tmp/docker.tgz docker/docker \
    && rm /tmp/docker.tgz \
    && mkdir -p /usr/local/lib/docker/cli-plugins \
    && ln -sf /usr/bin/docker-compose /usr/local/lib/docker/cli-plugins/docker-compose

# Install Node.js, npm, and pnpm (skip yarn to avoid binary collision during build)
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get update \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g pnpm@latest \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry in a shared location
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - \
    && ln -sf /opt/poetry/bin/poetry /usr/local/bin/poetry

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Ensure the vscode user exists and can access the Docker socket
RUN if ! id -u vscode >/dev/null 2>&1; then \
      useradd -m -s /bin/bash vscode; \
    fi \
    && usermod -aG docker vscode

# Set up Python virtual environment and install Python dependencies
USER vscode
WORKDIR /home/vscode

# Create and activate virtual environment
RUN python3 -m venv ~/.venv \
    && echo 'source ~/.venv/bin/activate' >> ~/.bashrc

# Install Python development tools
RUN ~/.venv/bin/pip install --upgrade pip setuptools wheel \
    && ~/.venv/bin/pip install black isort flake8 mypy pytest pytest-cov

# Set up workspace
WORKDIR /workspaces/codex-meta-repo

# Expose ports for common development servers
EXPOSE 3000 4173 8000 8080 5432 6379

# Default command
CMD ["sleep", "infinity"]
