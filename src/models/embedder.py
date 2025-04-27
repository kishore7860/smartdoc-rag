
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Small, fast model

    def embed_text(self, text: str):
        return self.model.encode(text, convert_to_tensor=True)