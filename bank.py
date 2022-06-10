from typing_extensions import Self
from unicodedata import decomposition, name

class Account:
    bank_name = "Equity"
    def __init__(self,account_number,name) :
        self.account_number = account_number
        self.account_balance = 0
        self.name = name
        self.deposits=[]
        self.withdrawals=[]
        
    def deposit(self,amount):

        if amount<=0:
            return amount>0
        else:
            self.account_balance+=amount
        return f"my deposit is {self.deposits} on the account {self.account_number} . The balance is {self.account_balance}"

    def withdraw(self,amount):
            self.transaction=100

            if amount>self.account_balance:
              return f"Insufficient funds"
            elif amount<=0:
                return f"Insufficient funds"
            else:
                self.withdraw-=amount
                return f"Hello{self.name}  you have withdrawn {self.withdrawals} and the balance is {self.account_balance} "
            
    def deposits_statement(self):
        for x in self.desposits:
            print(x,end="\n")
    def withdrawals_statement(self):
        for k in self.withdrawals:
            print(k,end="\n")
    def current_balance(self):
        return f"Hello {Self.name} ,your current balance is {self.account_balance}"
       
            
            