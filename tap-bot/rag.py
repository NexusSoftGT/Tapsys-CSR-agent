import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ✅ Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ TAPSYS Knowledge Base (FAQs)
documents = [
    "POS terminals are used for card payments.",
    "Settlement issues can occur due to network downtime.",
    "Transaction declines may happen due to insufficient funds.",
    "Reconciliation helps in matching transactions with bank records.",
    "POS system troubleshooting includes checking network and device status."
]

# ✅ Convert Text to Embeddings
doc_embeddings = np.array([model.encode(doc) for doc in documents])
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

def search_rag(query):
    """Searches RAG knowledge base for a relevant answer"""
    query_embedding = model.encode(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, 1)

    if distances[0][0] < 0.3:  # ✅ If relevant match found
        return documents[indices[0][0]]
    return None  # ❌ No good match, use LLM fallback
