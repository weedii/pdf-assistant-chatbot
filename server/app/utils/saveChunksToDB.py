from langchain.schema import Document
from .embeddingsFunction import getEmbeddingsFunction
from .db import getDB


CHROMA_PATH = "chroma"


def saveChunksToDB(chunks: list[Document]):

    db = getDB()

    db.add_documents(chunks)
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")
