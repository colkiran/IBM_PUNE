
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        self.__price = val

    def delete_price(self):
        self.__price = 0

    price = property(get_price, set_price, delete_price)

coke = Product(150)

print(coke.price)

coke.price = 110

print(coke.price)

del coke.price
print(coke.price)






coke = Product(150)
# print(coke.)