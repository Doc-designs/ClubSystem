from User import *
from Batch import *

class Member(User):
    #Class Init
    def __init__(self, name, password, contactInfo, authority):
        #Inherit
        super().__init__(name, password, contactInfo, authority)
        #Useable Functions
        self.functions = ["Balance", "Schedule"]
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
    def Pay(self, Amount):
        #Subtract amount from self
        self.balance -= Amount
        #Return Amount being paid to its destination
        return Amount
    def Schedule(self, batch):
        #add batch to batch member's batch list and enroll student in batch function
        self.batchesList.append(batch)
        batch.enroll(self)
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
