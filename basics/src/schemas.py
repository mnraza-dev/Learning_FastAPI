from pydantic import BaseModel

class Product(BaseModel):
    id: int
    title: str
    price:int
    quantity:int
    