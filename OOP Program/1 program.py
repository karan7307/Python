#Enhance your coding skills, start writing your code here!!
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


initial = float(input())
deposit_amount = float(input())
withdraw_amount = float(input())

account = BankAccount(initial)
account.deposit(deposit_amount)
account.withdraw(withdraw_amount)

print(account.get_balance())
