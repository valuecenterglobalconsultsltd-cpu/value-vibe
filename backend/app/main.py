from fastapi import FastAPI

app = FastAPI(
    title="Value Vibe API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "application": "Value Vibe",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
