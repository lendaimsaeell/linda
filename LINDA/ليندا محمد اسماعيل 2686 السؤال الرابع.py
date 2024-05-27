class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount 
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
           return "Insufficient funds"
        self.balance -= amount
        return self.balance 
    def get_balance(self): 
        return self.balance 
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate 
        self.balance += interest_amount
        return interest_amount
    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nCurrent Balance: ${self.balance}\nInterest Rate: {self.interest_rate}" 
    
my_savings_account = SavingsAccount("777777", "lole", interest_rate=0.02) 
my_savings_account.deposit(1000.0) 
interest_amount = my_savings_account.apply_interest() 
print(f"Interest applied: ${interest_amount}") 
print(my_savings_account)
