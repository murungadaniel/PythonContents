class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

# instantiating objects
# ozzy = Dog("ozzy",2)
# print(ozzy)

# To access an object's attributes in Python, you can use the dot notation. 
# print(ozzy.name)
# print(ozzy.age)
# print(ozzy.name + " is " + str(ozzy.age) + " years old.")
# ozzy.bark()

# ozzy = Dog("Ozzy", 2)
# skippy = Dog("Skippy", 12)
# filou = Dog("Filou", 8)

# ozzy.doginfo()
# skippy.doginfo()
# filou.doginfo()

# ozzy.birthday()
# print(ozzy.age)
####################buddy#######

ozzy = Dog("Ozzy",2)
filou = Dog("Filour",80)

ozzy.setBuddy(filou)

########To get info about buddy
print(ozzy.buddy)
print(filou.buddy)

print(ozzy.buddy.name)
print(ozzy.buddy.age)

print(filou.buddy.name)
print(filou.buddy.age)

####### buddy's method can also be called ###############
print(filou.buddy.doginfo())
print(ozzy.buddy.doginfo())