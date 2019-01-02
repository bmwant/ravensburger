from enum import Enum


class ResourceType(Enum):
    CLAY = 'clay'
    ORE = 'ore'
    STONE = 'stone'
    WOOD = 'wood'
    GLASS = 'glass'
    TEXTILE = 'textile'
    PAPYRUS = 'papyrus'


class Resource(object):
    def __init__(self, produce):
        self.produce = produce


resources = [
    Resource(produce=[ResourceType.ORE]),
    Resource(produce=[ResourceType.ORE]),
]
