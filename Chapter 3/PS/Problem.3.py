# Write a program to detect double space in a string

name = "Alok is an amazing  person"  # String with double space
print(name.find("  "))  # Find the index of double space, returns -1 if not found
# if output is -1 that means double space is not found, any other number means double space is found at that index



# or
string = "Hello  World"  # String with double space
if "  " in string:
    print("Double space found!")
else:
    print("No double space found.")