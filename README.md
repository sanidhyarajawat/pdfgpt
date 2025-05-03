# 📘 PDF RAG QA

A simple Retrieval-Augmented Generation (RAG) tool to ask questions about any PDF using OpenAI and FAISS.

## Features
- Upload any PDF
- Automatically extracts, chunks, and embeds the text
- Ask natural questions and get context-aware answers

## Tech Stack
- Python
- LangChain
- FAISS
- OpenAI GPT-3.5
- PyPDF2

## Setup
```bash
git clone https://github.com/yourusername/pdf-rag-qa
cd pdf-rag-qa
pip install -r requirements.txt
echo "OPENAI_API_KEY=your-key" > .env
python app.py