#school = str(input("Enter your school name: "))
#school = school.strip().lower()

def setup():
    while school != "namanjalala":
        print("Enter a valid school name")
        school = str(input("Enter your school name: "))

    print("Woow good you got it!!! {}".format(school))

from random import randint

def game_loop():
    while True:
        target_random = randint(20,30)
        user_input = int(input("Guess a number between 20 and 30: "))
        if user_input > target_random:
            print(f"Too high, guess a lower number than {user_input}")
        elif user_input < target_random:
            print(f"Too low, please guess a higher number than {user_input}")
        else:
            print("Woow you got it !!!")
            break

if __name__ == "__main__":
    game_loop()