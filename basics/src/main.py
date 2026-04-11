from fastapi import FastAPI, Request
from . mockData import products
from .schemas import Product
app = FastAPI()

# GET - List all Product 

@app.get("/products")
def get_all_products():
    return products

# GET - Single Product 

@app.get("/products/{product_id}")
def get_single_product(product_id: int):
    for singleproduct in products:
        if singleproduct.get("id") == product_id:
            return singleproduct
    return {
        "error":"Product not found"
    }
    
# POST - Create a Product 

@app.post("/products/create")
def create_product(product: Product):
    new_product = product.model_dump()
    products.append(new_product)
    return{
        "msg":"Product added successfully!",
        "data":products
    }

# PUT - UPDATE PRODUCT

@app.put("/products/update/{product_id}")
def update_product(product_id: int, product:Product):
    for p in products :
        if p.get('id') == product_id:
            p.update(product.model_dump())
            return {
                "msg":"Product updated successfully!",
                "data":p
            }
    return {"error": "Product not found"}

# DELETE - DELETE PRODUCT

@app.delete("/products/delete/{product_id}")
def delete_product(product_id:int):
    for index, p in enumerate(products):
        if p.get('id')  ==  product_id:
           deleted_product = products.pop(index)
           return {
               "msg":"Product deleted successfully!",
               "data": deleted_product
           }
    return {
        "err":"Product not found"
    }