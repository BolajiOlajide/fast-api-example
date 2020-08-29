from typing import Dict, Optional

from fastapi import FastAPI, UploadFile, File, Form, Cookie
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models import Sentence
from routers import user_router


app = FastAPI()
app.include_router(user_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"hello": "world"}


@app.get("/search")
def search(q: str):
    return {"query": q}


@app.post("/lowercase")
def lower_case(sentence: Sentence):
    return {"text": sentence.text.lower()}


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    return {"name": file.filename}


@app.post("/submit")
def echo(city: Optional[str] = Form("Paris")):
    # def echo(city: Optional[str] = Form(None)):
    # def echo(city: str = Form(...)):
    return {"city": city}


@app.get("/profile")
def profile(name=Cookie(None)):
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run(app)
