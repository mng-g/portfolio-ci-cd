# Portfolio CI/CD

![CI Build](https://github.com/mng-g/portfolio-ci-cd/actions/workflows/ci.yml/badge.svg)[![codecov](https://codecov.io/gh/mng-g/portfolio-ci-cd/branch/main/graph/badge.svg)](https://codecov.io/gh/mng-g/portfolio-ci-cd)![GitHub release (latest by date)](https://img.shields.io/github/v/release/mng-g/portfolio-ci-cd)



<img src="https://www.mabl.com/hubfs/CICDBlog.png" width="100">

This repository demonstrates an end-to-end CI/CD pipeline for a simple Python web backend API. The goal is to showcase best practices in continuous integration and continuous delivery using GitHub Actions, Docker and Kubernetes.

## Overview

- **Application:** A simple Python app that prints a message and the status.
- **CI/CD Tools:** GitHub Actions for automated testing, building, and pushing to docker images to ghcr. ArgoCD for deployment.
- **Containerization:** Docker is used to package the application for consistency across environments.
- **???:** Kubernetes is used for ...

## Repository Structure

```
portfolio-ci-cd/
├── .github/
│   ├── workflows/               # CI/CD GitHub Actions workflows to build and push the docker image on ghcr
│   ├── ISSUE_TEMPLATE           # Issue templates for new issues
│   ├── dependabot.yml           # Dependabot automates dependency updates in GitHub repositories for security.
│   └── PULL_REQUEST_TEMPLATE.md # Pull request template
├── deploy
│   ├── helm
│   └── k8s
├── Dockerfile                   # Dockerfile to containerize the application
├── docs                         # Documentation and pipeline diagrams
│   ├── development_workflow.md
│   ├── pipeline_design.md
│   ├── pipeline_diagram.md
│   └── versioning.md
├── requirements.txt             # Python dependencies
├── src                          # Python application source code
├── tests                        # Unit and integration tests
└── .gitignore                   # Git ignore file
```

## Branching Strategy

- **main:** Contains production-ready code.
- **develop:** Integration branch where features are merged and tested.
- **feature/\*** and **bugfix/\***: For individual features and bug fixes, respectively.

## CI/CD Pipeline

The CI/CD pipeline (detailed in `docs/pipeline_diagram.md`) will:

1. Run automated tests on every push.
2. Build a Docker image upon successful tests.
3. Deploy the container to a staging or production environment.
4. Send notifications on build and deploy events.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/portfolio-ci-cd.git
   ```
2. **Create and switch to a feature branch:**
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run tests:**
   ```bash
   pytest tests/
   ```

## Next Steps

- **Branch Protection:** Branch rules (including pull request requirements) are configured to enforce best practices.
- **Pipeline Setup:** GitHub Actions workflows are set up for CI and CD.
- **Documentation:** Further documentation is available in the `docs/` folder.

Feel free to open issues or pull requests if you have suggestions or improvements!