import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI, APIError
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/echo")
def echo(message: Message):
    return {"received": message.text}

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=500)

@app.post("/generate")
def generate(request: GenerateRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured"
        )
    try:
        client = OpenAI(timeout=20.0, max_retries=1)
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=request.prompt,
            max_output_tokens=150
        )
        return {"answer": response.output_text}
    
    except APIError:
        raise HTTPException(
            status_code=502,
            detail="AI service unavailable"
        )