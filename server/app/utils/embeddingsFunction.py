from langchain_huggingface import HuggingFaceEmbeddings


def getEmbeddingsFunction():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings
