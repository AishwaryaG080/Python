class BankAccount():
    ROI=10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposite(self):
        deposite_amount=float(input("Enter the amount to deposite: "))
        if deposite_amount > 0:
            self.amount += deposite_amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    
    def calculateinterest(self):
        intrest=(self.amount*self.ROI)/100
        return intrest

    def display(self):
        print(f"Account Holder Name : {self.name}")
        print(f"Account Balance     : ₹{self.amount}")
       

account1 = BankAccount("Aishwarya", 15000)
account2 = BankAccount("Guruprasad", 20000)


account1.display()
account2.display()


print("Operations for Account 1")
account1.deposite()
account1.withdraw()
account1.display()
print(f"Interest: ₹{account1.calculateinterest()}")


print("\nOperations for Account 2")
account1.deposite()
account1.withdraw()
account1.display()
print(f"Interest: ₹{account2.calculateinterest()}")



      