Bug Detector and Severity Analyser
Overview
An AI-powered backend service that analyzes software bug reports and predicts their severity using large language model (LLM)–based classification.

The system is designed to support software engineering teams by automating part of the bug triaging process, enabling faster prioritization and more efficient issue management within development workflows.

This project demonstrates the integration of modern AI services with backend engineering practices, including modular architecture, API-driven design, and environment-based configuration.

Key Capabilities
- Automated bug severity prediction using LLM-based analysis
- FastAPI backend for scalable API deployment
- Database integration for persistent bug storage
- Modular architecture aligned with maintainable backend engineering practices
- Environment-driven configuration for flexible deployment
- Rule-based fallback classification when LLM services are unavailable

Project Structure
app/

├── main.py           FastAPI application entry point
├── config.py         Environment and configuration management
├── database.py       Database initialization and connection
├── models.py         ORM data models
├── schemas.py        Pydantic schemas for request validation
├── crud.py           Database interaction logic
└── llm_service.py    LLM integration and severity prediction logic

requirements.txt
.gitignore
README.md

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

Create a .env file in the project root:

APP_NAME="Bug Detector and Severity Analyser"
ENVIRONMENT="development"
DATABASE_URL="sqlite:///./bugs.db"
LLM_PROVIDER="openai"
LLM_API_KEY=""
LLM_MODEL="gpt-4o-mini"
FALLBACK_SEVERITY="medium"

Running the API
Start the application server:

uvicorn app.main:app --reload

Interactive API documentation is available at:
http://127.0.0.1:8000/docs

API Endpoints
GET /health          Service health check
POST /bugs/analyze     Analyze bug description and predict severity
GET /bugs/{bug_id}     Retrieve stored bug report

Example Request
POST /bugs/analyze

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
The system follows a layered backend architecture designed for modularity and scalability.

Client Application
        │
        ▼
FastAPI Backend (main.py)
        │
        ▼
API Layer (Request Validation - Pydantic Schemas)
        │
        ▼
Service Layer (LLM Severity Prediction)
        │
        ├── LLM Provider (OpenAI or others)
        └── Rule-Based Fallback
        │
        ▼
Data Access Layer (CRUD Operations)
        │
        ▼
Database Layer (SQLite / PostgreSQL)

API Lifecycle
Client Application
        │
        │ POST /bugs/analyze
        ▼
FastAPI Endpoint
        │
        ▼
Request Validation
        │
        ▼
Severity Analysis (LLM Service)
        │
        ├── LLM API Call
        └── Rule-Based Fallback
        │
        ▼
Prediction Result
        │
        ▼
Database Storage
        │
        ▼
API Response

Agile Workflow Integration
Bug Reporting Stage
Bug reports submitted by testers or users can be automatically analyzed and assigned severity levels before entering the backlog.

Sprint Planning
Predicted severity levels help teams prioritize high-impact issues during backlog grooming and sprint planning.

CI/CD Integration
Automated testing pipelines can send failure reports to the API for severity classification, allowing automated issue prioritization in development workflows.

Future Enhancements
- Integration with GitHub Issues and Jira
- Training custom ML models using historical bug data
- Analytical dashboards for bug severity trends
- CI/CD pipeline automation
- Support for multiple LLM providers

License
MIT License
