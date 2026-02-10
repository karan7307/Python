#Enhance your coding skills, start writing your code here!!
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit Successful: {self.__balance}")
        else:
            print("Deposit Failed")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal Successful: {self.__balance}")
        else:
            print("Withdrawal Failed")

initial_balance = int(input())
deposit_amount = int(input())
withdrawal_amount = int(input())

account = BankAccount(initial_balance)

account.deposit(deposit_amount)
account.withdraw(withdrawal_amount)
