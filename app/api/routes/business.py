from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.clinic_settings import (
    ClinicSettingsUpdate,
    ClinicSettingsResponse,
)
from app.services.business_service import (
    get_business_info,
    update_business_info,
)

router = APIRouter(prefix="/business-info", tags=["Business Information"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=ClinicSettingsResponse | dict)
def read_business_info(db: Session = Depends(get_db)):
    try:
        return get_business_info(db)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve clinic information.",
        ) from exc


@router.put("/", response_model=ClinicSettingsResponse | dict)
def edit_business_info(
    payload: ClinicSettingsUpdate,
    db: Session = Depends(get_db),
):
    try:
        return update_business_info(payload, db)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to update clinic information.",
        ) from exc