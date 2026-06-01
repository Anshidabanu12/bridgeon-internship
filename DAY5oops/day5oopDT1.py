class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self,owner,balance =0):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self,amount):
        self.balance =+ amount
        self.history.append(f"deposit:{amount}")
    def withdraw(self,amount):
        if(amount > self.balance):
            raise InsufficientFundsError("insufficient balance")
        self.balance -= amount
        self.history.append(f"withdraw:{amount}")
    def get_balance(self):
       return self.balance
    def transaction_history(self):
        for transaction in self.history:
            print(transaction)
    def __str__(self):  
        return f"owner:{self.owner} balance:{self.balance}"
class savingsAccount(BankAccount):
        def __init__(self,owner,balance,interest_rate):
            super().__init__(owner,balance)
            self.interest_rate = interest_rate
        def apply_interest(self): 
            interest = self.balance * self.interest_rate / 100
            self.history.append(f"interest added : {interest}")

class CurrentAccount(BankAccount):
        def __init__(self,owner,balance,overdreaft_limit):
             super().__init__(owner,balance)
             self.overdreaft_limit = overdreaft_limit
        def withdraw(self, amount):
             return super().withdraw(amount)
        def withdraw (self,amount):
             if(self.balance-amount <- self.overdreaft_limit):
               raise InsufficientFundsError("overdraft limit exceeded")
             self.balance -= amount
             self.history.append(f"withdraw:{amount}") 
             
print("\n BankAccount")
acc = BankAccount("sara",500000)
acc.deposit(1000000)
acc.withdraw(500) 
print(acc)
print("Balance :",acc.get_balance())

print("\n transaction history :")
acc.transaction_history()

print("\n SAVINGS ACCOUNT")
sav = savingsAccount("sara",2000,1)

print("befor intrest:",sav.get_balance())
sav.apply_interest()
print("after intrest:", sav.get_balance())
print("\n transaction history :")
sav.transaction_history()

print("\n CURRENT ACCOUNT")
cur = CurrentAccount("tom",1000000,500)
cur.withdraw(1200)
print(cur)
print("balance :",cur.get_balance())

print("\n transaction history :")
cur.transaction_history()

print("\n ERROR TESTS")
try:
    acc.withdraw(5000)
except InsufficientFundsError as e :
    print("Error :",e)
try:
    cur.withdraw(1000)
except InsufficientFundsError as e:
    print("Error :",e)