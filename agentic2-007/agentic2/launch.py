import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["/workspaces/agentic2-20250516T181724Z-1-001/agentic2/app"]
    )