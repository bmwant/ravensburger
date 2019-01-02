from enum import Enum

from game import Resource, ResourceType, Invention, InventionType
from game import Point, Coin, War


class CardType(Enum):
    RAW = 'raw'  # brown
    GOODS = 'goods'  # grey
    PUBLIC_BUILDINGS = 'public_buildings'  # blue
    SCIENTIFIC_BUILDINGS = 'scientific_buildings'  # green
    TRADING_BUILDINGS = 'trading_buildings'  # yellow
    MILITARY_BUILDINGS = 'military_buildings'  # red
    GUILD = 'guild'  # violet


class CardLink(object):
    def __init__(self, name):
        self.name = name


class Card(object):
    def __init__(
            self, *,
            name, card_type, epoch, players_limit,
            rewards=None, price=None, chain_next=None,
    ):
        self.name = name
        self.card_type = card_type
        self.epoch = epoch
        self.players_limit = players_limit
        self.rewards = rewards or []
        self.price = price or []
        self.chain_next = chain_next or []



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
        # chain_next=None, Statue
        rewards=[Point(value=2)],
    ),
    Card(
        name='THEATER',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=6,
        # chain_next=None, Statue
        rewards=[Point(value=2)],
    ),
    Card(
        name='ALTAR',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=5,
        # chain_next=None, temple
        rewards=[Point(value=2)],
    ),
    Card(
        name='ALTAR',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        # chain_next=None, temple
        rewards=[Point(value=2)],
    ),
    Card(
        name='PAWNSHOP',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=4,
        # chain_next=None
        rewards=[Point(value=3)],
    ),
    Card(
        name='PAWNSHOP',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=7,
        # chain_next=None
        rewards=[Point(value=3)],
    ),
    Card(
        name='BATHS',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        # chain_next=None, aqueduct
        rewards=[Point(value=3)],
        price=[ResourceType.STONE],
    ),
    Card(
        name='BATHS',
        card_type=CardType.PUBLIC_BUILDINGS,
        epoch=1,
        players_limit=7,
        # chain_next=None, aqueduct
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
        rewards=[Invention(invention_type=InventionType.METER)],
        price=[ResourceType.TEXTILE],
    ),
    Card(
        name='APOTHECARY',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=5,
        chain_next=[CardLink(name='STABLES'), CardLink(name='DISPENSARY')],
        rewards=[Invention(invention_type=InventionType.METER)],
        price=[ResourceType.TEXTILE],
    ),
    Card(
        name='WORKSHOP',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink(name='LABORATORY'), CardLink(name='ARCHERY RANGE')],
        rewards=[Invention(invention_type=InventionType.GEAR)],
        price=[ResourceType.GLASS],
    ),
    Card(
        name='WORKSHOP',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=7,
        chain_next=[CardLink(name='LABORATORY'), CardLink(name='ARCHERY RANGE')],
        rewards=[Invention(invention_type=InventionType.GEAR)],
        price=[ResourceType.GLASS],
    ),
    Card(
        name='SCRIPTORIUM',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=3,
        chain_next=[CardLink(name='COURTHOUSE'), CardLink(name='LIBRARY')],
        rewards=[Invention(invention_type=InventionType.RUNES)],
        price=[ResourceType.PAPYRUS],
    ),
    Card(
        name='SCRIPTORIUM',
        card_type=CardType.SCIENTIFIC_BUILDINGS,
        epoch=1,
        players_limit=4,
        chain_next=[CardLink(name='COURTHOUSE'), CardLink(name='LIBRARY')],
        rewards=[Invention(invention_type=InventionType.RUNES)],
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
]
