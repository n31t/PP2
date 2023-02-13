class Account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def checkBal(self):
        print(f"Balance is {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} - has been deposited")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money on your balance")
        else:
            self.balance -= amount
            print(f"{amount} - has been withdrawn from deposit")


acc = Account("Amir")
acc.checkBal()
acc.deposit(5000)
acc.checkBal()
acc.withdraw(2000)
acc.checkBal()
acc.withdraw(200000)
