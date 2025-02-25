import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ✅ Load Sentence Transformer Model for Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")  # Lightweight & fast

# ✅ POS Queries Knowledge Base (Add More POS-Related Data)
documents = [
    "POS terminals are used for card payments.",
    "Settlement issues can occur due to network downtime.",
    "Transaction declines may happen due to insufficient funds.",
    "Reconciliation helps in matching transactions with bank records.",
    "POS system troubleshooting includes checking network and device status."
]

# ✅ Convert Text to Embeddings
doc_embeddings = np.array([model.encode(doc) for doc in documents])

# ✅ Create FAISS Index
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

# ✅ Save FAISS Index
faiss.write_index(index, "pos_faiss.index")
np.save("pos_documents.npy", documents)

print("✅ POS Knowledge Base Stored!")
