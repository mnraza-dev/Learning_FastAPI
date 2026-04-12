from pydantic import BaseModel

class Product(BaseModel):
    id: int
    title: str
    price:int
    quantity:int

class Todo(BaseModel):
    id:int
    title:str
    status: str

class Post(BaseModel):
    id:int
    title: str
    desc:str
    author: str
    published_on:str    