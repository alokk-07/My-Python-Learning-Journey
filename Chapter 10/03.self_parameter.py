class Employee:   
    language = "Python"  # language:class attribute
    salary = 2000000

# self represents the object that calls this method.
# self must be the first parameter of an instance method
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("Good morning")

alok = Employee()
# alok.language = "JavaScript"  # This is an instance attribute.
alok.greet()
alok.getInfo()  # here : self becomes alok.
# Employee.getInfo(alok)