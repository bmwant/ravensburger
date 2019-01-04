
# todo (misha): number value
class Coin(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        return self.__class__(self.value+other.value)

    def to_points(self):
        return self.value // 3


class Discount(object):
    def __init__(self, price, items=None,
                 left: bool=False, right: bool=False):
        self.price = price
        self.left = left
        self.right = right
        self.items = items or []


# todo (misha): unify both
class CardMatch(object):
    def __init__(
            self, rewards, card_type,
            left: bool=False, bottom: bool=False, right: bool=False,
    ):
        self.rewards = rewards
        self.card_type = card_type
        self.left = left
        self.bottom = bottom
        self.right = right


class StageBonus(object):
    def __init__(
            self, rewards,
            left: bool=False, bottom: bool=False, right: bool=False,
    ):
        self.rewards = rewards
        self.left = left
        self.bottom = bottom
        self.right = right
