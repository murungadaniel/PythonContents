# try:
#     x = int(input("What is x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")


# while True:
#     try:
#         x = int(input("What is x? "))
#         break
#     except ValueError:
#         print("x is not an integer")

# print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x


# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x
    
def get_int():
    while True:
        try:
            x = int(input("What is x? "))
            return x
        except ValueError:
            print("x is not an integer")  

def main():
    x = get_int()
    print(f"x is {x}")

main()







