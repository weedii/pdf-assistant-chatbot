from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


CHROMA_PATH = "chroma"


async def saveChunksToDB(chunks: list[Document], userEmail: str):
    collectionName = f"user_{userEmail.replace('@', '_').replace('.', '_')}"

    db = Chroma(
        collection_name=collectionName,
        embedding_function=OpenAIEmbeddings(),
        persist_directory=CHROMA_PATH
    )
    await db.aadd_documents(chunks)

    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")
