from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

llm = OllamaLLM(
    model="llama3.2"
)

def get_answer(question):

    docs = vectordb.similarity_search_with_score(
        question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc, score in docs
    )

    prompt = f"""
You are a customer support assistant.

Answer ONLY from the context.

If answer is unavailable say:
'I could not find that information in the policy.'

Context:
{context}

Question:
{question}
"""

    answer = llm.invoke(prompt)

    pages = []

    scores = []

    for doc, score in docs:

        pages.append(
            str(doc.metadata.get("page", "Unknown"))
        )

        scores.append(score)

    confidence = round(
        max(
            0,
            100 - (sum(scores)/len(scores))*10
        ),
        2
    )

    return {
        "answer": answer,
        "pages": list(set(pages)),
        "confidence": confidence
    }