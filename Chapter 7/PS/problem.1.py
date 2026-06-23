# Write a program to print multiplication table of a given number using for loop

n = int(input("Enter a number: ")) # input() takes input as a string. int() converts it into an integer.

for i in range(1, 11):    # range(start, stop)   # start to stop-1
    print(f"{n} x {i} = {n * i}")

# f before a string creates an f-string (formatted string literal).
# Anything inside {} is evaluated and its value is inserted into the string.