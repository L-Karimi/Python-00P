from unicodedata import decomposition


class Account:
    bank_name = "Equity"
    def __init__(self,account_number,account_balance) :
        self.account_number = account_number
        self.account_balance = account_balance
    def deposit(self,account_balance):
        self.account_balance = account_balance
        
    def withdraw(self,accunt_balance):
        