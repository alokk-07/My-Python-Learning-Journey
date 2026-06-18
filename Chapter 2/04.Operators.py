#1.Arithmetic Operators

a=10
b=5
print(a+b) # Addition
print(a-b) # Subtraction    
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Floor Division
print(a%b) # Modulus
print(a**b) # Exponentiation

#2.Assignment Operators

a=4-3 # a is assigned the value of 1
print(a)
b=6
b+=3 # Increment the value of b by 3, and then assign it to b 
print(b) 
c=10
c-=2 # Decrement the value of c by 2, and then assign it to c
print(c)

#3.Comparison Operators

d= 5<=5 # Less than or equal to
print(d) 

e= 10>5 # Greater than
print(e)

f= 3==3 # Equal to
print(f)

g= 4!=5 # Not equal to
print(g)        

h= 7>=6 # Greater than or equal to
print(h)

i= 2<1 # Less than
print(i)

#4.logical operators

j= True and False # Logical AND
print(j)
k= True or False # Logical OR
print(k)
l= not True # Logical NOT
print(l)

# Truth table for OR operator
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

# Truth table for AND operator
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

# Truth table for NOT operator
print("not True:", not True)
print("not False:", not False)


#5.Identity Operators
x= [1, 2, 3]
y= [1, 2, 3]
print(x is y) # False, because x and y are different objects in memory
print(x == y) # True, because x and y have the same content 
z= x
print(x is z) # True, because x and z refer to the same object in memory        

#6.Membership Operators
my_list= [1, 2, 3, 4, 5]    
print(3 in my_list) # True, because 3 is an element of my_list
print(6 in my_list) # False, because 6 is not an element of my_list
print(2 not in my_list) # False, because 2 is an element of my_list
print(7 not in my_list) # True, because 7 is not an element of my_list  

#7.Bitwise Operators
a= 5 # In binary: 0101
b= 3 # In binary: 0011  
print(a & b) # Bitwise AND: 0101 & 0011 = 0001 (1 in decimal)
print(a | b) # Bitwise OR: 0101 | 0011 =
# 0111 (7 in decimal)
print(a ^ b) # Bitwise XOR: 0101 ^ 0011 =
# 0110 (6 in decimal)
print(~a) # Bitwise NOT: ~0101 = 1010 (in two's complement, -6 in decimal)
print(a << 1) # Bitwise left shift: 0101 << 1 = 1010 (10 in decimal)
print(a >> 1) # Bitwise right shift: 0101 >> 1 =
# 0010 (2 in decimal)


