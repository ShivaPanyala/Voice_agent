from fastapi import FastAPI

from app.api.routes.messages import router as messages_router
from app.api.routes.business import router as business_router

app = FastAPI(
    title="AI Receptionist API",
    description="Backend for an AI-powered business receptionist.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "AI Receptionist API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(messages_router)
app.include_router(business_router)