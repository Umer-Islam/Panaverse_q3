from fastapi import FastAPI

app = FastAPI(lifespan=lifespan, title="Hello World API with DB", 
    version="0.0.1",
    servers=[
        {
            "url": "http://0.0.0.0:8000",
            "description": "Development Server"
        }
        ])


@app.get("/")
def read_root():
    return {"Hello": "World😊😊😊"}