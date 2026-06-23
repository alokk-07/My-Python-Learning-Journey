# Write a program to print the following star pattern.
'''
  *
 ***
***** 
for n = 3'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")  # Printing Spaces
    print("*"* (2*i-1), end="")  # 2*i - 1 (generates odd numbers).
    # This creates the pyramid shape.
    # Both outputs stay on the same line, allowing spaces and stars to form one row of the pyramid before print("") moves to the next line.

    print("")
    

'''Pattern Formula to Remember
Spaces = n - i
Stars = 2*i - 1
These two formulas are the key to most pyramid-pattern questions.'''


