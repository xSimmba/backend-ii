# app/main.py
from fastapi import FastAPI
from app.api import router as api_router
from app.api.summarize import router as summarize_router 

app = FastAPI(title="Agentic AI Backend")
app.include_router(api_router)
app.include_router(summarize_router, prefix="/api")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)