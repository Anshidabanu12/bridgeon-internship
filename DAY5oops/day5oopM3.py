class car:
    def __init__(self,make,model,year,odometer=0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def drive (self,km):
        self.odometer += km
    def get_info(self):
        print(f"make:{self.make}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
        print(f"odometer:{self.odometer}km")
car1 = car("BMW", "M4", 2026)
car1.get_info()
car1.drive(100)
car1.drive(150)
print("\n after driving :")
car1.get_info()