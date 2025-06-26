from data_loader import load_website_data
from embedder import chunk_text, embed_chunks
from retriever import VectorStore
from generator import generate_response

class Chatbot:
    def __init__(self):
        docs = load_website_data()
        self.chunks = [chunk for doc in docs for chunk in chunk_text(doc)]
        self.embeddings = embed_chunks(self.chunks)
        self.vstore = VectorStore(np.array(self.embeddings), self.chunks)

    def ask(self, query):
        context = self.vstore.search(query)
        return generate_response(query, context)