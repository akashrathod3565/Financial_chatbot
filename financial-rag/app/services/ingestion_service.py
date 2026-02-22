import uuid
from pypdf import PdfReader
from fastapi import UploadFile

from app.services.embedding_service import generate_embedding
from app.services.vector_service import upsert_vector


def extract_text_from_pdf(file: UploadFile) -> str:
    reader = PdfReader(file.file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text


def chunk_text(text: str, chunk_size: int = 600, overlap: int = 50):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def ingest_file(file: UploadFile):
    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)

    for chunk in chunks:
        vector_id = str(uuid.uuid4())
        embedding = generate_embedding(chunk)

        upsert_vector(
            vector_id=vector_id,
            embedding=embedding,
            text=chunk,
            source=file.filename
        )