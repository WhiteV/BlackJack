from random import choice
from Card import *


class Deck(object):
    def __init__(self):
        self.deck = []

    def creation_of_deck(self):
        value_list = [2, 3, 4, 5, 6, 7, 8, 9,
                      10, 'J', 'Q', 'K', 'A']
        suit_list = ['♦', '♥', '+', '♠']

        for value in value_list:
            for suit in suit_list:
                card = Card(value, suit)
                card.calculation_of_power()
                self.deck.append(card)

    def give_a_card(self):
        random_card = choice(self.deck)
        return random_card
