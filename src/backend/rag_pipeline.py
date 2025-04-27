# src/backend/rag_pipeline.py

from src.models.embedder import Embedder
from src.backend.vector_store import VectorStore
from src.models.llm import LLM
# src/backend/rag_pipeline.py

class RAGPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()
        self.llm = LLM()

    def ingest_documents(self, documents):
        self.vector_store.clear()
        self.vector_store.add_documents(documents)

    def query(self, user_question: str):
        query_embedding = self.embedder.embed_text(user_question)
        relevant_chunks = self.vector_store.retrieve(query_embedding)

        if not relevant_chunks:
            return "❌ Sorry, I couldn't find any relevant information in the uploaded documents."

        # Build context
        unique_texts = list(dict.fromkeys([chunk['text'] for chunk in relevant_chunks]))
        context = "\n\n".join(unique_texts)
        # ✨ New minimalist prompt
        prompt = (
            f"You are an expert assistant. Based only on the following context, give a short, direct, 2–3 sentence answer.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {user_question}\n\n"
            f"Do not repeat the context. Answer clearly:"
            )

        answer = self.llm.generate(prompt)

        # 🧹 Only return the answer
        return answer