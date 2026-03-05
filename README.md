Bug Detector and Severity Analyser

An AI-powered backend service that analyzes software bug reports and predicts their severity using large language model (LLM)–based classification.

The system is designed to support software engineering teams by automating part of the bug triaging process, enabling faster prioritization and more efficient issue management within development workflows.

This project demonstrates the integration of modern AI services with backend engineering practices, including modular architecture, API-driven design, and environment-based configuration.

Overview

In modern software development environments, teams receive large volumes of bug reports through testing pipelines, issue trackers, and user feedback systems. Manually reviewing and prioritizing these issues can slow down development cycles and introduce inconsistencies.

The Bug Detector and Severity Analyser provides an automated approach for analyzing bug descriptions and predicting severity levels such as low, medium, high, or critical.

The system can be integrated into Agile development workflows, CI/CD pipelines, and issue tracking platforms to support faster and more consistent issue prioritization.

Key Capabilities

Automated bug severity prediction using LLM-based analysis

FastAPI backend for scalable API deployment

Database integration for persistent bug storage

Modular architecture aligned with maintainable backend engineering practices

Environment-driven configuration for flexible deployment

Rule-based fallback classification when LLM services are unavailable

Project Structure
app/

├── main.py           # FastAPI application entry point
├── config.py         # Environment and configuration management
├── database.py       # Database initialization and connection
├── models.py         # ORM data models
├── schemas.py        # Pydantic schemas for request validation
├── crud.py           # Database interaction logic
└── llm_service.py    # LLM integration and severity prediction logic

requirements.txt
.gitignore
README.md

The architecture follows a separation-of-concerns design, enabling maintainability and scalability.

Installation
1. Clone the Repository
git clone https://github.com/SAARTHAAK0001/BUG_DETECTOR_AND_SEVERITY_ANALYSER.git
cd BUG_DETECTOR_AND_SEVERITY_ANALYSER
2. Create and Activate Virtual Environment
Linux / macOS
python -m venv .venv
source .venv/bin/activate
Windows
python -m venv .venv
.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the project root.

APP_NAME="Bug Detector and Severity Analyser"
ENVIRONMENT="development"
DATABASE_URL="sqlite:///./bugs.db"

LLM_PROVIDER="openai"
LLM_API_KEY=""

LLM_MODEL="gpt-4o-mini"
FALLBACK_SEVERITY="medium"

If the LLM_API_KEY is not provided, the system automatically switches to a rule-based fallback classifier.

Running the API

Start the application server:

uvicorn app.main:app --reload

Interactive API documentation is available at:

http://127.0.0.1:8000/docs
API Endpoints
Method	Endpoint	Description
GET	/health	Service health check
POST	/bugs/analyze	Analyze bug description and predict severity
GET	/bugs/{bug_id}	Retrieve stored bug report
Example Request
POST /bugs/analyze

Request body:

{
  "title": "Checkout fails with 500",
  "description": "Users cannot place orders. Payment request returns HTTP 500 in production."
}
Example Response
{
  "bug": {
    "id": 1,
    "title": "Checkout fails with 500",
    "description": "Users cannot place orders. Payment request returns HTTP 500 in production.",
    "predicted_severity": "high",
    "model_used": "rule-based-fallback",
    "created_at": "2026-01-01T10:00:00.000000"
  }
}
System Architecture Design

The Bug Detector and Severity Analyser follows a layered backend architecture designed for modularity, maintainability, and scalability.

The system separates responsibilities across API handling, business logic, LLM integration, and persistent storage.

Architecture Overview
Client Application
(Web / CLI / Issue Tracker Integration)
        │
        │ HTTP Requests
        ▼
FastAPI Backend
(app.main)
        │
        ▼
API Layer
(Request Validation - Pydantic Schemas)
        │
        ▼
Service Layer
(LLM Severity Prediction Logic)
        │
        ├── LLM Provider
        │   (OpenAI / Other Providers)
        │
        └── Rule-Based Fallback
            (Keyword Heuristics)
        │
        ▼
Data Access Layer
(CRUD Operations)
        │
        ▼
Database Layer
(SQLite / Future: PostgreSQL)
Architectural Principles

Separation of Concerns

API logic, database access, and LLM logic are separated into independent modules.

Scalability

The system allows replacement or extension of the LLM provider without modifying the core API.

Provider Flexibility

LLM providers can be changed through configuration variables.

Fail-Safe Design

If the LLM API fails or is unavailable, the system automatically switches to a rule-based classifier.

API Lifecycle Diagram

The API lifecycle describes the flow of a bug report from submission to severity prediction and storage.

Client Application
        │
        │ POST /bugs/analyze
        ▼
FastAPI Endpoint
(main.py)
        │
        ▼
Request Validation
(schemas.py)
        │
        ▼
Severity Analysis
(llm_service.py)
        │
        ├── LLM API Call
        │
        └── Rule-Based Fallback
        │
        ▼
Prediction Result
(predicted_severity)
        │
        ▼
Database Storage
(crud.py → models.py)
        │
        ▼
API Response
(JSON Response)
Lifecycle Steps

Client submits a bug report through the /bugs/analyze endpoint.

FastAPI receives the request and validates input using Pydantic schemas.

The request is passed to the severity analysis service.

The LLM provider processes the bug description and predicts severity.

If the LLM service is unavailable, the fallback rule-based classifier is used.

The predicted severity and bug details are stored in the database.

The API returns the structured response to the client.

Agile Workflow Integration

The Bug Detector and Severity Analyser is designed to support Agile software development practices by assisting with automated bug triaging and prioritization.

Bug Reporting Stage

When testers or users report bugs, the system can automatically analyze the issue description and assign a predicted severity level before the issue enters the product backlog.

Benefits include:

Faster bug triaging

Reduced manual classification

Consistent severity labels across reports

Sprint Planning

During sprint planning sessions, the predicted severity helps development teams prioritize issues effectively.

Examples:

Critical bugs affecting production systems

High-severity failures impacting key features

Low-severity cosmetic or UI issues

This improves decision-making during backlog grooming and sprint planning meetings.

CI/CD Pipeline Integration

The system can also integrate with automated testing pipelines.

Example workflow:

Automated Tests
        │
        ▼
Test Failure Report
        │
        ▼
Bug Severity Analyzer API
        │
        ▼
Severity Classification
        │
        ▼
Issue Creation in Tracker
(GitHub / Jira / Internal Tool)

This allows development teams to automatically prioritize bugs detected during continuous integration.

Development and Verification

Verify the project structure and syntax:

python -m compileall app

Verify the FastAPI application initialization:

python -c "from app.main import app; print(app.title)"
Future Enhancements

Potential improvements include:

Integration with GitHub Issues and Jira APIs

Training custom machine learning models using historical bug data

Analytical dashboards for bug severity trends

CI/CD pipeline automation

Support for multiple LLM providers and local inference models

License

This project is licensed under the MIT License.
