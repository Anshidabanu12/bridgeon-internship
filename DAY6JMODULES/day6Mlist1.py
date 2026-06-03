import json
students = [
    {"name":"john","age":20,"mark":92},
    {"name":"zara","age":21,"mark":99},
    {"name":"miya","age":23,"mark":98},
    {"name":"jerry","age":21,"mark":90},
    {"name":"niya","age":21,"mark":89}
]
with open("students.json", "w") as f:
    json.dump(students,f, indent=2)
with open("students.json","r") as f:
    print(f.read())