from app.utils import retrieveData, generateResponseFromPrompt
from fastapi import HTTPException


async def sendPromptController(prompt: str, userEmail: str):
    # retrieve Data
    data = retrieveData(prompt, userEmail)

    if (data == None):
        raise HTTPException(
            status_code=404, detail="Unable to find matching results")

    # Generate response from prompt
    res = generateResponseFromPrompt(data, prompt)

    # return f"Message recieved {prompt}"
    return res
