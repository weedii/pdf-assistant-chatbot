from fastapi import APIRouter
from app.controllers import sendPromptController

chatRouter = APIRouter()


@chatRouter.post("/chat")
async def sendPrompt(prompt: str):
    return await sendPromptController(prompt)
