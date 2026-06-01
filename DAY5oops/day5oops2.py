class student: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
    def __str__(self):
        return self.name
s1= student ("sara",23)
print(s1)
s1.display()