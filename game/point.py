from enum import Enum


class Point(object):
    def __init__(self, value):
        self.value = value


class InventionType(Enum):
    RUNES = 'runes'
    GEAR = 'gear'
    METER = 'meter'


class Invention(object):
    def __init__(self, invention_type):
        self.invention_type = invention_type


class War(object):
    def __init__(self, amount):
        self.amount = amount
