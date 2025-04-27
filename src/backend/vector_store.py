
import chromadb
from src.models.embedder import Embedder
import uuid

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="documents")
        self.embedder = Embedder()

    def add_documents(self, documents):
        texts = [doc["text"] for doc in documents]
        embeddings = self.embedder.model.encode(texts).tolist()
        ids = [str(uuid.uuid4()) for _ in range(len(texts))]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids,
        )

    def retrieve(self, query_embedding):
        query_vector = query_embedding.tolist()
        results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=3,
            include=["documents"]
        )
        retrieved_texts = results["documents"][0]
        return [{"text": t} for t in retrieved_texts]