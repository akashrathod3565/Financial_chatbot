from fastapi import APIRouter
from httpx import request
from pydantic import BaseModel
from app.services.llm_service import generate_response

router = APIRouter()

class  QueryRequest(BaseModel):
    question: str
    
@router.post("/query")
def query_llm(request: QueryRequest):
    answer = generate_response(request.question)
    return {"answer": answer}