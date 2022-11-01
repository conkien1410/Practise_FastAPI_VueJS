import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    uvicorn.run("main:app", port=5000, log_level="debug")