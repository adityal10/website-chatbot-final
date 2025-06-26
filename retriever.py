import faiss
import numpy as np
from embedder import model

class VectorStore:
    """
    Storing the embedded chunks into FAISS vector database

    Args:
    Text Embeddings
    Texts
    """
    def __init__(self, embeddings, texts):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.texts = texts

    def search(self, query, top_k=5):
        query_vec = model.encode([query])
        _, I = self.index.search(np.array(query_vec), top_k)
        return [self.texts[i] for i in I[0]]