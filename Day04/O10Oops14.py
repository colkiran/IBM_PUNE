
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    @price.deleter
    def price(self):
        self.__price = 0

pepsi = Product(140)

print(pepsi.price)

pepsi.price = 200

print(pepsi.price)

del pepsi.price
print(pepsi.price)
