class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound  
    def speak(self):
        print(f"{self.name}say {self.sound}")
class dog (animal):  
    def speak(self):
        print(f"{self.name} say woof")
class cat(animal):
    def speak(self):
      print(f"{self.name} say meow")
d1 =dog("tomy" ,"woof")
c1 =cat("kitty","meow")
d1.speak()
c1.speak()