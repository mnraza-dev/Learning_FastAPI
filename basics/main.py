from fastapi import FastAPI, Request
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
    return {
       "message":  f"Hey! {name}, Your age is {age}"
    }

@app.get("/hello")
def hello(request:Request):
    query_params = dict(request.query_params)
    # print(query_params)
    return {
       "message":  f"Hey! {query_params.get("name")}, You are {query_params.get("age")} years old "
    }
