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

    MAX_BATCH_SIZE = 150
    for i in range(0, len(chunks), MAX_BATCH_SIZE):
        batch = chunks[i:i+MAX_BATCH_SIZE]
        await db.aadd_documents(batch)
        print(f"Saved batch with {len(batch)} chunks.")

    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")
