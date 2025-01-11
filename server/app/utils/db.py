from langchain_chroma import Chroma
from .embeddingsFunction import getEmbeddingsFunction
import os

CHROMA_PATH = "chroma"


def getDB():
    embeddings = getEmbeddingsFunction()

    db = Chroma(persist_directory=CHROMA_PATH,
                embedding_function=embeddings)

    return db
