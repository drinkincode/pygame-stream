import pytest
from actors.actor import Actor


# Test data for Actor class
stats_list_data = [("health", 10)]
attack_list_data = [{"atkName": "kick", "atkDamage": 10, "atkLevel": 1, "atkCost": 0}]
x = 0
y = 0


@pytest.fixture
def actor():
    name = "Test Actor"
    return Actor(name, stats_list_data, attack_list_data, x, y)


def test_actor_initialization(actor):
    assert actor.name == "Test Actor"

    # Tests stats list
    assert [(stat.name, stat.statPoints) for stat in actor.statManager.stats] == stats_list_data

    # Tests attack list
    for i in range(len(attack_list_data)):
        assert actor.attackManager.attackList[i].name == attack_list_data[0]['atkName']
        assert actor.attackManager.attackList[i].damage == attack_list_data[0]['atkDamage']
        assert actor.attackManager.attackList[i].attackLevel == attack_list_data[0]['atkLevel']
        assert actor.attackManager.attackList[i].attackCost == attack_list_data[0]['atkCost']

    # Tests x and y coordinates
    assert actor.x == 0
    assert actor.y == 0


def test_print_greeting(actor, capsys):
    actor.print_greeting()
    captured = capsys.readouterr()
    assert captured.out == "Hi! I'm Test Actor\n"