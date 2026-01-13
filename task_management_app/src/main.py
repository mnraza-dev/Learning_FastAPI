from fastapi import FastAPI

app = FastAPI(title="Task Management App")

@app.get("/")
def root():
    return {"message": "Hello from task-management-app!"}
