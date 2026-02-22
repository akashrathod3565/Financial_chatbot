from fastapi import APIRouter, UploadFile, File
from app.services.ingestion_service import ingest_file

router = APIRouter()

@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    ingest_file(file)
    return {"message": f"{file.filename} ingested successfully"}