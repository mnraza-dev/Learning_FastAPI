from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

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

@app.post("/create-product")
def create_product(product_data: ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status":"Product created Successfully!","data":products}

@app.put("/update-product")
def update_product(product_id: int, product_data: ProductDTO):
    for index, item in enumerate(products):
        if product_id == item.get("id"):
            products[index] = product_data.model_dump()
            return {
                "status": "Product updated successfully",
                "product": products[index]
            }

    return {
        "status": "Product not found"
    }

