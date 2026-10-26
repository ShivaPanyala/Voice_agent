from sqlalchemy.orm import Session

from app.models.clinic_settings import ClinicSettings


DEFAULT_SETTINGS = {
    "business_name": "ABC Clinic",
    "opening_hours": "Monday to Saturday, 9:00 AM to 6:00 PM",
    "address": "Update with your actual clinic address",
    "contact_number": "Update with your actual clinic phone number",
    "services": [
        "General consultation",
        "Appointment enquiries",
        "Clinic information",
    ],
}


def get_business_info(db: Session) -> dict:
    settings = db.query(ClinicSettings).first()

    if settings is None:
        return DEFAULT_SETTINGS.copy()

    return {
        "business_name": settings.business_name,
        "opening_hours": settings.opening_hours,
        "address": settings.address,
        "contact_number": settings.contact_number,
        "services": [
            service.strip()
            for service in settings.services.split(",")
            if service.strip()
        ],
    }


def update_business_info(payload, db: Session) -> dict:
    settings = db.query(ClinicSettings).first()

    services_text = ", ".join(
        service.strip()
        for service in payload.services
        if service.strip()
    )

    if not services_text:
        raise ValueError("At least one clinic service is required.")

    if settings is None:
        settings = ClinicSettings()
        db.add(settings)

    settings.business_name = payload.business_name.strip()
    settings.address = payload.address.strip()
    settings.contact_number = payload.contact_number.strip()
    settings.opening_hours = payload.opening_hours.strip()
    settings.services = services_text

    db.commit()
    db.refresh(settings)

    return get_business_info(db)