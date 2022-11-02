class Ticket:

    def __init__(self, number, price=2):
        self.number = number
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError()
        if value < 0.0:
            raise ValueError()
        self._price = value

    def __str__(self):
        return f"{self.number} - {self.price}"


class Advance(Ticket):

    def __init__(self, number):
        super().__init__(number)
        self.price = self.price - self.price * 0.4


class Student(Ticket):

    def __init__(self, number):
        super().__init__(number)
        self.price = self.price - self.price * 0.5


class Late(Ticket):

    def __init__(self, number):
        super().__init__(number)
        self.price = self.price + self.price * 0.1


