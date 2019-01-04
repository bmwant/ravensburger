from functools import partial
from collections import deque
from random import sample

from click import secho

from game import Coin, CardType, WarPoint
from game.registry import cards_registry
from game.location import locations_a


def is_legit(card, epoch: int, players_count: int) -> bool:
    return card.epoch == epoch and \
           card.players_limit <= players_count and \
           card.card_type != CardType.GUILD


def select_guild_cards(players_count: int) -> list:
    cards = list(filter(
        lambda c: c.card_type == CardType.GUILD, cards_registry))
    return sample(cards, players_count+2)


class Game(object):
    def __init__(self, players: list, verbose=True):
        self.players = players
        self._cards = []
        self.verbose = verbose
        self._epoch_finished = False
        self._rotate = 1

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
        if epoch == 3:
            self._cards.extend(select_guild_cards(self.players_count))

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
            # Change cards passing direction
            self._rotate *= -1
            return
        self.shift_cards()

    def shift_cards(self):
        direction = 'clockwise' if self._rotate == 1 else 'counterclockwise'
        self.print(f'Passing cards to next player {direction}')
        cards = deque([player.cards for player in self.players])
        cards.rotate(self._rotate)
        for player in self.players:
            player.take(cards.popleft())

    def resolve_war(self, epoch: int):
        self.print('Resolving war')
        for index, player in enumerate(self.players):
            player_left = self.players[index-1]
            player_right = self.players[(index+1) % self.players_count]
            value_left = player_left.war
            value_right = player_right.war
            value = player.war
            win_point = WarPoint(value=1+(epoch-1)*2)
            lose_point = WarPoint(value=-1)

            if value < value_left:
                player._war_points.append(lose_point)
            elif value > value_left:
                player._war_points.append(win_point)

            if value < value_right:
                player._war_points.append(lose_point)
            elif value > value_right:
                player._war_points.append(win_point)

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
