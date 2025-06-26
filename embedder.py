from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

model = SentenceTransformer(EMBEDDING_MODEL)

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Takes each document content and splits into chunks with the desired chunk size.

    Args:
        text (str): Each row string content.
        chunk_size: length of input sequences.
        chunk_overlap: length of words or sentences to overlap between chunks.

    Returns:
        returns chunks
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

def embed_chunks(chunks):
    return model.encode(chunks, show_progress_bar=True)