import os
from dotenv import load_dotenv
load_dotenv()

class settings:
    OPENAI_API_KEY:str = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY:str = os.getenv("PINECONE_API_KEY")
    PINECONE_HOST:str = os.getenv("PINECONE_HOST")

settings = settings()