flowchart LR
    A[Commit Code] --> B[Push to GitHub]
    B --> C[Trigger GitHub Actions CI]
    C --> D[Run Automated Tests]
    D -- Tests Pass --> E[Build Docker Image]
    D -- Tests Fail --> F[Notify Failure (Slack/Email)]
    E --> G[Deploy to Staging]
    G --> H[Run Integration Tests]
    H -- Tests Pass --> I[Deploy to Production]
    H -- Tests Fail --> F
    I --> J[Notify Success (Slack/Email)]
