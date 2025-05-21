# app/api/summarize.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.summarizer import summarize_text

router = APIRouter()

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str

@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text)
    return SummarizeResponse(summary=summary)
