marks=[45,56,89,90,67,49,56,34,23,90]
average=sum(marks)/len(marks)
print(average)
print("highes:",max(marks))
print("lowest:",min(marks))
unique=list(set(marks))
print(unique)
above = []
for i in marks:
    if i > average:
        above.append(i)
print(above)

