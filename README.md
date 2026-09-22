# azure-pipelines-real-world
Real-World Multi-Stage Azure Pipeline
# Azure Pipelines Real-World CI/CD Project

## Overview

This project demonstrates how to build a simple multi-stage CI/CD pipeline using Azure Pipelines.

The pipeline automatically builds, tests, packages, and deploys a Python Flask application to Azure App Service.

The main goal of the project is to learn how Azure Pipelines can automate application delivery from source code to staging and production environments.

## Pipeline Workflow

```text
Git Push
   ↓
Build
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Create Deployment Artifact
   ↓
Deploy to Staging
   ↓
Production Approval
   ↓
Deploy to Production
```

## Technologies Used

* Azure DevOps
* Azure Pipelines
* YAML
* Python
* Flask
* Pytest
* Azure App Service
* Azure DevOps Environments
* Variable Groups
* Azure Service Connections

## Project Structure

```text
azure-pipelines-real-world/
│
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
├── azure-pipelines.yml
└── README.md
```

## Pipeline Stages

### Build

The Build stage:

* Checks out the source code
* Configures Python
* Installs application dependencies
* Runs automated tests
* Packages the application
* Publishes the application as a pipeline artifact

### Deploy to Staging

The staging stage downloads the artifact created during the Build stage and deploys it to an Azure App Service staging environment.

### Deploy to Production

The production stage uses an Azure DevOps Environment with manual approval.

Once the deployment is approved, the same application artifact that was tested in staging is deployed to production.

## Important Azure Pipelines Concepts

This project demonstrates several important Azure Pipelines concepts:

* Triggers
* Microsoft-hosted agents
* Stages
* Jobs
* Steps
* Tasks
* Variables
* Variable Groups
* Pipeline Artifacts
* Service Connections
* Deployment Jobs
* Environments
* Manual Approvals

## Running the Application Locally

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
pytest -v
```

Start the application:

```bash
python app.py
```

The application runs on:

```text
http://localhost:8000
```

Test the health endpoint:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

## Running the Pipeline

After configuring the Azure service connection, variable group, and Azure DevOps environments, commit and push the project:

```bash
git add .
git commit -m "Create Azure Pipelines CI/CD project"
git push origin main
```

A push to the `main` branch automatically triggers the pipeline.

## Troubleshooting Practiced

During this project, common Azure Pipelines issues can be investigated, including:

* Pipeline trigger failures
* YAML syntax errors
* Failed unit tests
* Missing pipeline artifacts
* Unauthorized service connections
* Unauthorized variable groups
* Incorrect deployment package paths
* Failed Azure App Service deployments
* Production deployments waiting for approval

## Key Learning Outcome

This project demonstrates how Azure Pipelines can act as the automation layer between source control and Azure resources.

The final workflow is:

```text
Developer
   ↓
Git
   ↓
Azure Pipelines
   ↓
Build and Test
   ↓
Pipeline Artifact
   ↓
Staging
   ↓
Approval
   ↓
Production
```

The project also demonstrates the important CI/CD practice of **building an application once and promoting the same tested artifact through multiple environments**.
