from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Welcome to FastAPI 🚀"}

