from enum import Enum

from game import Resource, ResourceType


class CardType(Enum):
    RAW = 'raw'  # brown
    GOODS = 'goods'  # grey
    PUBLIC_BUILDINGS = 'public_buildings'  # blue
    SCIENTIFIC_BUILDINGS = 'scientific_buildings'  # green
    TRADING_BUILDINGS = 'trading_buildings'  # yellow
    MILITARY_BUILDINGS = 'military_buildings'  # red
    GUILD = 'guild'  # violet


class Card(object):
    def __init__(
            self, *,
            name, card_type, epoch, players_limit,
            rewards=None, price_coins=0, price_resources=None,
    ):
        self.name = name
        self.card_type = card_type
        self.epoch = epoch
        self.players_limit = players_limit
        self.rewards = rewards or []
        self.price_coins = price_coins
        self.price_resources = price_resources or []



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
        price_coins=1,
        rewards=[Resource(produce=[ResourceType.CLAY, ResourceType.ORE])],
    ),
    Card(
        name='TREE FARM',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        price_coins=1,
        rewards=[Resource(produce=[ResourceType.WOOD, ResourceType.CLAY])],
    ),
    Card(
        name='EXCAVATION',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=4,
        price_coins=1,
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.CLAY])],
    ),
    Card(
        name='MINE',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=6,
        price_coins=1,
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.ORE])],
    ),
    Card(
        name='FOREST CAVE',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=5,
        price_coins=1,
        rewards=[Resource(produce=[ResourceType.WOOD, ResourceType.ORE])],
    ),
    Card(
        name='TIMBER YARD',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=3,
        price_coins=1,
        rewards=[Resource(produce=[ResourceType.STONE, ResourceType.WOOD])],
    ),
]



