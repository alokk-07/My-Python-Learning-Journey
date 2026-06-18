# Write a program to input eight numbers from the user and display all the unique numbers (once).
s = set()
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
n= input("Enter number : ")
n= input("Enter number : ")
n= input("Enter number : ")
n= input("Enter number : ")
n= input("Enter number : ")
n= input("Enter number : ")

print(s)


# or
'''s = {
    int(input("Enter number 1: ")),
    int(input("Enter number 2: ")),
    int(input("Enter number 3: ")),
    int(input("Enter number 4: ")),
    int(input("Enter number 5: ")),
    int(input("Enter number 6: ")),
    int(input("Enter number 7: ")),
    int(input("Enter number 8: "))
}

print("Unique numbers are:", s)'''