from fastapi import APIRouter
from .models import Task
from .database import tasks

router = APIRouter()

@router.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "isCompleted": task.isCompleted
    }
    tasks.append(new_task)
    return new_task

@router.get("/tasks")
def get_tasks():
    return tasks

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["isCompleted"] = updated_task.isCompleted
            return {
                "message": "Task updated successfully",
                "task": task
            }
    return {"error": "Task not found"}
