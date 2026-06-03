# def greet(Name):
#     return f"Hello,{Name}"
def calculate_grade(*mark):
    avg = sum(mark) / len(mark)
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "E" 
    else:
        return "F"
    return mark
print(calculate_grade(10,17,89))