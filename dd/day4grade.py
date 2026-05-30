class InvalidMarkError(Exception):
   pass
def students (name,*mark):
    if len(mark) == 0:
        print("no marks")
    for m in mark:
        if m < 0 or m > 100:
            raise InvalidMarkError("mark must be 0 to 100")
    avg = sum(mark) / len(mark)
    if avg>=90:
       grade="A"
    elif avg>=80:
       grade="B"
    elif avg>=75:
       grade="C"
    elif avg>=50:
       grade="D"
    elif avg>=40:
       grade="E"
    else:
      grade="F"
    return name, avg, grade
def generate_report(students_list):
    print("_" * 30)
    print(f"{'name':<10}{'average':<10}{'grade':<10}")
    print("_" * 30)
    for student in students_list:
       try:
          name = student[0]
          mark = student[1:]
          result = students(name,*mark)
          print(f"{result[0]:<10}{result[1]:<10}{result[2]:<10}")
       except InvalidMarkError as e:
          print(f"{student[0]:}error{e}")
students_data = [
     ("john",99,99.8,78,99),
     ("sara",45,67,34,90,67),
     ("jeny",93,45,90,89,90)
]
generate_report(students_data)
          
