from enum import Enum


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
        self.players_limit = players_limit  # lower limit for players number
        self.rewards = rewards or []
        self.price = price or []
        self.chain_next = chain_next or []

    def __str__(self):
        return f'{self.name} {self.players_limit}+'



