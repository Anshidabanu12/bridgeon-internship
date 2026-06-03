import json
student = [
    {"name":"john","age":20,"mark":92},
    {"name":"zara","age":21,"mark":99},
    {"name":"miya","age":23,"mark":98},
    {"name":"jerry","age":21,"mark":90},
    {"name":"niya","age":21,"mark":89}
]
with open("student.json", "w") as f:
    json.dump(student, f, indent=2)
with open("student.json","r") as f:
    print(f.read())