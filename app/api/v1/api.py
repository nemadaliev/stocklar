from fastapi import APIRouter

from app.api.v1.endpoints import list, halal

api_router = APIRouter()

api_router.include_router(list.router, prefix="/list", tags=["list"])
api_router.include_router(halal.router, prefix="/halal", tags=["halal"])
