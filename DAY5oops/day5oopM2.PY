class employee:
    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary
    def get_info(self):
        return f"name: {self.name}, department:{self.department},salary:{self.salary}"
    def __str__(self):
          return f"employee {self.name},{self.department},{self.salary}"
emp = employee("john","IT",100000)
print(emp.get_info())
print(emp)
