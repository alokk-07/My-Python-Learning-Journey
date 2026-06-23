# Write a program to print the following star pattern.
'''
* * *
*   *     for n = 3
* * *
'''


n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):     # Checks whether the current row is: First row (i == 1).Last row (i == n)
        print("*"*n, end="")
    else:         # This block executes for the middle rows.
        print("*", end="")   # Prints the left boundary star.
        print(" "* (n-2), end="") # Spaces in Middle
        print("*", end="") # Prints the right boundary star.
    print("")  # Moves the cursor to the next line.

'''Key Logic to Remember

For a hollow square:

First row → all stars
Last row → all stars
Middle rows → star + spaces + star

Formula:

Spaces = n - 2'''