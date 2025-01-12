from langchain_huggingface import HuggingFaceEmbeddings
from .db import getDB
from .embeddingsFunction import getEmbeddingsFunction

CHROMA_PATH = "chroma"


def retrieveData(prompt: str):

    db = getDB()
    embeddings = getEmbeddingsFunction()
    prpr = embeddings.embed_query(prompt)

    res = db._similarity_search_with_relevance_scores(prompt, k=5)
    # filtered_res = [(doc, score) for doc, score in res if 0.7 <= score <= 0.9]
    # print(res)

    # if len(filtered_res) == 0:
    # return None

    # if (len(res) == 0 or res[0][1] < 0.7 or res[0][1] > 1.3):
    #     return None

    # context_text = "\n\n---\n\n".join(
    #     [doc.page_content + f"\n$$$$$$${_score}$$$$$$" for doc, _score in res])

    context_text = "\n\n---\n\n".join(
        [doc.page_content for doc, _score in res])

    # print(context_text)

    return context_text
