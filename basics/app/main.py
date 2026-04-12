from fastapi import FastAPI
from .mockData import posts
from .schemas.schemas import Post

app = FastAPI()

# List all posts
@app.get("/posts")
def list_posts():
    return {
        "msg":"All posts fetched",
        "data":posts
    }

# Get a post using id
@app.get("/posts/{post_id}")
def single_post(post_id:int):
    for p in posts:
        if p.get("id") == post_id:
            return p
    return {
        "error":"Post not found!"
    }
    
# Create a post 
@app.post("/posts/create")
def create_post(p: Post):
    posts.append(p.model_dump())
    return {
        "msg":"Post created",
        "data": p
    }
    
# Update a post - id
@app.put("/posts/update/{post_id}")
def update_post(post_id:int,p: Post):
    for b in posts:
        if b.get("id") == post_id:
            b.update(p.model_dump())
            return {
                "msg":"Updated a post",
                "data": b
            }
    return {
        "error":"Post not found!"
    }
    
# Delete a post - id
@app.delete("/posts/delete/{post_id}")
def delete_post(post_id:int):
    for index, b in enumerate(posts):
        if b.get("id") == post_id:
            deleted_post = posts.pop(index)
            return {
                "msg":"Deleted a post",
                "data": deleted_post
            }
    return {
        "error":"Post not found!"
    }