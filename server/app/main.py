from fastapi import FastAPI
from app.routers import entryRouter, pdfRouter, chatRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origings = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origings,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entryRouter)
app.include_router(pdfRouter)
app.include_router(chatRouter)
