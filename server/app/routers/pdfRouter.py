from fastapi import APIRouter, UploadFile
from app.controllers import uploadPDFController

pdfRouter = APIRouter()


@pdfRouter.post("/pdf")
async def uploadPDF(file: UploadFile):
    return await uploadPDFController(file)
