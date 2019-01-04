from game.game import Game
from game.agent import RandomActionAgentV0


def run():
    players = [
        RandomActionAgentV0(name='Masha', color='green'),
        RandomActionAgentV0(name='Misha', color='red'),
        RandomActionAgentV0(name='Oksana', color='yellow'),
        RandomActionAgentV0(name='Vova', color='blue'),
    ]
    from game import Resource, ResourceType
    players[0]._resources = [Resource(produce=[ResourceType.CLAY, ResourceType.ORE])]
    players[1]._resources = [Resource(produce=[ResourceType.CLAY, ResourceType.ORE])]
    players[2]._resources = [Resource(produce=[ResourceType.CLAY, ResourceType.ORE])]
    players[3]._resources = [Resource(produce=[ResourceType.CLAY, ResourceType.ORE])]
    game = Game(players=players, verbose=False)
    game.init_players()
    for epoch in range(1, 4):
        game.init_epoch(epoch)
        while not game.finished:
            game.step()
        game.resolve_war(epoch=epoch)
    game.finish()
