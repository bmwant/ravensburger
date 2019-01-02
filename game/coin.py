

class Coin(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        return self.__class__(self.value+other.value)


class Discount(object):
    def __init__(self, price, items=None,
                 left: bool=False, right: bool=False):
        self.price = price
        self.left = left
        self.right = right
        self.items = items or []
