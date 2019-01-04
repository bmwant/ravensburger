from game.game import Game
from game.agent import RandomActionAgentV0


def run():
    players = [
        RandomActionAgentV0(name='Masha', color='green'),
        RandomActionAgentV0(name='Misha', color='red'),
        RandomActionAgentV0(name='Oksana', color='yellow'),
        RandomActionAgentV0(name='Vova', color='blue'),
    ]
    game = Game(players=players)
    game.init_players()
    for epoch in range(1, 4):
        game.init_epoch(epoch)
        while not game.finished:
            game.step()
        game.resolve_war(epoch=epoch)
    game.finish()
