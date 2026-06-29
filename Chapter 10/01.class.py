class Employee:   
    language = "Python"  # class attribute
    salary = 2000000

alok = Employee()
alok.name = "Alok" # object/instance attribute
print(alok.language, alok.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.salary, rohan.language)

# Here name is object/instance attribute 
# salary and language are class attributes as they directly belong to the class