# from typing import Union
# Union is no longer needed, in line 15 we can simple remove union[str,None] and replace it with "str| None"
from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

conn = MongoClient("mongodb://localhost:27017")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes_fastapi.notes.find({})
    for doc in docs:
        print(doc)
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
