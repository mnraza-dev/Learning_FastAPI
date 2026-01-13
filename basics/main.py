from fastapi import FastAPI
from mockData import products
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello there"}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_single_products(product_id : int):
    for item in products:
        if item.get("id") == product_id:
            return item
    return {
        "error":"Product not found"
    }

@app.get("/greet")
def greet(name:str, age:int):
    return f"Hey! {name}, Your age is {age}"