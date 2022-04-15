from User import *

class Coach(User):
  #Class Init
  def __init__(self, name, password, contactInfo, authority):
    #Inherit
    super().__init__(name, password, contactInfo, authority)
    #Useable Functions
    self.functions = ["Balance", "Create Announcement", "Message Student", "Pay", "Members"]
    self.batchList = []
    self.selectedBatch
  #Find Batch
  def findClass(self):
    userInput = input("Please Enter the Date of the Batch (yy/mm/dd)")
    for batch in self.batchList:
      if(batch.date == userInput):
        return batch
  def classAnnouncement(batch, message):
    batch.append(message)
  def messageStudent(batch, name, message):
    for student in batch.get_batch():
      if(name == student.name.lower()):
        student.messagesReceived.append(message)
  def getFunction(self):
    return self.functions
  def useFunction(self, userInput, Users, Batches):
    #Balance
    if(userInput.lower() == functions[0].lower()):
      print(self.balance)
    #Hire
    elif(userInput.lower() == functions[1].lower()):
      self.selectedBatch = self.findClass()
      self.classAnnouncements()
    #Message
    elif(userInput.lower() == functions[2].lower()):
      self.selectedBatch = self.findClass()
      studentName = input("Please Enter the Students Name: ")
      message = input("Please enter your message: ")
      self.messageStudent(selectedBatch, studentName, message)
    #Pay
    elif(userInput.lower() == functions[3].lower()):
      self.Pay()
    #Members List
    elif(userInput.lower() == functions[4].lower()):
      self.Members()
    #Invalid
    else:
      print("Invalid user input")
