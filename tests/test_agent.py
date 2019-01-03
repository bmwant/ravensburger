from game.agent import RandomActionAgentV0
from game.card import Card, CardType
from game import ResourceType


def test_can_take_card_with_resources():
    card = Card(
        name='test card',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=0,
        price=[ResourceType.CLAY]
    )

    agent = RandomActionAgentV0(name='Smith')
    agent._resources = [ResourceType.CLAY]

    assert agent.can_play(card)


def test_cannot_take_card_with_resources():
    card = Card(
        name='test card',
        card_type=CardType.RAW,
        epoch=1,
        players_limit=0,
        price=[ResourceType.CLAY]
    )

    agent = RandomActionAgentV0(name='Smith')
    agent._resources = [ResourceType.ORE]

    assert not agent.can_play(card)
