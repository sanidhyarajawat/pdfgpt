from utils.extract import extract_text_from_pdf
from utils.chunking import chunk_text
from utils.embed_store import embed_and_store
from utils.query import get_qa_chain, answer_question

def main():
    pdf_path = input("Enter PDF file path: ")
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    vectorstore = embed_and_store(chunks)
    
    print("\n✅ PDF indexed. Ask a question (type 'exit' to quit):")
    chain = get_qa_chain(vectorstore)
    
    while True:
        query = input("\nYour question: ")
        if query.lower() == "exit":
            break
        answer = answer_question(chain, query)
        print(f"\n📘 Answer: {answer}")

if __name__ == "__main__":
    main()