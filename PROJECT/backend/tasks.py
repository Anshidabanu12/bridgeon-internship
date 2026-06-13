from fastapi import APIRouter, HTTPException

from models import Task
from database import users_db, tasks_db

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/{username}")
def get_tasks(username: str):

    if username not in users_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return tasks_db[username]


@router.post("/{username}")
def create_task(username: str, task: Task):

    if username not in users_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    task_id = len(tasks_db[username]) + 1

    new_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "due_date": str(task.due_date),
        "completed": False
    }

    tasks_db[username].append(new_task)

    return {
        "message": "Task Created Successfully",
        "task": new_task
    }


@router.put("/{username}/{task_id}")
def complete_task(username: str, task_id: int):

    if username not in users_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    for task in tasks_db[username]:

        if task["id"] == task_id:

            task["completed"] = True

            return {
                "message": "Task Completed"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@router.delete("/{username}/{task_id}")
def delete_task(username: str, task_id: int):

    if username not in users_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    for index, task in enumerate(tasks_db[username]):

        if task["id"] == task_id:

            tasks_db[username].pop(index)

            return {
                "message": "Task Deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )