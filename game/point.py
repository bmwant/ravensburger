from enum import Enum


class Point(object):
    def __init__(self, value):
        self.value = value


class InventionType(Enum):
    RUNES = 'runes'
    GEAR = 'gear'
    METER = 'meter'


class Invention(object):
    def __init__(self, inventions):
        self.inventions = inventions


class War(object):
    def __init__(self, amount):
        self.amount = amount
