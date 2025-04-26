
from appigaadu.models.embedder import Embedder
from appigaadu.backend.vector_store import VectorStore
from appigaadu.models.llm import LLM

class RAG:
    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()
        self.llm = LLM()

    def query(self, user_question: str):
        # Step 1: Embed the query
        query_embedding = self.embedder.embed_text(user_question)
        
        # Step 2: Retrieve relevant documents
        relevant_chunks = self.vector_store.retrieve(query_embedding)
        
        # Step 3: Create prompt
        context = "\n".join([chunk['text'] for chunk in relevant_chunks])
        prompt = f"Answer the question based on the context:\n\nContext:\n{context}\n\nQuestion:\n{user_question}\nAnswer:"
        
        # Step 4: Get LLM Response
        answer = self.llm.generate(prompt)
        return answer