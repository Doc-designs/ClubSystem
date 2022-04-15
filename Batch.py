
from Member import * 

class Batch():
    def __init__(self, name, date, instructor, sizeCap):
        self.name = name
        self.date = date
        self.instructor = instructor
        self.sizeCap = sizeCap
        self.currentSize = 0
        self.students = []
        self.announcements = []
        self.functions = ["Enroll"]


    def get_batch(self):
        return self.students #returns a list of members currently enrolled in the batch
    
    def enroll(self, Member): #enrolls member to the Batch, adds member object to the students list
        self.students.append(Member)
        self.currentsize ++
    
    def isFull()
        return self.currentsize == self.sizeCap
