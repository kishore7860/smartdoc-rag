# src/utils/pdf_utils.py

import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter

def parse_and_chunk_pdfs(uploaded_files):
    all_text = ""

    for file in uploaded_files:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"  # Add page break

    # Now split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # ~500 characters (around 100-150 tokens)
        chunk_overlap=50,  # overlap between chunks to preserve context
        separators=["\n\n", "\n", ".", " "]  # prioritize splitting at paragraph breaks
    )

    chunks = text_splitter.split_text(all_text)

    # Return chunks as dicts (ready for vectorstore)
    return [{"text": chunk} for chunk in chunks]