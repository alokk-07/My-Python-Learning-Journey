# An attribute that belongs to the class rather than a particular object
class Employee:   
    language = "Python"  # class attribute
    salary = 2000000


# Instance attributes, take preference over class attributes during assignment & retrieval
alok = Employee()
alok.language = "java" # object/instance attribute
print(alok.language, alok.salary)

