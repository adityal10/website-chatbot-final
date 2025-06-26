from config import MODEL_SOURCE, HUGGINGFACE_MODEL, OLLAMA_ENDPOINT
import requests, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

if MODEL_SOURCE == "mistral":
    tokenizer = AutoTokenizer.from_pretrained(HUGGINGFACE_MODEL)
    lm_model = AutoModelForCausalLM.from_pretrained(
        HUGGINGFACE_MODEL, torch_dtype=torch.float16, device_map="auto"
    )

def generate_response(query, context):
    prompt = (
        "Answer the question based on the context below. If unsure, say you don't know.\n\n"
        f"Context:\n{chr(10).join(context)}\n\n"
        f"Question: {query}\nAnswer:"
    )

    if MODEL_SOURCE == "llama":
        res = requests.post(OLLAMA_ENDPOINT, json={"model": "llama3", "prompt": prompt, "stream": False})
        return res.json().get("response", "") if res.status_code == 200 else "Error"

    if MODEL_SOURCE == "mistral":
        inputs = tokenizer(prompt, return_tensors="pt").to(lm_model.device)
        outputs = lm_model.generate(**inputs, max_new_tokens=300)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result.split("Answer:")[-1].strip()