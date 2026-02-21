from app.core.openai_client import client

def generate_response(question: str) -> str:
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages=[
            {"role": "system","content": "You are a helpful financial research assistant for financial queries."},
            {"role": "user","content": question}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content