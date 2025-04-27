# src/models/llm.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class LLM:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"
        }

    def generate(self, prompt: str):
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 300,
                "temperature": 0.7,
                "top_p": 0.95,
            }
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)

        # Handle unauthorized better
        if response.status_code == 401:
            raise Exception("Unauthorized: Please check your HuggingFace token or accept model access agreement.")
        
        response.raise_for_status()
        generated_text = response.json()[0]["generated_text"]
        return generated_text.strip()