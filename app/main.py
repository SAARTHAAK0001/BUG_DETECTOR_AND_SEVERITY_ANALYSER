from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.config import settings
from app.database import Base, engine, get_db
from app.llm_service import SeverityAnalyzer

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
analyzer = SeverityAnalyzer()


@app.get("/health")
def health():
    return {"status": "ok", "environment": settings.environment}


@app.post("/bugs/analyze", response_model=schemas.AnalyzeResponse)
def analyze_bug(payload: schemas.BugReportCreate, db: Session = Depends(get_db)):
    severity, model_used = analyzer.predict(payload.title, payload.description)
    bug = crud.create_bug_report(db, payload, severity, model_used)
    return {"bug": bug}


@app.get("/bugs/{bug_id}", response_model=schemas.BugReportResponse)
def read_bug(bug_id: int, db: Session = Depends(get_db)):
    bug = crud.get_bug_report(db, bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug report not found")
    return bug
