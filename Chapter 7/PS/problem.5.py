# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))
i = 1     # We start from 1 because natural numbers begin with 1.
sum = 0   # Initially no numbers have been added, so sum is 0.
while(i<=n):     #The loop continues until i becomes greater than n
    sum += i   # sum = sum + i (Compound Assignment Operator)
    i += 1     # It increases the value of i by 1 after every iteration.(Increment Operator)

print(sum)
