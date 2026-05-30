mark=[23,6,38,47,20,86,98,541,22,45]
average=(sum(mark)/len(mark))
print(average)
largest=max(mark)
lowest=min(mark)
unique=list(set(mark))
print(unique)
above=[]
for i in mark:
    if(i>average):
        above.append(i)
print(above)
print(mark)
print("\n___student marks_")  
print("average",average)
print("unique",unique)
print("highest",largest)
print("lowest",lowest)
print("above ",above)