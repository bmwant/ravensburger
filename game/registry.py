from game import Card, CardType, CardLink
from game import Resource, ResourceType, Invention, InventionType
from game import Point, Coin, Discount, War, WarPoint, CardMatch, StageBonus


cards_registry = [
    # epoch I
    ## brown
    Card(
        name='CLAY POOL',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=5,
        rewards=[Resource(produce=[ResourceType.CLAY])],
    ),
    Card(
        name='CLAY POOL',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.CLAY])],
    ),
    Card(
        name='ORE VEIN',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.ORE])],
    ),
    Card(
        name='ORE VEIN',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=4,
        rewards=[Resource(produce=[ResourceType.ORE])],
    ),
    Card(
        name='LUMBER YARD',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.WOOD])],
    ),
    Card(
        name='STONE PIT',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.STONE])],
    ),
    Card(
        name='STONE PIT',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=5,
        rewards=[Resource(produce=[ResourceType.STONE])],
    ),
    Card(
        name='LUMBER YARD',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=4,
        rewards=[Resource(produce=[ResourceType.WOOD])],
    ),
    Card(
        name='CLAY PIT',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        price=[Coin(value=1)],
        rewards=[Resource(produce=[ResourceType.CLAY, ResourceType.ORE])],
    ),
    Card(
        name='TREE FARM',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        price=[Coin(value=1)],
        rewards=[Resource(produce=[ResourceType.WOOD, ResourceType.CLAY])],
    ),
    Card(
        name='EXCAVATION',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=4,
        price=[Coin(value=1)],
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.CLAY])],
    ),
    Card(
        name='MINE',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        price=[Coin(value=1)],
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.ORE])],
    ),
    Card(
        name='FOREST CAVE',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=5,
        price=[Coin(value=1)],
        rewards=[Resource(produce=[ResourceType.WOOD, ResourceType.ORE])],
    ),
    Card(
        name='TIMBER YARD',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        price=[Coin(value=1)],
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.WOOD])],
    ),
    ## grey
    Card(
        name='LOOM',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.TEXTILE])],
    ),
    Card(
        name='LOOM',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        rewards=[Resource(produce=[ResourceType.TEXTILE])],
    ),
    Card(
        name='GLASSWORKS',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.GLASS])],
    ),
    Card(
        name='GLASSWORKS',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        rewards=[Resource(produce=[ResourceType.GLASS])],
    ),
    Card(
        name='PRESS',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.PAPYRUS])],
    ),
    Card(
        name='PRESS',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        rewards=[Resource(produce=[ResourceType.PAPYRUS])],
    ),
    ## blue
    Card(
        name='THEATER',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink('STATUE')],
        rewards=[Point(value=2)],
    ),
    Card(
        name='THEATER',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=6,
        chain_next=[CardLink('STATUE')],
        rewards=[Point(value=2)],
    ),
    Card(
        name='ALTAR',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=5,
        chain_next=[CardLink('TEMPLE')],
        rewards=[Point(value=2)],
    ),
    Card(
        name='ALTAR',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink('TEMPLE')],
        rewards=[Point(value=2)],
    ),
    Card(
        name='PAWNSHOP',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=4,
        rewards=[Point(value=3)],
    ),
    Card(
        name='PAWNSHOP',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=7,
        rewards=[Point(value=3)],
    ),
    Card(
        name='BATHS',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink('AQUEDUCT')],
        rewards=[Point(value=3)],
        price=[ResourceType.STONE],
    ),
    Card(
        name='BATHS',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=7,
        chain_next=[CardLink('AQUEDUCT')],
        rewards=[Point(value=3)],
        price=[ResourceType.STONE],
    ),
    ## green
    Card(
        name='APOTHECARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink(name='STABLES'), CardLink(name='DISPENSARY')],
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[ResourceType.TEXTILE],
    ),
    Card(
        name='APOTHECARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=5,
        chain_next=[CardLink(name='STABLES'), CardLink(name='DISPENSARY')],
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[ResourceType.TEXTILE],
    ),
    Card(
        name='WORKSHOP',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[
            CardLink(name='LABORATORY'),
            CardLink(name='ARCHERY RANGE'),
        ],
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[ResourceType.GLASS],
    ),
    Card(
        name='WORKSHOP',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=7,
        chain_next=[
            CardLink(name='LABORATORY'),
            CardLink(name='ARCHERY RANGE'),
        ],
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[ResourceType.GLASS],
    ),
    Card(
        name='SCRIPTORIUM',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink(name='COURTHOUSE'), CardLink(name='LIBRARY')],
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[ResourceType.PAPYRUS],
    ),
    Card(
        name='SCRIPTORIUM',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=4,
        chain_next=[CardLink(name='COURTHOUSE'), CardLink(name='LIBRARY')],
        rewards=[InventionType.RUNES],
        price=[ResourceType.PAPYRUS],
    ),
    ## red
    Card(
        name='STOCKADE',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[War(value=1)],
        price=[ResourceType.WOOD],
    ),
    Card(
        name='STOCKADE',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=7,
        rewards=[War(value=1)],
        price=[ResourceType.WOOD],
    ),
    Card(
        name='GUARD TOWER',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[War(value=1)],
        price=[ResourceType.CLAY],
    ),
    Card(
        name='GUARD TOWER',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=4,
        rewards=[War(value=1)],
        price=[ResourceType.CLAY],
    ),
    Card(
        name='BARRACKS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[War(value=1)],
        price=[ResourceType.ORE],
    ),
    Card(
        name='BARRACKS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=5,
        rewards=[War(value=1)],
        price=[ResourceType.ORE],
    ),
    ## yellow
    Card(
        name='TAVERN',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=4,
        rewards=[Coin(value=5)],
    ),
    Card(
        name='TAVERN',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=5,
        rewards=[Coin(value=5)],
    ),
    Card(
        name='TAVERN',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=7,
        rewards=[Coin(value=5)],
    ),
    Card(
        name='MARKETPLACE',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[
            Discount(
                price=1,
                items=[
                    ResourceType.GLASS,
                    ResourceType.TEXTILE,
                    ResourceType.PAPYRUS,
                ],
                left=True,
                right=True,
            )
        ],
        chain_next=[CardLink('CARAVANSERY')],
    ),
    Card(
        name='MARKETPLACE',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=6,
        rewards=[
            Discount(
                price=1,
                items=[
                    ResourceType.GLASS,
                    ResourceType.TEXTILE,
                    ResourceType.PAPYRUS,
                ],
                left=True,
                right=True,
            )
        ],
        chain_next=[CardLink('CARAVANSERY')],
    ),
    Card(
        name='WEST TRADING POST',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[
            Discount(
                price=1,
                items=[
                    ResourceType.CLAY,
                    ResourceType.STONE,
                    ResourceType.WOOD,
                    ResourceType.ORE,
                ],
                left=True,
            )
        ],
        chain_next=[CardLink('FORUM')],
    ),
    Card(
        name='WEST TRADING POST',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=7,
        rewards=[
            Discount(
                price=1,
                items=[
                    ResourceType.CLAY,
                    ResourceType.STONE,
                    ResourceType.WOOD,
                    ResourceType.ORE,
                ],
                left=True,
            )
        ],
        chain_next=[CardLink('FORUM')],
    ),
    Card(
        name='EAST TRADING POST',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[
            Discount(
                price=1,
                items=[
                    ResourceType.CLAY,
                    ResourceType.STONE,
                    ResourceType.WOOD,
                    ResourceType.ORE,
                ],
                right=True,
            )
        ],
        chain_next=[CardLink('FORUM')],
    ),
    Card(
        name='EAST TRADING POST',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=1,
        players_limit=7,
        rewards=[
            Discount(
                price=1,
                items=[
                    ResourceType.CLAY,
                    ResourceType.STONE,
                    ResourceType.WOOD,
                    ResourceType.ORE,
                ],
                right=True,
            )
        ],
        chain_next=[CardLink('FORUM')],
    ),
    # epoch II
    ## brown
    Card(
        name='QUARRY',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.STONE])],
        price=[Coin(value=1)],
    ),
    Card(
        name='QUARRY',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=4,
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.STONE])],
        price=[Coin(value=1)],
    ),
    Card(
        name='BRICKYARD',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.CLAY, ResourceType.CLAY])],
        price=[Coin(value=1)],
    ),
    Card(
        name='BRICKYARD',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=4,
        rewards=[Resource(produce=[ResourceType.CLAY, ResourceType.CLAY])],
        price=[Coin(value=1)],
    ),
    Card(
        name='FOUNDRY',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.ORE, ResourceType.ORE])],
        price=[Coin(value=1)],
    ),
    Card(
        name='FOUNDRY',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=4,
        rewards=[Resource(produce=[ResourceType.ORE, ResourceType.ORE])],
        price=[Coin(value=1)],
    ),
    Card(
        name='SAWMILL',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.WOOD, ResourceType.WOOD])],
        price=[Coin(value=1)],
    ),
    Card(
        name='SAWMILL',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=4,
        rewards=[Resource(produce=[ResourceType.WOOD, ResourceType.WOOD])],
        price=[Coin(value=1)],
    ),
    ## grey
    Card(
        name='PRESS',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.PAPYRUS])],
    ),
    Card(
        name='PRESS',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=5,
        rewards=[Resource(produce=[ResourceType.PAPYRUS])],
    ),
    Card(
        name='LOOM',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.TEXTILE])],
    ),
    Card(
        name='LOOM',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=5,
        rewards=[Resource(produce=[ResourceType.TEXTILE])],
    ),
    Card(
        name='GLASSWORKS',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=3,
        rewards=[Resource(produce=[ResourceType.GLASS])],
    ),
    Card(
        name='GLASSWORKS',
        card_type=CardType.RAW,
        epoch=2,
        players_limit=5,
        rewards=[Resource(produce=[ResourceType.GLASS])],
    ),
    ## blue
    Card(
        name='AQUEDUCT',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Point(value=5)],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.STONE],
    ),
    Card(
        name='AQUEDUCT',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[Point(value=5)],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.STONE],
    ),
    Card(
        name='COURTHOUSE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Point(value=4)],
        price=[ResourceType.CLAY, ResourceType.CLAY, ResourceType.TEXTILE],
    ),
    Card(
        name='COURTHOUSE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=5,
        rewards=[Point(value=4)],
        price=[ResourceType.CLAY, ResourceType.CLAY, ResourceType.TEXTILE],
    ),
    Card(
        name='TEMPLE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Point(value=3)],
        price=[ResourceType.WOOD, ResourceType.CLAY, ResourceType.GLASS],
        chain_next=[CardLink('PANTHEON')],
    ),
    Card(
        name='TEMPLE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[Point(value=3)],
        price=[ResourceType.WOOD, ResourceType.CLAY, ResourceType.GLASS],
        chain_next=[CardLink('PANTHEON')],
    ),
    Card(
        name='STATUE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Point(value=4)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink('GARDENS')],
    ),
    Card(
        name='STATUE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[Point(value=4)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink('GARDENS')],
    ),
    ## green
    Card(
        name='SCHOOL',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[ResourceType.WOOD, ResourceType.PAPYRUS],
        chain_next=[CardLink(name='ACADEMY'), CardLink(name='STUDY')],
    ),
    Card(
        name='SCHOOL',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[ResourceType.WOOD, ResourceType.PAPYRUS],
        chain_next=[CardLink(name='ACADEMY'), CardLink(name='STUDY')],
    ),
    Card(
        name='LIBRARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.TEXTILE],
        chain_next=[CardLink(name='SENATE'), CardLink(name='UNIVERSITY')],
    ),
    Card(
        name='LIBRARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.TEXTILE],
        chain_next=[CardLink(name='SENATE'), CardLink(name='UNIVERSITY')],
    ),
    Card(
        name='DISPENSARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.GLASS],
        chain_next=[CardLink(name='LODGE'), CardLink(name='ARENA')],
    ),
    Card(
        name='DISPENSARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=4,
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.GLASS],
        chain_next=[CardLink(name='LODGE'), CardLink(name='ARENA')],
    ),
    Card(
        name='LABORATORY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[ResourceType.CLAY, ResourceType.CLAY, ResourceType.PAPYRUS],
        chain_next=[
            CardLink(name='OBSERVATORY'),
            CardLink(name='SIEGE WORKSHOP'),
        ],
    ),
    Card(
        name='LABORATORY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=2,
        players_limit=5,
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[ResourceType.CLAY, ResourceType.CLAY, ResourceType.PAPYRUS],
        chain_next=[
            CardLink(name='OBSERVATORY'),
            CardLink(name='SIEGE WORKSHOP'),
        ],
    ),
    ## red
    Card(
        name='ARCHERY RANGE',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[War(value=2)],
        price=[ResourceType.WOOD, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='ARCHERY RANGE',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[War(value=2)],
        price=[ResourceType.WOOD, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='STABLES',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[War(value=2)],
        price=[ResourceType.CLAY, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='STABLES',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=5,
        rewards=[War(value=2)],
        price=[ResourceType.CLAY, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='WALLS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[War(value=2)],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.STONE],
        chain_next=[CardLink(name='FORTIFICATIONS')],
    ),
    Card(
        name='WALLS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[War(value=2)],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.STONE],
        chain_next=[CardLink(name='FORTIFICATIONS')],
    ),
    Card(
        name='TRAINING GROUND',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=4,
        rewards=[War(value=2)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink(name='CIRCUS')],
    ),
    Card(
        name='TRAINING GROUND',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[War(value=2)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink(name='CIRCUS')],
    ),
    Card(
        name='TRAINING GROUND',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[War(value=2)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink(name='CIRCUS')],
    ),
    ## yellow
    Card(
        name='BAZAR',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=4,
        rewards=[
            CardMatch(
                rewards=[Coin(value=2)],
                card_type=CardType.GOODS,  # grey
                left=True,
                bottom=True,
                right=True,
            )
        ]
    ),
    Card(
        name='BAZAR',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[
            CardMatch(
                rewards=[Coin(value=2)],
                card_type=CardType.GOODS,  # grey
                left=True,
                bottom=True,
                right=True,
            )
        ]
    ),
    Card(
        name='VINEYARD',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[
            CardMatch(
                rewards=[Coin(value=1)],
                card_type=CardType.RAW,  # brown
                left=True,
                bottom=True,
                right=True,
            )
        ]
    ),
    Card(
        name='VINEYARD',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[
            CardMatch(
                rewards=[Coin(value=1)],
                card_type=CardType.RAW,  # brown
                left=True,
                bottom=True,
                right=True,
            )
        ]
    ),
    Card(
        name='CARAVANSERY',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[
            Resource(
                produce=[  # todo (misha): one of
                    ResourceType.WOOD,
                    ResourceType.STONE,
                    ResourceType.ORE,
                    ResourceType.CLAY,
                ]
            )
        ],
        price=[ResourceType.WOOD, ResourceType.WOOD],
        chain_next=[CardLink('LIGHTHOUSE')],
    ),
    Card(
        name='CARAVANSERY',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=5,
        rewards=[
            Resource(
                produce=[  # todo (misha): one of
                    ResourceType.WOOD,
                    ResourceType.STONE,
                    ResourceType.ORE,
                    ResourceType.CLAY,
                ]
            )
        ],
        price=[ResourceType.WOOD, ResourceType.WOOD],
        chain_next=[CardLink('LIGHTHOUSE')],
    ),
    Card(
        name='CARAVANSERY',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[
            Resource(
                produce=[  # todo (misha): one of
                    ResourceType.WOOD,
                    ResourceType.STONE,
                    ResourceType.ORE,
                    ResourceType.CLAY,
                ]
            )
        ],
        price=[ResourceType.WOOD, ResourceType.WOOD],
        chain_next=[CardLink('LIGHTHOUSE')],
    ),
    Card(
        name='FORUM',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[
            Resource(
                produce=[  # todo (misha): one of
                    ResourceType.GLASS,
                    ResourceType.TEXTILE,
                    ResourceType.PAPYRUS,
                ]
            )
        ],
        price=[ResourceType.CLAY, ResourceType.CLAY],
        chain_next=[CardLink('HAVEN')],
    ),
    Card(
        name='FORUM',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[
            Resource(
                produce=[  # todo (misha): one of
                    ResourceType.GLASS,
                    ResourceType.TEXTILE,
                    ResourceType.PAPYRUS,
                ]
            )
        ],
        price=[ResourceType.CLAY, ResourceType.CLAY],
        chain_next=[CardLink('HAVEN')],
    ),
    Card(
        name='FORUM',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[
            Resource(
                produce=[  # todo (misha): one of
                    ResourceType.GLASS,
                    ResourceType.TEXTILE,
                    ResourceType.PAPYRUS,
                ]
            )
        ],
        price=[ResourceType.CLAY, ResourceType.CLAY],
        chain_next=[CardLink('HAVEN')],
    ),
    # epoch III
    ## blue
    Card(
        name='PANTHEON',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Point(value=7)],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.ORE,
            ResourceType.GLASS,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='PANTHEON',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=6,
        rewards=[Point(value=7)],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.ORE,
            ResourceType.GLASS,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='GARDENS',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Point(value=5)],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.WOOD,
        ],
    ),
    Card(
        name='GARDENS',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=4,
        rewards=[Point(value=5)],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.WOOD,
        ],
    ),
    Card(
        name='SENATE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Point(value=6)],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.STONE,
            ResourceType.ORE,
        ],
    ),
    Card(
        name='SENATE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=5,
        rewards=[Point(value=6)],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.STONE,
            ResourceType.ORE,
        ],
    ),
    Card(
        name='PALACE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Point(value=8)],
        price=[
            ResourceType.STONE,
            ResourceType.ORE,
            ResourceType.WOOD,
            ResourceType.CLAY,
            ResourceType.GLASS,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='PALACE',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=7,
        rewards=[Point(value=8)],
        price=[
            ResourceType.STONE,
            ResourceType.ORE,
            ResourceType.WOOD,
            ResourceType.CLAY,
            ResourceType.GLASS,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='TOWN HALL',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Point(value=6)],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.ORE,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='TOWN HALL',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=5,
        rewards=[Point(value=6)],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.ORE,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='TOWN HALL',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=3,
        players_limit=6,
        rewards=[Point(value=6)],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.ORE,
            ResourceType.GLASS,
        ],
    ),
    ## green
    Card(
        name='ACADEMY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='ACADEMY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=7,
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='LODGE',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='LODGE',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=6,
        rewards=[Invention(inventions=[InventionType.METER])],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='UNIVERSITY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.PAPYRUS,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='UNIVERSITY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=4,
        rewards=[Invention(inventions=[InventionType.RUNES])],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.PAPYRUS,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='STUDY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[
            ResourceType.WOOD,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='STUDY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=5,
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[
            ResourceType.WOOD,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='OBSERVATORY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.GLASS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='OBSERVATORY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=3,
        players_limit=7,
        rewards=[Invention(inventions=[InventionType.GEAR])],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.GLASS,
            ResourceType.TEXTILE,
        ],
    ),
    ## red
    Card(
        name='SIEGE WORKSHOP',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[War(value=3)],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.WOOD,
        ],
    ),
    Card(
        name='SIEGE WORKSHOP',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=5,
        rewards=[War(value=3)],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.WOOD,
        ],
    ),
    Card(
        name='FORTIFICATIONS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[War(value=3)],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.STONE,
        ],
    ),
    Card(
        name='FORTIFICATIONS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=7,
        rewards=[War(value=3)],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.STONE,
        ],
    ),
    Card(
        name='CIRCUS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=4,
        rewards=[War(value=3)],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.ORE,
        ],
    ),
    Card(
        name='CIRCUS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=5,
        rewards=[War(value=3)],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.ORE,
        ],
    ),
    Card(
        name='CIRCUS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=6,
        rewards=[War(value=3)],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.ORE,
        ],
    ),
    Card(
        name='ARSENAL',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[War(value=3)],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.ORE,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='ARSENAL',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=4,
        rewards=[War(value=3)],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.ORE,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='ARSENAL',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=3,
        players_limit=7,
        rewards=[War(value=3)],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.ORE,
            ResourceType.TEXTILE,
        ],
    ),
    ## yellow
    Card(
        name='ARENA',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[StageBonus(rewards=[Coin(value=3), Point(value=1)])],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.ORE],
    ),
    Card(
        name='ARENA',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=5,
        rewards=[StageBonus(rewards=[Coin(value=3), Point(value=1)])],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.ORE],
    ),
    Card(
        name='ARENA',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=7,
        rewards=[StageBonus(rewards=[Coin(value=3), Point(value=1)])],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.ORE],
    ),
    Card(
        name='LIGHTHOUSE',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[
            CardMatch(
                card_type=CardType.TRADING_BUILDINGS,  # yellow
                rewards=[Coin(value=1), Point(value=1)],
                bottom=True,
            )
        ],
        price=[ResourceType.STONE, ResourceType.GLASS],
    ),
    Card(
        name='LIGHTHOUSE',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=6,
        rewards=[
            CardMatch(
                card_type=CardType.TRADING_BUILDINGS,  # yellow
                rewards=[Coin(value=1), Point(value=1)],
                bottom=True,
            )
        ],
        price=[ResourceType.STONE, ResourceType.GLASS],
    ),
    Card(
        name='CHAMBER OF COMMERCE',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=4,
        rewards=[
            CardMatch(
                card_type=CardType.GOODS,  # grey
                rewards=[Coin(value=2), Point(value=2)],
                bottom=True,
            )
        ],
        price=[ResourceType.CLAY, ResourceType.CLAY, ResourceType.PAPYRUS],
    ),
    Card(
        name='CHAMBER OF COMMERCE',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=6,
        rewards=[
            CardMatch(
                card_type=CardType.GOODS,  # grey
                rewards=[Coin(value=2), Point(value=2)],
                bottom=True,
            )
        ],
        price=[ResourceType.CLAY, ResourceType.CLAY, ResourceType.PAPYRUS],
    ),
    Card(
        name='HAVEN',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=3,
        rewards=[
            CardMatch(
                card_type=CardType.RAW,  # brown
                rewards=[Coin(value=1), Point(value=1)],
                bottom=True,
            )
        ],
        price=[ResourceType.WOOD, ResourceType.ORE, ResourceType.TEXTILE],
    ),
    Card(
        name='HAVEN',
        card_type=CardType.TRADING_BUILDINGS,
        epoch=3,
        players_limit=4,
        rewards=[
            CardMatch(
                card_type=CardType.RAW,  # brown
                rewards=[Coin(value=1), Point(value=1)],
                bottom=True,
            )
        ],
        price=[ResourceType.WOOD, ResourceType.ORE, ResourceType.TEXTILE],
    ),
    ## violet
    Card(
        name='TRADERS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.TRADING_BUILDINGS,  # yellow
                rewards=[Point(value=1)],
                left=True,
                right=True,
            )
        ],
        price=[ResourceType.GLASS, ResourceType.TEXTILE, ResourceType.PAPYRUS],
    ),
    Card(
        name='SPIES GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.MILITARY_BUILDINGS,  # red
                rewards=[Point(value=1)],
                left=True,
                right=True,
            )
        ],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='PHILOSOPHERS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.SCIENTIFIC_BUILDINGS,  # green
                rewards=[Point(value=1)],
                left=True,
                right=True,
            )
        ],
        price=[
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.PAPYRUS,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='MAGISTRATES GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.PUBLIC_BUILDINGS,  # blue
                rewards=[Point(value=1)],
                left=True,
                right=True,
            )
        ],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.STONE,
            ResourceType.TEXTILE,
        ],
    ),
    Card(
        name='CRAFTSMENS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.GOODS,  # grey
                rewards=[Point(value=2)],
                left=True,
                right=True,
            )
        ],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.STONE,
            ResourceType.STONE,
        ],
    ),
    Card(
        name='WORKERS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.RAW,  # brown
                rewards=[Point(value=1)],
                left=True,
                right=True,
            )
        ],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.CLAY,
            ResourceType.STONE,
            ResourceType.WOOD,
        ],
    ),
    Card(
        name='SHIPOWNERS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=CardType.RAW,  # brown
                rewards=[Point(value=1)],
                bottom=True,
            ),
            CardMatch(
                card_type=CardType.GOODS,  # grey
                rewards=[Point(value=1)],
                bottom=True,
            ),
            CardMatch(
                card_type=CardType.GUILD,  # violet
                rewards=[Point(value=1)],
                bottom=True,
            ),
        ],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.GLASS,
            ResourceType.PAPYRUS,
        ],
    ),
    Card(
        name='BUILDERS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            StageBonus(
                rewards=[Point(value=1)],
                left=True,
                bottom=True,
                right=True,
            )
        ],
        price=[
            ResourceType.STONE,
            ResourceType.STONE,
            ResourceType.CLAY,
            ResourceType.CLAY,
            ResourceType.GLASS,
        ],
    ),
    Card(
        name='SCIENTISTS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            Invention(  # todo (misha): one of
                inventions=[
                    InventionType.METER,
                    InventionType.RUNES,
                    InventionType.GEAR,
                ]
            )
        ],
        price=[
            ResourceType.WOOD,
            ResourceType.WOOD,
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.PAPYRUS,
        ],
    ),
    Card(
        name='STRATEGISTS GUILD',
        card_type=CardType.GUILD,
        epoch=3,
        players_limit=0,
        rewards=[
            CardMatch(
                card_type=WarPoint(value=-1),
                rewards=[Point(value=1)],
                left=True,
                right=True,
            )
        ],
        price=[
            ResourceType.ORE,
            ResourceType.ORE,
            ResourceType.STONE,
            ResourceType.TEXTILE,
        ],
    ),
]
