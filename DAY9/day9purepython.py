class TaskNotFoundError(Exception):
    pass


class TaskAlreadyExistsError(Exception):
    pass


# Store tasks
tasks = {}


# Get all tasks
def get_all_tasks() -> list:
    return list(tasks.values())


# Get one task
def get_task(task_id: int) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")
    return tasks[task_id]


# Create task
def create_task(task_id: int, data: dict) -> dict:
    if task_id in tasks:
        raise TaskAlreadyExistsError("Task ID already exists")

    tasks[task_id] = data
    return data


# Update task
def update_task(task_id: int, data: dict) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")

    tasks[task_id].update(data)
    return tasks[task_id]


# Delete task
def delete_task(task_id: int) -> bool:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")

    del tasks[task_id]
    return True


# Menu
while True:
    print("\n--- Task Manager ---")
    print("1. View all tasks")
    print("2. View task")
    print("3. Create task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            print(get_all_tasks())

        elif choice == "2":
            task_id = int(input("Enter task ID: "))
            print(get_task(task_id))

        elif choice == "3":
            task_id = int(input("Enter ID: "))
            title = input("Enter title: ")

            task_data = {
                "id": task_id,
                "title": title
            }

            create_task(task_id, task_data)
            print("Task created")

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            new_title = input("Enter new title: ")

            print(update_task(task_id, {"title": new_title}))

        elif choice == "5":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
            print("Task deleted")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)