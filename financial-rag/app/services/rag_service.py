from app.services.embedding_service import generate_embedding
from app.services.vector_service import retrieve_similar_chunks
from app.services.llm_service import generate_response


def generate_rag_answer(question: str) -> str:
    # 1️⃣ Generate embedding for question
    query_embedding = generate_embedding(question)

    # 2️⃣ Retrieve relevant chunks
    contexts = retrieve_similar_chunks(query_embedding)

    # 3️⃣ Build structured context block
    context_text = "\n\n".join(contexts)

    enhanced_prompt = f"""
You are a financial research assistant.

Use ONLY the context below to answer the question.
If the answer is not found in the context, say "Information not available in provided documents."

Context:
{context_text}

Question:
{question}
"""

    # 4️⃣ Generate grounded answer
    return generate_response(enhanced_prompt)