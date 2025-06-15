import file_two
from file_two import add,function_two

# Python file one module
print("File one __name__ is set to: {}" .format(__name__))

result = add(30,40)
print(result)


if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
else:
   print("File two executed when imported")