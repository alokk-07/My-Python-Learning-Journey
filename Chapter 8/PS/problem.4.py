# Write a recursive function to calculate the sum of first n natural numbers.


'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4

sum(n)=1+2+3+4+.........+n-1+n
sum(n)=sum(n-1)+n

'''

def sum(n):
    if(n==1):   # In recursion, a base case stops the function from calling itself forever.
        return 1
    return sum(n-1)+n

print(sum(4))


'''
A recursive function has two important parts:
Base Case → Stops recursion.
if n == 1:
    return 1
Recursive Case → Function calls itself.
return sum(n-1) + n

Without the base case, the function would keep calling itself forever and cause a RecursionError.
'''