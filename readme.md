# Retrieval-Augmented Website Assistant

It is a local chatbot built to answer user queries based on website data. It uses **Retrieval-Augmented Generation (RAG)** and supports **open-source models** like `LLaMA 3` (via Ollama) and `Mistral 7B` (via HuggingFace).


## Project Structure
```
jaaji_chatbot
├── app.py                 # CLI chat interface
├── config.py              # Configuration: model, paths, chunking, etc.
├── data_loader.py         # CSV loader + cleaner
├── embedder.py            # Chunking + Embedding
├── retriever.py           # FAISS vector store for retrieval
├── generator.py           # LLM response (Ollama or HuggingFace)
├── interface.py           # Chat logic: query → retrieve → generate
├── data/
│   └── updated_website_data.csv  # Your website content
├── requirements.txt
└── README.md
```
## Setup

1. **Clone the project**

```bash
git clone https://your-repo-url
cd jaaji_chatbot
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create .env file and add your hugginface token**

```bash
HUGGINGFACE_API_KEY=your_token_here
```

4. **Start the chatbot**

```bash
python app.py
```

---

## Model Switching

You can use either LLaMA 3 (via Ollama) or Mistral (via HuggingFace).

To switch models, open `config.py`:

```python
MODEL_SOURCE = "llama"  # or "mistral"
```

Make sure to do these steps for using mistral

* Keep your HuggingFace API key in a secrets folder.
* Go to this url [Mistral LLM](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) and accpet the terms and conditions after logging in using api key 
---

## How it Works

1. **Data Loading**: Parses `updated_website_data.csv` into clean text.
2. **Embedding**: Splits text into chunks + generates embeddings.
3. **Retrieval**: Uses FAISS to find relevant chunks per query.
4. **Generation**: Prompts an LLM (LLaMA or Mistral) with context + question.
5. **Response**: LLM generates helpful answers grounded in your site data.

---

## Dependencies

Key Python libraries:

* `transformers`, `torch`, `sentence-transformers`
* `faiss-cpu`, `pandas`, `numpy`, `tqdm`
* `requests` (for Ollama HTTP API)

---

## Credits

Created by the Jaaji team.
Powered by open-source models: [Meta AI LLaMA](https://ai.meta.com/llama) & [Mistral AI](https://huggingface.co/mistralai).
