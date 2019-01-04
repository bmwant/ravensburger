from game import Resource, ResourceType, Invention, InventionType
from game import Coin, Point, War


class Stage(object):
    def __init__(self, *, rewards, price):
        self.rewards = rewards
        self.price = price
        self.finished = False


class Location(object):
    def __init__(
            self, *, name, resource, stages=None,
    ):
        self.name = name
        self.resource = resource
        self.stages = stages

    def __str__(self):
        return f'Location {self.name}'


locations_a = [
    Location(
        name='BABYLON',
        resource=Resource(produce=[ResourceType.CLAY]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.CLAY, ResourceType.CLAY],
            ),
            Stage(
                rewards=[
                    Invention(
                        inventions=[
                            InventionType.RUNES,
                            InventionType.METER,
                            InventionType.GEAR,
                        ]
                    )
                ],
                price=[
                    ResourceType.WOOD,
                    ResourceType.WOOD,
                    ResourceType.WOOD,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.CLAY,
                    ResourceType.CLAY,
                    ResourceType.CLAY,
                    ResourceType.CLAY,
                ],
            )
        ],
    ),
    Location(
        name='ALEXANDRIA',
        resource=Resource(produce=[ResourceType.GLASS]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.STONE, ResourceType.STONE],
            ),
            Stage(
                rewards=[
                    Resource(
                        produce=[
                            ResourceType.CLAY,
                            ResourceType.ORE,
                            ResourceType.WOOD,
                            ResourceType.STONE,
                        ]
                    )
                ],
                price=[
                    ResourceType.ORE,
                    ResourceType.ORE,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.GLASS,
                    ResourceType.GLASS,
                ],
            )
        ],
    ),
    Location(
        name='OLYMPIA',
        resource=Resource(produce=[ResourceType.WOOD]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.WOOD, ResourceType.WOOD],
            ),
            Stage(
                rewards=[
                    # todo (misha): tbd
                ],
                price=[
                    ResourceType.STONE,
                    ResourceType.STONE,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.ORE,
                    ResourceType.ORE,
                ],
            )
        ],
    ),
    Location(
        name='HALIKARNASSOS',
        resource=Resource(produce=[ResourceType.TEXTILE]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.CLAY, ResourceType.CLAY],
            ),
            Stage(
                rewards=[
                    # todo (misha): tbd
                ],
                price=[
                    ResourceType.ORE,
                    ResourceType.ORE,
                    ResourceType.ORE,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.TEXTILE,
                    ResourceType.TEXTILE,
                ],
            )
        ],
    ),
    Location(
        name='GIZAH',
        resource=Resource(produce=[ResourceType.STONE]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.STONE, ResourceType.STONE],
            ),
            Stage(
                rewards=[Point(value=5)],
                price=[
                    ResourceType.WOOD,
                    ResourceType.WOOD,
                    ResourceType.WOOD,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.STONE,
                    ResourceType.STONE,
                    ResourceType.STONE,
                    ResourceType.STONE,
                ],
            )
        ],
    ),
    Location(
        name='EPHESOS',
        resource=Resource(produce=[ResourceType.PAPYRUS]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.STONE, ResourceType.STONE],
            ),
            Stage(
                rewards=[Coin(value=9)],
                price=[
                    ResourceType.WOOD,
                    ResourceType.WOOD,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.PAPYRUS,
                    ResourceType.PAPYRUS,
                ],
            )
        ],
    ),
    Location(
        name='RHODOS',
        resource=Resource(produce=[ResourceType.ORE]),
        stages=[
            Stage(
                rewards=[Point(value=3)],
                price=[ResourceType.WOOD, ResourceType.WOOD],
            ),
            Stage(
                rewards=[War(value=2)],
                price=[
                    ResourceType.CLAY,
                    ResourceType.CLAY,
                    ResourceType.CLAY,
                ],
            ),
            Stage(
                rewards=[Point(value=7)],
                price=[
                    ResourceType.ORE,
                    ResourceType.ORE,
                    ResourceType.ORE,
                    ResourceType.ORE,
                ],
            )
        ],
    ),
]
