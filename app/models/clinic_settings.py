from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class ClinicSettings(Base):
    __tablename__ = "clinic_settings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    business_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        default="ABC Clinic",
    )

    address: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="Update with your actual clinic address",
    )

    contact_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="Update with your actual clinic phone number",
    )

    opening_hours: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        default="Monday to Saturday, 9:00 AM to 6:00 PM",
    )

    services: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="General consultation, Appointment enquiries, Clinic information",
    )