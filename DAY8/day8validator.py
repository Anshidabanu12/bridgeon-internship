from pydantic import BaseModel, ValidationError
class taskmodel(BaseModel):
    tittle : str
    priority :str = "low"
    completed : bool = False
try:    
    task1 = taskmodel(
    tittle ="leran fastAPI",
    priority ="high",
    completed = True
    )
    print("vali task")  
    print(task1)
except ValidationError as e:
    print(e)
print("\n" + "e" * 40 + "\n")


try:
    bad_task = taskmodel(
        tittle = 123,
        priority = ["high"],
        completed = "hello"
    )
except ValidationError as e:
    print("validation error")
    print("-" * 30) 
    for error in e.errors():
        field = error["loc"][0]
        message = error["msg"]
        print(f"{field}:{message}")