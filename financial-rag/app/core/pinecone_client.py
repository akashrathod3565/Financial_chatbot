from pinecone import Pinecone
from app.core.config import settings

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

index = pc.Index(host=settings.PINECONE_HOST)