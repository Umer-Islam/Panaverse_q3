# from typing import Union
# Union is no longer needed, in line 15 we can simple remove union[str,None] and replace it with "str| None"
from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


app = FastAPI()




