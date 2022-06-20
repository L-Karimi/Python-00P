
from re import T
from datetime import datetime
# Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Update the deposit method to store each deposit transaction as a dictionary like this 
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }

# Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date and using a for loop prints each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000

# Add a new attribute loan_balance which is zero by default.

# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.

# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit

# Add a new method transfer which accepts two attributes (amount and instance of another account). If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.




class Account:
    bank_name = "Equity"
    def __init__(self,account_number,name) :
        self.account_number = account_number
        self.account_balance = 0
        self.name = name
        self.deposits=[]
        self.withdrawals=[]
        self.transaction= 100
        self.new_dict = {}
        self.loan_balance=0
    # def deposit(self,amount):

    #     if amount<=0:
    #         return amount>0
    #     else:
    #         self.deposits.append(amount)
    #         self.account_balance+=amount
    #     return f"my deposit is {self.deposits} on the account {self.account_number} . The balance is {self.account_balance}"

    # def withdraw(self,amount):
    #         transaction=100
    #         totalfee=amount+transaction

    #         if amount>self.account_balance:
    #           return f"Insufficient funds"
    #         elif amount<=0:
    #             return f"Insufficient funds"
    #         else:
    #             self.account_balance-=totalfee
    #             self.withdrawals.append(amount)
    #             return f"Hello{self.name}  you have withdrawn {self.withdrawals} and the balance is {self.account_balance} "
            
    # def deposits_statement(self):
    #     for x in self.deposits:
    #         print(x,end="\n")
    # def withdrawals_statement(self):
    #     for k in self.withdrawals:
    #         print(k,end="\n")
    # def current_balance(self):
    #     return f"Hello {self.name} ,your current balance is {self.account_balance}"
       
            
    

        
        
    def deposit(self,amount):
        now=datetime.now()
        if amount<=0:
            return f"deposit amount must be greater than 0 {now}"
        else:
            self.narration=f" hello {self.name} you have deposited {amount} and your new balance is  {self.balance}  {now}"
            self.balance+=amount
            self.deposits.append(amount)
            self.newdict["date"]=now
            self.newdict["amount"]=amount
            self.newdict["narration"]=self.narration
            return f" hello {self.name} confirmed you have deposited {amount} and your new balance is {self.balance} on  {now}"
    def withdrawa(self,amount):
        now=datetime.now()
        withdrawal_amount=amount+self.transaction
        if amount >self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return f"amount must be greater than 0"
        else:
            self.narration=f" hello  {self.name}  confirmed you have withdrawn {amount} your new balance is{self.balance} on{ now}" 
            self.balance-=withdrawal_amount
            self.withdrawals.append(amount)
            self.newdict["date"]=now
            self.newdict["amount"]=amount
            self.newdict["narrations"]=self.narration

            
            return f" hello {self.name} you have withdrawn {amount} your new balance is {self.balance} on {now}"     
    def deposits_statement (self):
        now=datetime.now()
        for depo in self.deposits:
            print(f"You deposited {depo}  {now}")

    def withdrawal_statements(self):
         now=datetime.now()
         for witho in self.withdrawals:
            print(f" you have withdrawn {witho}  on {now}")     
    def total_balance(self):
        now=datetime.now()
        return f" your balance is {self.balance} on {now}"
    def full_statement(self):
        now=datetime.now()
        full=[self.deposits+self.withdrawals]
        for x in full:
            print(f"{now}{x}")
    def borrow(self,loan):
        sum=0
        for dep in self.deposits:
            sum+=dep
            print(sum)
        if len(self.deposits)<10:
            return f" you have more than 10 depoist and your loan is{loan}"
        elif loan>100:
            return f"you qualify for a loan"
        elif self.loan_balance==0:
            pass
            
        else:
            print("not qualified for a loan")    

              