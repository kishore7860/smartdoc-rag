# app/models/llm.py

from transformers import pipeline

class LLM:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')  # Start with GPT-2 locally

    def generate(self, prompt: str):
        response = self.generator(prompt, max_length=200, do_sample=True, top_p=0.95, temperature=0.7)
        return response[0]['generated_text'].strip()