from fastapi import FastAPI
from app.routers import entryRouter, pdfRouter, chatRouter


app = FastAPI()

app.include_router(entryRouter)
app.include_router(pdfRouter)
app.include_router(chatRouter)
