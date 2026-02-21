from fastapi import FastAPI
from app.routes.health import router as health_router
from app.core.config import settings
from app.routes.query import router as query_router 

app = FastAPI()
app.include_router(health_router)
app.include_router(query_router)

@app.get("/")
def root():
    return {
        "message":"Financial RAG API is running",
        "openai_api_key": settings.OPENAI_API_KEY is not None
            }