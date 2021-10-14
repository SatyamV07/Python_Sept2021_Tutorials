a = "Super Python"
b = ["Super", "Python"]
print(len(a))
print(a.__len__())

# print(dir(str))
print(b[0])
print(b.__getitem__(0))

# print(dir(list))


class Order:
    def __init__(self, cart, customer) -> None:
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)


order = Order(["banana", "apple", "mango"], "Super Python")
print(len(order))
print(order.cart)
order = order + "mango"
print(order.cart)
