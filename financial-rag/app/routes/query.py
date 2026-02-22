from fastapi import APIRouter
from httpx import request
from pydantic import BaseModel
from app.services.rag_service import generate_rag_answer

router = APIRouter()

class  QueryRequest(BaseModel):
    question: str
    
@router.post("/query")
def query_llm(request: QueryRequest):
    answer = generate_rag_answer(request.question)
    return {"answer": answer}