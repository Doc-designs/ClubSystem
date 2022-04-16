from User import *
from Batch import *

class Member(User):
    #Class Init
    def __init__(self, name, password, contactInfo, authority):
        #Inherit
        super().__init__(name, password, contactInfo, authority)
        #Useable Functions
        self.functions = ["Balance", "Pay", "Schedule"]
        self.balance = 0
        self.attended = 0
        self.totalClasses = 0
        self.batchesList = []
        self.messagesReceived = []
        self.paymentDue = False
        self.willAttend = False
        self.discount = False
        self.penaltyFee = False
        self.termination = False
    def receiveAnnouncements(self, batch):
        for batch in self.batchesList:
            for announcement in batch.announcements:
                print(batch.name + ": " + announcement)
    def receiveMessages(self, batch):
        for batch in self.batchesList:
            for message in self.messagesReceived:
                print(batch.instructor + ": " + message)
    def Schedule(self, batches):
        for batch in batches:
            if not batch.isFull():
                print(batch.date)
        x = True
        while x:
            userInput = input("Please type in the date of the batch that is available: ")
            for batch in batches:
                if userInput == batch.date:
                    #add batch to batch member's batch list and enroll student in batch function
                    self.batchesList.append(batch)
                    self.totalClasses += 1
                    batch.enroll(self)
                    x = False
                    break
            print("No batch is found with such date")
        print("Scheduling successful")      
    def getFunction(self):
        return self.functions
    def useFunction(self, userInput, Users, Batches):
            #Balance
            if(userInput.lower() == self.functions[0].lower()):
                print(self.balance)
            #Schedule
            elif(userInput.lower() == self.functions[1].lower()):
                self.Schedule()
            #Invalid Input
            else:
                print("Invalid user input") 