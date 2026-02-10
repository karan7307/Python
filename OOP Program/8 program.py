#Enhance your coding skills, start writing your code here!!
class Vault:
    def __init__(self, vault_id, balance):
        self.__vault_id = vault_id
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def display_vault(self):
        return f"Vault {self.__vault_id}: Balance {self.__balance}"


n = int(input())
vaults = []

for _ in range(n):
    vid, bal = input().split()
    bal = int(bal)
    vaults.append(Vault(vid, bal))

q = int(input())
for _ in range(q):
    parts = input().split()
    op = parts[0]
    idx = int(parts[1]) - 1
    amount = int(parts[2])

    if op == "deposit":
        vaults[idx].deposit(amount)
    elif op == "withdraw":
        vaults[idx].withdraw(amount)

for v in vaults:
    print(v.display_vault())
