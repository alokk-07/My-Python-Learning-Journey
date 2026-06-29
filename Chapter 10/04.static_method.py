class Employee:   
    language = "Python"  # language:class attribute
    salary = 2000000


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod       # it is a decorator
    def greet():        # greet is a static method and doesn't need object.
        print("Good morning")

alok = Employee()
# alok.language = "JavaScript"  # This is an instance attribute.
alok.greet()
alok.getInfo()  
# Employee.getInfo(alok)