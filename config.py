from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")


MODEL_SOURCE = "mistral"  # or "llama"
CSV_PATH = "data/updated_website_data.csv"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
HUGGINGFACE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"