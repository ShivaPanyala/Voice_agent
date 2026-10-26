from fastapi import APIRouter

from app.services.business_service import get_business_info

router = APIRouter(prefix="/business-info", tags=["Business Information"])


@router.get("/")
def business_info():
    return get_business_info()