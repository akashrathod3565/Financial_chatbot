from app.core.pinecone_client import index

def upsert_vector(
        vector_id:str,
        embedding:list[float],
        text:str,
        source: str = 'unknown'
):
    index.upsert(
        vectors=[
            {
                'id': vector_id,
                'values': embedding,
                'metadata':{
                    'text': text,
                    'source':source
                }
            }
        ]
    )

def retrieve_similar_chunks(
        query_embedding:list[float],
        top_k: int = 3,
) -> list[str]:
    
    response = index.query(
        vector=query_embedding,
        top_k = top_k,
        include_metadata=True
) 
    results = []
    for match in response["matches"]:
        results.append(match['metadata']['text'])
    

    return results