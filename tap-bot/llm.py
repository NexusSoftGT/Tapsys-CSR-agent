import requests
from config import GROQ_API_KEY

def query_llm(query):
    """Fallback to Groq LLM if RAG fails"""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are an expert in TAPSYS POS-related issues."},
            {"role": "user", "content": query}
        ]
    }
    
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No valid response.")
    return "Error in LLM API."
