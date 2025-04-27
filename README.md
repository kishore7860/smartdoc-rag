# 📚 RAG-Powered Document Q&A Chatbot

An intelligent chatbot that answers questions based on uploaded documents (PDFs, research papers) using Retrieval-Augmented Generation (RAG) and powerful LLMs like Mistral-7B via Hugging Face Inference API.

---

## ✨ Features
- Upload PDFs
- Smart document chunking
- Semantic retrieval with embeddings
- LLM-based context-aware answer generation
- Deployed-ready (Docker + Cloud Run)

---

## 🛠 Tech Stack
- Python
- Streamlit (Frontend)
- Hugging Face Transformers (Embeddings, Inference)
- ChromaDB (Vector Storage)
- Docker (Deployment)

---

## 📦 Setup Instructions

1. Clone the repository
   
   git clone https://github.com/your-username/rag-doc-chatbot.git
   cd rag-doc-chatbot

2.	Create and activate a virtual environment

    python3 -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows

3.	Install the required packages
    pip install -r requirements.txt

4. Configure Hugging Face Inference API key in the .env file
    HUGGING_FACE_API_KEY=your_api_key_here

5. Run the Streamlit app
    streamlit run app.py


## 📚 Architecture

User (Streamlit UI)
       ↓
  Query Embedding → Vector Retrieval → RAG Prompt
       ↓
    LLM Generation (Mistral-7B Inference API)
       ↓
     Final Answer Display

## ✨ Credits
	•	Hugging Face 🤗
	•	Streamlit
	•	ChromaDB
	•	Mistral AI
