#Enhance your coding skills, start writing your code here!!
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        print(f"Balance after deposit: {self.__balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Balance after withdrawal: {self.__balance}")
        else:
            print("Withdrawal failed: Insufficient funds")


deposit_amount = int(input())
withdraw_amount = int(input())

account = BankAccount()
account.deposit(deposit_amount)
account.withdraw(withdraw_amount)
