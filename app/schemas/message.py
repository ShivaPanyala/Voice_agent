from pydantic import BaseModel, ConfigDict, Field


class MessageCreate(BaseModel):
    caller_name: str = Field(min_length=2, max_length=100)
    caller_phone: str = Field(min_length=7, max_length=20)
    message: str = Field(min_length=2, max_length=2000)


class MessageResponse(BaseModel):
    id: int
    caller_name: str
    caller_phone: str
    message: str

    model_config = ConfigDict(from_attributes=True)