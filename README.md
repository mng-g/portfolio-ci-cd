# CI/CD Pipeline for Python Web API 🚀  

![CI Build](https://github.com/mng-g/portfolio-ci-cd/actions/workflows/ci.yml/badge.svg)[![codecov](https://codecov.io/gh/mng-g/portfolio-ci-cd/branch/main/graph/badge.svg)](https://codecov.io/gh/mng-g/portfolio-ci-cd)![GitHub release (latest by date)](https://img.shields.io/github/v/release/mng-g/portfolio-ci-cd)  

<img src="https://www.mabl.com/hubfs/CICDBlog.png" width="100">  

This repository showcases an **end-to-end CI/CD pipeline** for a **Python web backend API**, integrating **GitHub Actions, Docker, Kubernetes, and ArgoCD**. The goal is to demonstrate **GitOps-driven automation**, best practices in **Continuous Integration (CI)** and **Continuous Deployment (CD)**.

## Overview  

### Features:  

- **Application:** A simple Python web app that returns a message and a status.  
- **CI/CD Workflow:**  
  - **GitHub Actions**  
    - `ci.yml`: Runs tests and attempts a build on `feature/*`, `bugfix/*`, and `release-*` branches, or on PRs to `main`.  
    - `push-image.yml`: Builds the Docker image, runs security scans, and pushes to **GitHub Container Registry (GHCR)**.  
  - **ArgoCD**  
    - Automates deployments using **GitOps**.  
    - Manifests, Helm values, and template files are stored in the `deploy/` directory.  
- **Containerization:** Uses **Docker** for consistency across environments.  
- **Orchestration:** Kubernetes manages workloads for **scalable deployment**.  

## Repository Structure  

```
portfolio-ci-cd/
├── .github/
│   ├── workflows/               # CI/CD GitHub Actions workflows
│   ├── ISSUE_TEMPLATE           # Issue templates for new issues
│   ├── dependabot.yml           # Automates dependency updates
│   └── PULL_REQUEST_TEMPLATE.md # PR template
├── deploy/
│   ├── helm/                    # Helm charts for Kubernetes deployments
│   ├── k8s/                     # Kubernetes manifests
├── Dockerfile                   # Dockerfile to containerize the application
├── docs/                        # Documentation and pipeline diagrams
│   ├── development_workflow.md
│   ├── pipeline_design.md
│   ├── pipeline_diagram.md
│   └── versioning.md
├── requirements.txt             # Python dependencies
├── src/                         # Python application source code
├── tests/                       # Unit and integration tests
└── .gitignore                   # Ignore file
```

## Branching Strategy  

We follow a **trunk-based development** approach:  

- **`main`**: Production-ready code.  
- **`feature/*`**: New features in development.  
- **`release-*`**: Stabilization branches for upcoming releases.  
- **`bugfix/*`**: Fixes applied to `release-*` branches before merging to `main`.  

📌 **See [`docs/development_workflow.md`](docs/development_workflow.md) for details.**  

## CI/CD Pipeline  

The **CI/CD pipeline** (`docs/pipeline_diagram.md`) includes:  

1. **CI Pipeline (`ci.yml`)**:  
   - Runs **automated tests** on every push.  
   - Attempts to **build the Docker image** on specified branches and PRs.  
2. **Image Build & Push (`push-image.yml`)**:  
   - Builds a **secure Docker image**.  
   - Scans for vulnerabilities.  
   - Pushes the image to **GHCR**.  
3. **CD Pipeline (ArgoCD)**:  
   - Deploys the application to **staging** and **production** environments.  
   - Manages **Kubernetes manifests and Helm charts** in `deploy/`.  
   - Uses **GitOps** principles for deployment consistency.  

## Deployment  

Deployment can be managed using **[devops-ready-cluster](https://github.com/mng-g/devops-ready-cluster)**:  

1. **Set up a cluster**:  
   ```bash
   git clone https://github.com/mng-g/devops-ready-cluster.git
   devops-ready-cluster create-cluster --name <CLUSTER_NAME>
   ```
2. **Install required components**:  
   ```bash
   devops-ready-cluster install-metrics
   devops-ready-cluster install-ingress
   devops-ready-cluster install-metallb
   devops-ready-cluster install-argocd
   ```
3. **Set up ArgoCD access**:  
   - Retrieve the initial ArgoCD admin password.  
   - If the repository is private, add a new **repository connection** in ArgoCD:  
     - **Repo URL:** `https://github.com/mng-g/portfolio-ci-cd.git`  
     - **Username:** `mng-g`  
     - **GH_PAT:** _GitHub Personal Access Token (with repo access)_  

4. **Deploy the application**:  
   ```bash
   # ArgoCD rollout are required
   helm repo add argo https://argoproj.github.io/argo-helm
   helm repo update
   helm upgrade --install argo-rollouts argo/argo-rollouts -n argocd --create-namespace

   kubectl apply -f deploy/k8s/staging
   kubectl apply -f deploy/k8s/prod
   ```

5. **Create a secret for pulling the image (REQUIRED ONLY IF THE IMAGE IS PRIVATE)**:  
   ```bash
   kubectl create secret docker-registry ghcr-secret \
     --docker-server=ghcr.io \
     --docker-username=mng-g \
     --docker-password=<GH_PAT> \
     --docker-email=mingazzini.michael@gmail.com -n flask-app-staging

   kubectl create secret docker-registry ghcr-secret \
     --docker-server=ghcr.io \
     --docker-username=mng-g \
     --docker-password=<GH_PAT> \
     --docker-email=mingazzini.michael@gmail.com -n flask-app-prod
   ```

6. **Update DNS or `/etc/hosts`**:  
   ```
   <ingress-controller-IP> flask-app.local
   <ingress-controller-IP> staging.flask-app.local
   ```

## Running Locally  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/mng-g/portfolio-ci-cd.git
   ```
2. **Switch to a new feature branch**:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Install dependencies**:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pytest
   pip install -r requirements.txt
   ```
4. **Run tests**:  
   ```bash
   pytest tests/
   ```
