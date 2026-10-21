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
    prompt: str = Field(
        min_length=10, 
        max_length=500
    )
    max_tokens: int = Field(
        default=1,
        ge=1,
        le=500
    )

class StudyNotesRequest(BaseModel):
    notes: str = Field(min_length=20, max_length=3000)


class StudyNotesResult(BaseModel):
    summary: str
    key_points: list[str]
    practice_question: str

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

@app.post("/study-notes")
def study_notes(request: StudyNotesRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured"
        )
    try:    
        client = OpenAI(timeout=20.0, max_retries=1)
        response = client.responses.parse(
            model="gpt-4.1-mini",
            instructions="Summarize the notes. Return exactly three key points and one practice question.",
            input=request.notes,
            text_format=StudyNotesResult,
            max_output_tokens=300
        )
        if response.output_parsed is None:
            raise HTTPException(
                status_code=502,
                detail="AI service returned no structured output"
            )
        return response.output_parsed
    except APIError:
        raise HTTPException(
            status_code=502,
            detail="AI service unavailable"
        )