def calculate_grade(name: str,marks: list[int])->str:
  avg: float = sum(marks)/len(marks)
  if avg >=90:
    return  "A"
  elif avg >= 75:
    return"B"
  elif avg >=50:
     return "c"
  else:
    return"F"
    return f"{name}' grade is {grade}"

grade = calculate_grade("sara",[85,99,99])
print("grade:",grade)
