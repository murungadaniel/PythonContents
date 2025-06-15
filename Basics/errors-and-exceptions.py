# Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it.
# Errors detected during execution are called exceptions and are not unconditionally fatal

# mult = 10 * (1/0)
# print(mult)
# This will generate ZeroDivisionError

# add = '2' + 2
# print(add)
# This will generate TypeError

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError as ve:
        print("Oops!  That was not a valid number. Try again...",ve)

