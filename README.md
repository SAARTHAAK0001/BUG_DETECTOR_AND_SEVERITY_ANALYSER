# Bug Detector and Severity Analyser

An AI-powered backend system that analyzes bug reports and predicts their severity using LLM-based classification.

---

## Features

- LLM-based bug severity prediction
- Structured FastAPI backend
- Database integration
- Environment-based configuration
- Clean project structure

---

## Project Structure
app/

│

├── main.py # FastAPI entry point

├── config.py # Environment configuration

├── database.py # Database setup

├── models.py # ORM models

├── schemas.py # Pydantic schemas

├── crud.py # Database operations

└── llm_service.py # LLM integration logic

requirements.txt
.gitignore
README.md

---

## Installation

### 1️) Clone the repository

```bash
git clone https://github.com/SAARTHAAK0001/BUG_DETECTOR_AND_SEVERITY_ANALYSER.git
cd BUG_DETECTOR_AND_SEVERITY_ANALYSER
```

### 2) Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment

Create `.env` in project root:

```env
APP_NAME="Bug Detector and Severity Analyser"
ENVIRONMENT="development"
DATABASE_URL="sqlite:///./bugs.db"
LLM_PROVIDER="openai"
LLM_API_KEY=""
LLM_MODEL="gpt-4o-mini"
FALLBACK_SEVERITY="medium"
```

> If `LLM_API_KEY` is empty, app automatically uses rule-based fallback.

## Run the API

```bash
uvicorn app.main:app --reload
```

Open interactive docs: `http://127.0.0.1:8000/docs`

## API Endpoints

- `GET /health`
- `POST /bugs/analyze`
- `GET /bugs/{bug_id}`

### Example request

```bash
curl -X POST "http://127.0.0.1:8000/bugs/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Checkout fails with 500",
    "description": "Users cannot place orders. Payment request returns HTTP 500 in production."
  }'
```

### Example response

```json
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
```

## Quick checks

```bash
python -m compileall app
python -c "from app.main import app; print(app.title)"
```


## System Architecture Design
The system follows a layered backend architecture designed for modularity and scalability.

Client Application
'''
        │
        ▼
'''       
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


## API Lifecycle
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


## Agile Workflow Integration
Bug Reporting Stage
Bug reports submitted by testers or users can be automatically analyzed and assigned severity levels before entering the backlog.

Sprint Planning
Predicted severity levels help teams prioritize high-impact issues during backlog grooming and sprint planning.

CI/CD Integration
Automated testing pipelines can send failure reports to the API for severity classification, allowing automated issue prioritization in development workflows.


## Future Enhancements
- Integration with GitHub Issues and Jira
- Training custom ML models using historical bug data
- Analytical dashboards for bug severity trends
- CI/CD pipeline automation
- Support for multiple LLM providers


## License
MIT License
