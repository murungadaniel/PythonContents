import sys

# print("hello, my name is",sys.argv[1])

# try:
#     print("hello, my name is",sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv)  > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is",sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv)  > 2:
#     sys.exit("Too many arguments")
# print("hello, my name is",sys.argv[1])


#Accepting multiple arguments from the command line
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is",arg,end=" ")