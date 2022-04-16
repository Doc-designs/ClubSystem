from User import *
from Treasurer import *
from Coach import *
from Batch import *
Users = [] # For storing the Users instances
Batches = [] # For storing the Batch instances
def main():
    #Test User
    Users.append(Treasurer("Tom", "abc123", "6102534533", "Treasurer"))
    Users.append(Member("John", "abc123", "63344", "Member"))
    Users.append(Member("Bob", "abc123", "63424", "Member"))
    Users[0].addMember(63344)
    Users[0].addMember(63424)
    #Welcome Message
    print("Welcome to the Club Digital System")
    print("If you are a returning Users, enter your Username and password,\nOtherwise Type 'Create'")
    #username
    username = input("Please Enter Your Username: ")
    #If new User
    if(username == "Create"):
        name = input("Please Enter Your Name: ")
        contactInfo = input("Please Enter Your Contact Information, This will be used as your Account's Username: ")
        password = input("Please Enter Your Password: ")
        authority = input("Please Enter Your Account Type(Ex: Member, Coach, or Treasurer): ")
        #add to Users List
        Users.append(Users(name, password, contactInfo, authority))
    #Otherwise accept password
    else:
        password = input("Please Enter Your Password: ")
    #Check Existing Users
    for i in range(len(Users)):
        #If User Exists
        if(Users[i].contactInfo == username and Users[i].password == password):
            name = Users[i].name
            authority = Users[i].authority
            print("Welcome " + name)
            Batches = Users[i].batchesList
            if(authority == "Member"):
                for batch in Batches:
                    Users[i].receiveAnnouncements(batch)
            #While Logged In
            while True:
                print(Users[i].getFunction())
                userInput = input("What would you like to do?: ")
                #Signout
                if userInput == "MemberPay":
                    info = input("Please enter that user's contact Info: ")
                    payment = input("How much money do they need to pay?: ")
                    paid = payToTreasurer(info, int(payment))
                    print("User paid:", int(paid))
                else:
                    #Input Users Function
                    Users[i].useFunction(userInput, Users, Batches)
                    
#Below function is used to set a variable to a treasurer object
def findTreasurer():
    for x in Users:
        if x.getAuthority() == "Treasurer":
            return x

#Below function checks to see if payee has a discount and applies, it
#Function then takes discounted amount and takes it from the payee, and gives it the treasurer revenue
def payToTreasurer(Payee, Amount):
    treasurer = findTreasurer()
    discountedAmount = Amount * (1-treasurer.applyDiscount(Payee))
    Payee.pay(discountedAmount)
    treasurer.addRevenue(Payee, discountedAmount)
    return discountedAmount
    
  
if __name__ == "__main__":
    main()
