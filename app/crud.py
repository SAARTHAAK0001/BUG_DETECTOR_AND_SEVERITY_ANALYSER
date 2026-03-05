from sqlalchemy.orm import Session

from app import models, schemas


def create_bug_report(
    db: Session,
    payload: schemas.BugReportCreate,
    predicted_severity: str,
    model_used: str,
) -> models.BugReport:
    bug = models.BugReport(
        title=payload.title,
        description=payload.description,
        predicted_severity=predicted_severity,
        model_used=model_used,
    )
    db.add(bug)
    db.commit()
    db.refresh(bug)
    return bug


def get_bug_report(db: Session, bug_id: int) -> models.BugReport | None:
    return db.query(models.BugReport).filter(models.BugReport.id == bug_id).first()
