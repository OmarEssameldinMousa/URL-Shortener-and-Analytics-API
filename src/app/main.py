# main.py
from fastapi import FastAPI
from .core.config import settings

app = FastAPI()

@app.get("/")
async def read_root():
    return {"settings": settings.model_dump()}