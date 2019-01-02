from functools import partial
from collections import deque
from random import sample

from click import secho

from game import Coin
from game.card import cards_registry
from game.location import locations_a


def is_legit(card, epoch: int, players_count: int) -> bool:
    return card.epoch == epoch and card.players_limit <= players_count


class Game(object):
    def __init__(self, players: list, verbose=True):
        self.players = players
        self._cards = []
        self.verbose = verbose
        self._epoch_finished = False

    def init_players(self):
        """
        Randomly assign a location for each player and give initial coins.
        """
        locations = sample(locations_a, self.players_count)
        for index, player in enumerate(self.players):
            player.location = locations[index]
            player.coins = Coin(value=3)
            self.print(player)

    def init_epoch(self, epoch: int):
        self.print(f'Drawing cards for epoch #{epoch}')
        cards_selector = partial(
            is_legit,
            epoch=epoch,
            players_count=self.players_count,
        )
        self._cards = list(filter(cards_selector, cards_registry))
        partition = len(self._cards) // self.players_count
        assert partition == 7
        for i in range(self.players_count):
            self.players[i].take(self._cards[i*partition:(i+1)*partition])
        self._epoch_finished = False

    # it's a lap, maybe divide into actual steps?
    def step(self):
        for player in self.players:
            player.act()
        if len(self.players[0].cards) == 1:
            self._epoch_finished = True
            return
        self.shift_cards()

    def shift_cards(self):
        self.print('Passing cards to next player clockwise')
        cards = deque([player.cards for player in self.players])
        cards.rotate(1)
        for player in self.players:
            player.take(cards.popleft())

    def resolve_war(self):
        pass

    def finish(self):
        pass

    @property
    def finished(self) -> bool:
        return self._epoch_finished

    @property
    def players_count(self) -> int:
        return len(self.players)

    def print(self, message):
        if self.verbose:
            secho(str(message), bold=True)
