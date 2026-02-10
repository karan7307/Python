#Enhance your coding skills, start writing your code here!!
class InventoryItem:
    def __init__(self, item_name):
        self.__item_name = item_name
        self.__stock = 0

    def restock(self, quantity):
        if quantity > 0:
            self.__stock += quantity

    def sell(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return self.__stock
        else:
            return "Insufficient stock"

    def get_stock(self):
        return self.__stock

    def get_item_name(self):
        return self.__item_name


item_name = input()
n = int(input())

item = InventoryItem(item_name)

for _ in range(n):
    op = input().split()
    command = op[0]
    qty = int(op[1])

    if command == "restock":
        item.restock(qty)
    elif command == "sell":
        result = item.sell(qty)
        print(result)
