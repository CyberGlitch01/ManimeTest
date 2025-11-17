# Base image (Python with devcontainer support)
FROM mcr.microsoft.com/devcontainers/python:3.10

# Switch to root for system installs
USER root

# Install all system dependencies for Manim
RUN apt-get update && apt-get install -y \
    ffmpeg libcairo2 libcairo2-dev libpango1.0-dev \
    libffi-dev libxml2 libxslt1.1 libgl1 libgl1-mesa-dev \
    libglfw3 libgles2-mesa-dev pkg-config \
    texlive texlive-latex-extra texlive-fonts-extra \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch back to non-root user
USER vscode

# Set working directory
WORKDIR /workspace

# Preinstall Manim
RUN pip install --no-cache-dir -U pip setuptools wheel manim

# Default command
CMD ["bash"]
