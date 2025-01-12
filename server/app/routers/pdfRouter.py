from fastapi import APIRouter, UploadFile
from app.controllers import uploadPDFController

pdfRouter = APIRouter()


@pdfRouter.post("/pdf")
async def uploadPDF(file: UploadFile, userEmail: str):
    return await uploadPDFController(file, userEmail)
