# from typing import Union
# Union is no longer needed, in line 15 we can simple remove union[str,None] and replace it with "str| None" 
from fastapi import FastAPI

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates




app = FastAPI()

app.mount("/static", StaticFiles(directory = "static"), name="static")

@app.get("/")

def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")

def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
