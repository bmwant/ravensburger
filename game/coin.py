

class Coin(object):
    def __init__(self, value):
        self.value = value


class Discount(object):
    def __init__(self, price, items=None,
                 left: bool=False, right: bool=False):
        self.price = price
        self.left = left
        self.right = right
        self.items = items or []
