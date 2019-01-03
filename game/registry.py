from game import Card, CardType, CardLink
from game import Resource, ResourceType, Invention, InventionType
from game import Point, Coin, Discount, War, ColorMatch


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
        rewards=[War(amount=1)],
        price=[ResourceType.WOOD],
    ),
    Card(
        name='STOCKADE',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=7,
        rewards=[War(amount=1)],
        price=[ResourceType.WOOD],
    ),
    Card(
        name='GUARD TOWER',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[War(amount=1)],
        price=[ResourceType.CLAY],
    ),
    Card(
        name='GUARD TOWER',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=4,
        rewards=[War(amount=1)],
        price=[ResourceType.CLAY],
    ),
    Card(
        name='BARRACKS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=3,
        rewards=[War(amount=1)],
        price=[ResourceType.ORE],
    ),
    Card(
        name='BARRACKS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=1,
        players_limit=5,
        rewards=[War(amount=1)],
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
        rewards=[War(amount=2)],
        price=[ResourceType.WOOD, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='ARCHERY RANGE',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[War(amount=2)],
        price=[ResourceType.WOOD, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='STABLES',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[War(amount=2)],
        price=[ResourceType.CLAY, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='STABLES',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=5,
        rewards=[War(amount=2)],
        price=[ResourceType.CLAY, ResourceType.WOOD, ResourceType.ORE],
    ),
    Card(
        name='WALLS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=3,
        rewards=[War(amount=2)],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.STONE],
        chain_next=[CardLink(name='FORTIFICATIONS')],
    ),
    Card(
        name='WALLS',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[War(amount=2)],
        price=[ResourceType.STONE, ResourceType.STONE, ResourceType.STONE],
        chain_next=[CardLink(name='FORTIFICATIONS')],
    ),
    Card(
        name='TRAINING GROUND',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=4,
        rewards=[War(amount=2)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink(name='CIRCUS')],
    ),
    Card(
        name='TRAINING GROUND',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=6,
        rewards=[War(amount=2)],
        price=[ResourceType.ORE, ResourceType.ORE, ResourceType.WOOD],
        chain_next=[CardLink(name='CIRCUS')],
    ),
    Card(
        name='TRAINING GROUND',
        card_type=CardType.MILITARY_BUILDINGS,
        epoch=2,
        players_limit=7,
        rewards=[War(amount=2)],
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
            ColorMatch(
                price=2,
                card_type=CardType.RAW,  # todo (misha): raw not raw
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
            ColorMatch(
                price=2,
                card_type=CardType.RAW,  # todo (misha): raw not raw
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
            ColorMatch(
                price=1,
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
            ColorMatch(
                price=1,
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
]
