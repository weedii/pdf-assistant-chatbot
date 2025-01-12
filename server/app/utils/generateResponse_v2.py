from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from langchain.schema import HumanMessage, AIMessage

load_dotenv()
openApiKey = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE = """
You are an expert assistant providing answers based solely on the provided context. Avoid including information that is not explicitly mentioned.

Context:
{context}

Question: {question}

Answer the question thoroughly but concisely and retun only response text:
"""

chatHistory = []


def generateFormattedPrompt(data: str, prompt: str):
    promptTemplate = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    formattedPrompt = promptTemplate.format(context=data, question=prompt)
    return formattedPrompt


def generateResponseFromPrompt(data: str, prompt: str):
    formattedPrompt = generateFormattedPrompt(data, prompt)

    chatHistory.append(HumanMessage(content=formattedPrompt, role="user"))

    model = ChatOpenAI(openai_api_key=openApiKey)
    res = model.invoke(chatHistory)

    chatHistory.append(AIMessage(content=res.content, role="assistant"))

    return res.content
