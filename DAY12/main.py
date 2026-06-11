from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    init_db,
    db_create_task,
    db_get_all_tasks,
    db_get_task,
    db_update_task,
    db_delete_task,
    db_get_tasks_by_status
)

app = FastAPI()

init_db()


class Task(BaseModel):
    title: str
    status: str


# CREATE
@app.post("/tasks")
def create_task(task: Task):

    return db_create_task(
        task.title,
        task.status
    )


# GET ALL + SEARCH
@app.get("/tasks")
def get_tasks(status: str = None):

    if status:
        return db_get_tasks_by_status(status)

    return db_get_all_tasks()


# GET ONE
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    task = db_get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# UPDATE
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    existing_task = db_get_task(task_id)

    if not existing_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return db_update_task(
        task_id,
        task.title,
        task.status
    )


# DELETE
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    deleted = db_delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }