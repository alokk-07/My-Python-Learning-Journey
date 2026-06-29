class Employee:   
    language = "Python"  # language:class attribute
    salary = 2000000

    def __init__(self, name, salary, language):  # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod       # it is a decorator
    def greet():        # greet is a static method and doesn't need object.
        print("Good morning")

alok = Employee("Alok", 1200000, "Java")
# alok.name = "Alok"
print(alok.name, alok.salary)

#rohan = Employee()


# __init__ dunder method will be called whenever object created.