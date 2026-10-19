from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/echo")
def echo(message: Message):
    return {"received": message.text}