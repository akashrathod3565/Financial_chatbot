from fastapi import FastAPI
from app.routes.health import router as health_router
from app.core.config import settings
from app.routes.query import router as query_router 
from app.services.embedding_service import generate_embedding
from app.routes.upload import router as upload_router

app = FastAPI()
app.include_router(health_router)
app.include_router(query_router)
app.include_router(upload_router)

@app.get("/")
def root():
    vector = generate_embedding("Revenue increased by 12% in 2023.")
    return {
        "message":"Financial RAG API is running",
        "openai_api_key": settings.OPENAI_API_KEY is not None,
        "vector_length": len(vector)
            }