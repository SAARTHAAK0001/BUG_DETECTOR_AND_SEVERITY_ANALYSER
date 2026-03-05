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


