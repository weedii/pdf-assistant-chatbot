from fastapi import UploadFile, HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from io import BytesIO
import PyPDF2
from app.utils import saveChunksToDB


async def uploadPDFController(file: UploadFile, userEmail: str):
    # ensure file type is pdf
    if (file.content_type != "application/pdf"):
        raise HTTPException(
            status_code=400, detail="file type must be 'application/pdf'")

    pdfContent = await file.read()
    # extract text from pdf
    pdfReader = PyPDF2.PdfReader(BytesIO(pdfContent))

    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = []
    for page_Num, page in enumerate(pdfReader.pages, start=1):
        pageText = page.extract_text()
        document = Document(
            page_content=pageText,
            metadata={"page number": page_Num}
        )
        documents.append(document)

    chunks = textSplitter.split_documents(documents)

    # todo save chunks to DB
    await saveChunksToDB(chunks, userEmail)

    return "File was uploaded successfuly"
