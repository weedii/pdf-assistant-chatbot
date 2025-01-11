from app.utils import retrieveData
from fastapi import HTTPException
from app.utils import generateResponseFromPrompt


async def sendPromptController(prompt: str):
    # retrieve Data
    data = retrieveData(prompt)

    if (data == None):
        raise HTTPException(
            status_code=404, detail="Unable to find matching results")

    # Generate response from prompt
    res = generateResponseFromPrompt(data, prompt)

    # return f"Message recieved {prompt}"
    return res