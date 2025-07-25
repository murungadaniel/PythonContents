##### Inheritance is a way of creating a new class for using details of an existing class without modifying it.######

# Base class
class Animal:

    def eat(self):
        print("I can eat!!!")
    
    def sleep(self):
        print("I can sleep")

# Derived class
class Dog(Animal):

    def bark(self):
        print("I can bark! woof woof!!")


# create object of the Dog class
dog1 = Dog()

# calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark()