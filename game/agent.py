from abc import ABC, abstractmethod
from enum import Enum

import click

from game import Coin, War, Point, WarPoint, CardType, ResourceType


class Agent(ABC):
    @abstractmethod
    def take(self, *args, **kwargs):
        pass

    @abstractmethod
    def act(self):
        pass


class RandomActionAgentV0(Agent):
    def __init__(self, name, color='white', verbose=False):
        self.name = name
        self.location = None
        self.coins = Coin(value=0)
        self._cards = []
        self._played_cards = []
        self._resources = []
        self._war_points = []
        self._color = color
        self._verbose = verbose

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
    def resources(self):
        resources = []
        # todo (misha): implement one of
        for r in self._resources:
            resources.extend(r.produce)
        return resources

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

    @property
    def war_points(self):
        value = WarPoint(value=0)
        for p in self._war_points:
            value += p
        return value

    @property
    def public_points(self):
        points = Point(value=0)
        # todo (misha): extract reward helper?
        for card in self._played_cards:
            if card.card_type == CardType.PUBLIC_BUILDINGS:
                for reward in card.rewards:
                    if isinstance(reward, Point):
                        points += reward
        return points

    def can_play(self, card):
        price = card.price
        for item in price:
            # todo (misha): check chain next first
            if isinstance(item, Coin) and self.coins < item:
                return False
            elif isinstance(item, ResourceType) and item not in self.resources:
                # todo (misha): tbd
                return False

        return True

    def print(self, message):
        if self._verbose:
            click.secho(message, fg=self._color)

    def play_card(self, card):
        self.print(f'{self.name} is playing {card}')
        self._played_cards.append(card)

    def dispose_card(self):
        self.coins += Coin(value=3)
        self._cards.pop()
        self.print(f'{self.name} disposing card for 3 coins')
