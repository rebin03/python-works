class Bank:

    def create_acc(self, acc_no, acc_type):
        self.bank_name = "SBI"
        self.__balance = 2000
        self.acc_no = acc_no
        self.acc_type = acc_type
        print("Account created")
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"Your {self.bank_name} Account with {self.acc_no} has been credited with {amount}/- Rs")
        
    def withdraw(self, amount):
        if amount > self.__balance:
            return print(f"Transaction failed. Insufficient balance")
        self.__balance -= amount
        print(f"Your {self.bank_name} Account with {self.acc_no} has been debited an amount of {amount}/- Rs")
        
    def get_balance(self):
        print(f"Available balance is: {self.__balance} Rs")
    
sbi = Bank()

sbi.create_acc(76767876, "savings")
sbi.get_balance()
sbi.deposit(1000)
sbi.get_balance()
sbi.withdraw(2000)
sbi.get_balance()

# print(sbi.__balance)