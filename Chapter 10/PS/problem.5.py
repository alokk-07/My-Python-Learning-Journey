# Write a Class ‘Train’ which has methods to book a ticket, 
# get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, runningFrom , runningTo):
        print(f"Ticket is booked in train no : {self.trainNo} from {runningFrom} to {runningTo}")

    def getStatus(self,):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self, runningFrom, runningTo):
        print(f"Ticket fare in train no : {self.trainNo} from {runningFrom} to {runningTo} is {randint (222, 5555)}")



t = Train(15097)
t.bookTicket("Lukhnow", "Delhi")
t.getStatus()
t.getFare("Lukhow", "Delhi")