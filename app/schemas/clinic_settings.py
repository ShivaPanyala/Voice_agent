from pydantic import BaseModel, Field


class ClinicSettingsUpdate(BaseModel):
    business_name: str = Field(min_length=1, max_length=150)
    address: str = Field(min_length=1)
    contact_number: str = Field(min_length=1, max_length=20)
    opening_hours: str = Field(min_length=1, max_length=200)
    services: list[str] = Field(min_length=1)


class ClinicSettingsResponse(BaseModel):
    id: int
    business_name: str
    address: str
    contact_number: str
    opening_hours: str
    services: list[str]

    model_config = {"from_attributes": True}