# app/api/__init__.py
from fastapi import APIRouter
from .summarize import router as summarize_router

router = APIRouter()
router.include_router(summarize_router, prefix="/api")
