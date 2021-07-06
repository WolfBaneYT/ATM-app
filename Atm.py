import random

class ATM(object):
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def CashWithdrawal(self,amount):
        amount = input("Enter Amount to withdraw : ")
        print("Amount of "+str(amount)+" has been withdrawn from your bank account.")

    def BalanceEnquiry(self,balance):
        balance = random.randrange(1,500000)
        print("Remaining balance is "+str(balance)+"in your account.")
       

    def CashDeposit(self,amount):
        amount = input("Enter Amount to deposit : ")
        print("Amount of "+str(amount)+" has been deposited into your bank account.")

start=input("What would you like to do today? Type w to withdraw , d to deposit and b for balance enquiries : ")
print(start)

if(start=="w"):
    ATM.CashWithdrawal()

if(start=="d"):
    ATM.CashDeposit()

if(start=="b"):
    ATM.BalanceEnquiry()