from enum import Enum


class NumberLike(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        cls = self.__class__
        return cls(value=self.value+other.value)

    def __str__(self):
        return str(self.value)


class Point(NumberLike):
    """
    Winning points
    """


class InventionType(Enum):
    RUNES = 'runes'
    GEAR = 'gear'
    METER = 'meter'


class Invention(object):
    def __init__(self, inventions):
        self.inventions = inventions


class War(NumberLike):
    """
    Value representing war amount for the given location
    """


class WarPoint(NumberLike):
    """
    Points assigned at the end of each epoch when resolving a war
    """
