import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
deck_1 = []
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    deck_1.append(cardp_1)
deck_2 = []
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    deck_2.append(cardp_2)


def fight(c1, c2):
    cards = [str(n) for n in range(2, 11)] + list('JQKA')
    return cards.index(c1[:-1]) - cards.index(c2[:-1])

def battle(deck_1, deck_2, war_1, war_2):
    if not deck_1 or not deck_2:
        return
    c1 = deck_1.pop(0)
    c2 = deck_2.pop(0)
    war_1.append(c1)
    war_2.append(c2)
    r = fight(c1, c2)
    if r > 0:
        deck_1.extend(war_1 + war_2)
        war_1[:] = []
        war_2[:] = []
    elif r < 0:
        deck_2.extend(war_1 + war_2)
        war_1[:] = []
        war_2[:] = []
    else:
        for i in range(3):
            if not deck_1 or not deck_2:
                return
            war_1.append(deck_1.pop(0))
            war_2.append(deck_2.pop(0))
        battle(deck_1, deck_2, war_1, war_2)

war_1, war_2 = [], []
round = 0

while deck_1 and deck_2:
    battle(deck_1, deck_2, war_1, war_2)
    round += 1

if war_1 or war_2:
    print('PAT')
elif deck_1:
    print(1, round)
else:
    print(2, round)
