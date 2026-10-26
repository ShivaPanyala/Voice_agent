BUSINESS_INFO = {
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


def get_business_info() -> dict:
    return BUSINESS_INFO.copy()