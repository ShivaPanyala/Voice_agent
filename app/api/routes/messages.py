from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageResponse

router = APIRouter(prefix="/messages", tags=["Messages"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MessageResponse, status_code=201)
def create_message(
    payload: MessageCreate,
    db: Session = Depends(get_db),
):
    try:
        message = Message(
            caller_name=payload.caller_name.strip(),
            caller_phone=payload.caller_phone.strip(),
            message=payload.message.strip(),
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Unable to save the message.",
        ) from exc


@router.get("/", response_model=list[MessageResponse])
def get_messages(
    db: Session = Depends(get_db),
):
    try:
        messages = (
            db.query(Message)
            .order_by(Message.id.desc())
            .all()
        )
        return messages

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve messages.",
        ) from exc
