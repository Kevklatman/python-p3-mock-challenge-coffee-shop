class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        if len(name) < 3:
            raise ValueError("Name must be more than 2 letters")
        self._name = name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if self.num_orders() == 0:
            return 0
        else:
            return sum([order.price for order in self.orders()]) / self.num_orders()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        return


class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in Order.all if order.customer == self))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        Order.all.append(order)
        return order

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            return

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            return None
        customers = [order.customer for order in coffee.orders()]
        if not customers:
            return None
        return max(customers, key=lambda c: sum(o.price for o in c.orders() if o.coffee == coffee))


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("not a customer")

        if not isinstance(coffee, Coffee):
            raise TypeError("not coffee")

        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1 dollar and 10 dollars")

        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        return
