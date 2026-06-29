# Create a class with a class attribute a; 
# create an object from it and set ‘a’ directly using ‘object.a = 0’. 
# Does this change the class attribute?

class Demo:
    a = 4

object= Demo()
print(object.a) # prints the class attribute because instance attribute is not present

object.a = 0  # Instance attribute is set
print(object.a) # Prints the instance attribute becuase instance attribute is present
print(Demo.a) # Prints the class attribute


# Ans : No , this does not change the class attribute

'''
a is a class attribute, shared by all objects of the class.
object.a = 0 creates an instance attribute for that object only.
It does not change the class attribute.
Demo.a remains unchanged.

Output
4
0
4

Conclusion
No, object.a = 0 does not change the class attribute. It only creates/updates the instance attribute for that specific object.
'''