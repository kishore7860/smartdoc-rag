# app/backend/vector_store.py

class VectorStore:
    def __init__(self):
        # Temporary: hardcode some sample document chunks
        self.documents = [
            {"text": "The Transformer architecture was introduced in 2017 by Vaswani et al."},
            {"text": "Pinecone is a vector database for semantic search applications."},
            {"text": "LangChain is a framework for developing LLM-powered apps."}
        ]

    def retrieve(self, query_embedding):
        # ⚡ MVP: Return all documents blindly for now
        # Later: use real similarity search with Pinecone or Chroma
        return self.documents