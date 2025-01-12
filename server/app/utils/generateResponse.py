from langchain.prompts import ChatPromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM


PROMPT_TEMPLATE = """
You are an expert assistant providing answers based solely on the provided context. Avoid including information that is not explicitly mentioned.

Context:
{context}

Question: {question}

Answer the question thoroughly but concisely:
"""


def generateFormattedPrompt(data: str, prompt: str):
    promptTemplate = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    formattedPrompt = promptTemplate.format(context=data, question=prompt)

    return formattedPrompt


def loadModel():
    tokenizer = AutoTokenizer.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    model = AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0")

    return tokenizer, model


def generateResponseFromModel(tokenizer, model, prompt):
    inputs = tokenizer(prompt, return_tensors="pt",
                       truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        num_beams=3,
        early_stopping=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Extract only the model's response without including the full prompt
    response = response[len(prompt):].strip()
    print(response)

    return response


def generateResponseFromPrompt(data: str, prompt: str):
    tokenizer, model = loadModel()
    formattedPrompt = generateFormattedPrompt(data, prompt)
    res = generateResponseFromModel(tokenizer, model, formattedPrompt)

    return res
