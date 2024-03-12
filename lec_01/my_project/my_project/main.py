from fastapi import FastAPI
app:FastAPI = FastAPI(title = "simple query")
@app.get("/")
def index():
    return {"message: Heloo WOrld!!!!!!"}
