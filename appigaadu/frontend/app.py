
import streamlit as st
from appigaadu.backend.rag_pipeline import RAG

st.set_page_config(page_title="Document Q&A Chatbot", page_icon="📚", layout="centered")

# Initialize RAG Pipeline
rag_pipeline = RAG()

st.title("📚 Document Q&A Chatbot")

# Upload PDF section (later we'll hook it up)
st.sidebar.header("Upload your documents")
uploaded_files = st.sidebar.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True)

st.write("### Ask a question about your uploaded documents:")

user_question = st.text_input("Enter your question here:")

if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = rag_pipeline.query(user_question)
        st.success(answer)