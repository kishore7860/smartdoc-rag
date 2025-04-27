# src/backend/rag_pipeline.py

from src.models.embedder import Embedder
from src.backend.vector_store import VectorStore
from src.models.llm import LLM

class RAGPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()
        self.llm = LLM()

    def ingest_documents(self, documents):
        """Add new documents to the vector database."""
        self.vector_store.add_documents(documents)

    def query(self, user_question: str):
        # Step 1: Embed the question
        query_embedding = self.embedder.embed_text(user_question)
        
        # Step 2: Retrieve relevant chunks
        relevant_chunks = self.vector_store.retrieve(query_embedding)
        
        if not relevant_chunks:
            return "❌ Sorry, I couldn't find any relevant information in the uploaded documents."

        # Step 3: Build a nice prompt
        context = "\n\n".join([chunk['text'] for chunk in relevant_chunks])
        prompt = (
            f"You are a helpful assistant. Use the following context to answer the question.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {user_question}\n\n"
            f"Answer:"
        )

        # Step 4: Get LLM response
        answer = self.llm.generate(prompt)
        return answer