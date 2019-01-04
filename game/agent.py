from abc import ABC, abstractmethod
from enum import Enum

import click

from game import Coin, War, CardType, ResourceType


class Agent(ABC):
    @abstractmethod
    def take(self, *args, **kwargs):
        pass

    @abstractmethod
    def act(self):
        pass


class RandomActionAgentV0(Agent):
    def __init__(self, name, color='white'):
        self.name = name
        self.location = None
        self.coins = Coin(value=0)
        self._cards = []
        self._played_cards = []
        self._resources = []
        self._war_points = []
        self._color = color

    def take(self, cards):
        self._cards = cards

    def act(self):
        index = None
        for i, card in enumerate(self._cards):
            if self.can_play(card):
                index = i
                break
        if index is not None:
            card = self._cards.pop(index)
            self.play_card(card)
        else:
            self.dispose_card()

    def __str__(self):
        return f'Player {self.name} at {self.location}'

    @property
    def cards(self):
        return self._cards

    @property
    def war(self):
        value = War(value=0)
        for card in self._played_cards:
            if card.card_type == CardType.MILITARY_BUILDINGS:
                for reward in card.rewards:
                    if isinstance(reward, War):
                        value += reward
        # todo (misha): add war from stages
        return value

    def can_play(self, card):
        price = card.price
        for item in price:
            # todo (misha): check chain next first
            if isinstance(item, Coin) and self.coins < item:
                return False
            elif isinstance(item, ResourceType) and item not in self._resources:
                # todo (misha): tbd
                return False

        return True

    def play_card(self, card):
        click.secho(f'{self.name} is playing {card}', fg=self._color)
        self._played_cards.append(card)

    def dispose_card(self):
        self.coins += Coin(value=3)
        self._cards.pop()
        click.secho(f'{self.name} disposing card for 3 coins', fg=self._color)
