# app/frontend/app.py

import streamlit as st
from src.backend.rag_pipeline import RAGPipeline
from src.utils.pdf_utils import parse_and_chunk_pdfs

# Set Streamlit page config
st.set_page_config(page_title="Document Q&A Chatbot", page_icon="📚", layout="wide")

# Initialize RAG Pipeline
rag_pipeline = RAGPipeline()

# UI - Sidebar for Document Upload
st.sidebar.header("📄 Upload Documents")
uploaded_files = st.sidebar.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    # Ingest documents
    chunks = parse_and_chunk_pdfs(uploaded_files)
    rag_pipeline.ingest_documents(chunks)
    st.sidebar.success(f"Uploaded and processed {len(chunks)} chunks from {len(uploaded_files)} file(s).")

# Main Section
st.title("📚 Document Q&A Chatbot")
st.write("Ask a question about your uploaded documents:")

user_question = st.text_input("💬 Enter your question:")

if st.button("Get Answer"):
    if not uploaded_files:
        st.warning("⚠️ Please upload at least one PDF first.")
    elif not user_question.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            answer = rag_pipeline.query(user_question)
            st.success(answer)