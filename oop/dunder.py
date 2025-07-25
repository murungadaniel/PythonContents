######### dunder methods starts with __ and ends with ___

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    # Instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self,sound):
        return f"{self.name} says {sound}"
    

miles = Dog("Miles",4)
# print(miles.description())
print(miles.speak("woof woof"))
print(miles)