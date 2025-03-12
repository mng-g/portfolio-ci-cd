```mermaid
flowchart TD
    A[Commit Code & Push to GitHub] --> B[Checkout Code]
    B --> C[Linting]
    C --> D[Run Unit & Integration Tests]
    D --> E{Tests Pass?}
    E -- Yes --> F[Build Docker Image]
    E -- No --> G["Notify Failure (Slack/Email)"]
    F --> H[Run Static Analysis & Security Scans]
    H --> I{Quality Checks Pass?}
    I -- Yes --> J[Package & Tag Artifact]
    I -- No --> G
    J --> K[Deploy to Staging]
    K --> L[Run Post-Deployment Tests]
    L --> M{Staging OK?}
    M -- Yes --> N[Deploy to Production]
    M -- No --> G
    N --> O["Notify Success (Slack/Email)"]
```

### How It Works
1. **Commit & Push:** The pipeline is triggered when code is committed and pushed to GitHub.
2. **Checkout:** The CI system checks out the code.
3. **Linting:** Code quality is enforced through linting.
4. **Testing:** Unit and integration tests run, with a decision node ensuring that failures are caught early.
5. **Build:** If tests pass, the Docker image is built.
6. **Static Analysis & Security:** The built image undergoes static analysis and security scans.
7. **Quality Gate:** A decision node checks whether quality metrics (e.g., code coverage, analysis results) meet the set standards.
8. **Packaging:** Successful quality checks lead to packaging and artifact tagging.
9. **Staging Deployment:** The artifact is deployed to a staging environment, where post-deployment tests run.
10. **Production Deployment:** Upon successful staging tests, the artifact is deployed to production.
11. **Notifications:** The pipeline notifies success or failure via Slack/Email.