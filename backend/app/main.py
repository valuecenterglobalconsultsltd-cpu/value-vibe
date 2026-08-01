from fastapi import FastAPI

app = FastAPI(
    title="Value Vibe API",
    version="1.0.0"
)


@app.get("/")
async def root():

    return {
        "application": "Value Vibe",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "database": "pending",
        "redis": "pending"
    }
