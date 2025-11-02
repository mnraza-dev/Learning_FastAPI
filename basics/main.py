from fastapi import FastAPI
from fastapi.params import Body
from .user import User

app = FastAPI()

@app.get("/")
def hello(person:User):
    return person

person = User(name="John Doe", age=30, email="john.doe@gmail.com", skills=["Python", "FastAPI"], contact_details={"phone": "123-456-7890"})

