from langchain_huggingface import HuggingFaceEmbeddings
from .db import getDB
from .embeddingsFunction import getEmbeddingsFunction

CHROMA_PATH = "chroma"


def retrieveData(prompt: str):

    db = getDB()

    # search in DB
    res = db.similarity_search_with_score(prompt, k=5)

    if (len(res) == 0 or res[0][1] < 0.7 or res[0][1] > 1.3):
        # print("Unable to find matching results")
        return None

    # context_text = "\n\n---\n\n".join(
    #     [doc.page_content + f"\n$$$$$$${_score}$$$$$$" for doc, _score in res])

    context_text = "\n\n---\n\n".join(
        [doc.page_content for doc, _score in res])

    # print(context_text)

    return context_text
