from langchain.schema import Document
from .embeddingsFunction import getEmbeddingsFunction
from .db import getDB
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


CHROMA_PATH = "chroma"


def saveChunksToDB(chunks: list[Document]):

    # db = getDB()

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )

    # db.add_documents(chunks)
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")
