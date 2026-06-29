# Can you change the self-parameter inside a class to something else (say “harry”). 
# Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def bookTicket(self, runningFrom , runningTo):
        print(f"Ticket is booked in train no : {self.trainNo} from {runningFrom} to {runningTo}")

    def getStatus(self,):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self, runningFrom, runningTo):
        print(f"Ticket fare in train no : {self.trainNo} from {runningFrom} to {runningTo} is {randint (222, 5555)}")



t = Train(15097)
t.bookTicket("Lukhnow", "Delhi")
t.getStatus()
t.getFare("Lukhnow", "Delhi")



# Yes. self is just a convention, not a keyword in Python. 
# You can replace it with any valid variable name like slf, harry, obj, etc.

#__________________________________________________________

'''
The first parameter of every instance method always refers to the current object.
Using self is recommended because it follows Python coding standards (PEP 8) and makes code easier to understand.

Example:

class Train:
    def __init__(harry, trainNo):
        harry.trainNo = trainNo

This works exactly the same as using self.
Using self makes your code easier for other Python programmers to read and maintain.

'''