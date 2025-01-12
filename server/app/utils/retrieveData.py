from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

CHROMA_PATH = "chroma"


def retrieveData(prompt: str, userEmail: str):

    collectionName = f"user_{userEmail.replace('@', '_').replace('.', '_')}"

    db = Chroma(
        collection_name=collectionName,
        persist_directory=CHROMA_PATH,
        embedding_function=OpenAIEmbeddings()
    )

    res = db.similarity_search_with_relevance_scores(prompt, k=5)
    if len(res) == 0:
        return None

    context_text = "\n\n---\n\n".join(
        [doc.page_content for doc, _score in res])

    return context_text
