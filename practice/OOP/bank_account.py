class BankAccount:
    
    def __init__(self, acc_holder_name, balance = 0):
        self.acc_holder_name = acc_holder_name
        self.balance = balance
        
    def __str__(self):
        return f"Account Honder Name: {self.acc_holder_name}\nBalance: {self.balance}\n"
        
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposited {deposit_amount} to your account\n")
        
    def withdraw(self, withrdraw_amount):
        if self.balance >= withrdraw_amount:
            self.balance -= withrdraw_amount
            print(f"{withrdraw_amount} withdrew successfully.\n")
        else:
            print(f"Not enough balance!!\nAvailable balance is {self.balance}")
            

ac = BankAccount("Rebin", 12000)

print(ac)
ac.deposit(100)
ac.withdraw(12000)
print(ac)