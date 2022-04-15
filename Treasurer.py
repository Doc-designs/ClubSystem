#Note whenever the Code refers to a member, it assumes that contact info was entered as a parameter
from User import *
class Treasurer(User):
    #Class Init
    def __init__(self, name, password, contactInfo, authority):
        #Inherit
        super().__init__(name, password, contactInfo, authority)

        self.memberList = []

        #Log of those who have paid in advance
        self.payList = []

        #Total Club balance
        self.clubBalance = 0.0

        #Various expenses are logged here
        self.hallCost = 0.0
        self.coachCost = 0.0
        self.otherCost = 0.0
        self.expenses = 0.0

        #Dictionary containing all members who have paid and the amount paid
        #Income and revenue is also logged in these variables
        self.memberPay = {}
        self.otherIncome = 0.0
        self.revenue = 0.0

        #Total profits for this month, and all previous month profits logged here
        self.profits = 0.0
        self.profitList = []

        #Total amount of debt
        self.debt = 0.0

        #Useable Functions
        self.functions = ["Signout", "Balance", "Hire", "Pay", "Members"]

    #Adds a member to the list of advance payment
    def addPaylist(self, payee, amount):
        self.payList.append(payee)
        self.memberPay[payee] = amount
        self.revenue += amount

    #Adds total revenue, second function adds other income
    def addRevenue(self, payee, amount):
        self.memberPay[payee] = amount
        self.revenue += amount
    def addOtherIncome(self):
        self.revenue += self.otherIncome

    #Returns current profit value
    def currentProfit(self):
        return self.revenue

    #Set various costs
    def setHallCost(self, amount):
        self.hallCost = amount
    def setCoachCost(self, amount):
        self.coachCost = amount
    def setOtherCost(self, amount):
        self.otherCost = amount

    #Set expenses for this month and retrieve them
    def setExpenses(self):
        self.expenses = self.coachCost + self.hallCost + self.otherCost
    def getExpenses(self):
        return self.expenses

    #Set profits for this month
    def setProfits(self):
        self.profits = self.revenue - self.expenses
        
    def debts(self):
        if self.profits < self.expenses:
            self.debt += self.expenses - self.profits
        return self.debt
    
    def payDebt(Amount):
        if self.debt == 0:
            print("There is no debt to pay")
        elif amount > self.debt:
            self.expenses += self.debt
            self.debt = 0.0
        else:
            self.expenses += amount
            self.debt -= amount

    #Below function creates the income statement
    def incomeStatement(self):
        print("Revenue:")
        for key in self.memberPay:
            print("Member", key +":\t", self.memberPay.get(key))
        print("Other Income:", self.otherIncome)
        print("Total Revenues:", self.revenue)
        print("\nExpenses:\nHall Costs:\t", self.hallCost,
              "\nCoach Cost:\t", self.coachCost)
        print("Total Expenses:", self.getExpenses())

        print("This month's profit:", self.profits)
        self.profitList.append(self.profits)

        print("Monthly Profits:")
        for x in range(len(self.profitList) - 1):
            print("Month", str(x+1) + ":", self.profitList[x])
            if x == len(self.profitList) - 2:
                print("Month", str(x+2) + "(Current Month):", self.profitList[x+1])
                
        print("Debt:", self.debts())

    #Two functions below are used to sort the member list
    #takePay sorts by the most payments
    def takePay(elem):
        return elem[1]
    #take Attendance sorts by the most attendances
    def takeAttendance(elem):
        return elem[2]
    
    #This function itself sorts the lists, depending on the sortType entered
    def SortMembers(self, sortType):
        sortList = self.memberList
        if sortType == "Paid":
            sortList.sort(key=self.takePay, reverse=True)
        elif sortType == "Attendance":
            sortList.sort(key=self.takeAttendance, reverse=True)
        return sortList

    #This function applys a discount, then resets that users pay value and attendance value
    def applyDiscount(self, member):
        discount = 0.0
        memTup = None
        for x in self.memberList:
            if member == x[0]:
                memTup = x

        sortList = self.SortMembers(self.memberList, "Paid")
        payFilter = filter(lambda x: x[1] == 3, sortList)
        payList = list(payFilter)
        for x in payList:
            if member == x[0]:
                discount += 0.10
                self.memberList.remove(x)
                memTup = (member, 0, memTup[2])
                self.MemberList.append(memTup)

        sortList = self.SortMembers(self.memberList, "Attendance")
        sortList = sortList[:10]
        for x in sortList:
            if member == x[0]:
                discount += 0.10
                self.memberList.remove(x)
                memTup = (member, memTup[1], 0)
                self.memberList.append(memTup)
        return discount


    def getFunction(self):
        return self.functions

    def useFunction(self, userInput):
        #Balance
        if(userInput.lower() == self.functions[1].lower()):
            print(self.balance)
        #Hire
        elif(userInput.lower() == self.functions[2].lower()):
            self.Hire()
        #Pay
        elif(userInput.lower() == self.functions[3].lower()):
            self.Pay()
        #List Members
        elif(userInput.lower() == self.functions[4].lower()):
            self.Members()
        #Invalid
        else:
            print("Invalid user input")
