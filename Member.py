from User import *

class Member(User):
    def __init__(Balance, PaymentDue, Attendance, TotalClasses):
        Balance.balance = balance
        Balance.PaymentDue = PaymentDue
        Balance.Attendance = Attendance
        Balance.TotalClasses = TotalClasses

    def Balance():
        if selection == 1:
        if intial_balance > 1:
                print("\nAn account has already been open. Please select another option.")
                print(menu)
            else:
                name = input("\nEnter the account pwner's name: ")

                while True:
                    initial_balance = input("\nEnter your initial balance: $")
                    try:
                        initial_balance = float(initial_balance)
                    except ValueError:
                        print("\nDeposit more money.")
                              continue
                    if initial_balance < 1:
                        print("\nDeposit more money.")
                        continue
                    else:
                        balance += initial_balance
                        print("\nAnccount owner: " + name)
                        account = BankAccount(initial_balance)
                        print("\nInitial balance: $ " + str(initial_balance))
                        print(menu)
                        break
                    
    def PaymentDue():
        while True:
            date = input("\nWhen is your payment start date?")
            num_payments = input("\nHow many payments")
            
        if len(date) == 3:
            if not (date[0].isdigit() and date[1].isdigit() and date[2].isdigit()):
                print("\nWrong input. Try again.")

        else:
            print("\nTry again.")

        if int(num_payments.isdigit()):
            for i in range(1, int(num_payments) + 1):
                print(i, end=" ")
                print(date)

        else:
            print("\nInvalid input. Try again.")
            break

    def check(no_of_days, row_num, b):
        global staff_mails
        global 12
        global 13
        break

    def Attendance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.find("LLL") != -1:
            return False
        cntA = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cntA += 1
                if cntA > 1:
                   return False
        return True

    def TotalClasses():
        from collections import Counter
        classes = (
            ('V', 1),
            ('VI', 1),
            ('V', 2),
            ('VI', 2),
            ('VI', 3),
            ('VII', 1),
        )
        students = Counter(class_name for class_name, no_students in classes)
        print(students)
        
                        
        
