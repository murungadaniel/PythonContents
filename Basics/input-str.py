name = input("What is your name? ")
#remove the extra space from the left and to the right of the string
name =  name.strip().title()
print("Hello,",name)


#spliting users name into first name and second name
first,last = name.split(" ")
print("Hello, ",first)

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break