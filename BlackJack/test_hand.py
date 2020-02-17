import unittest
from Hand import *
from Card import *


class TestHand(unittest.TestCase):
    def test_score_21(self):
        hand = Hand()
        card_1 = Card('K', '♦')
        card_2 = Card('A', '♦')
        cards = [card_1, card_2]
        for card in cards:
            card.calculation_of_power()
            hand.take_a_card(card)
            hand.scoring()
        point = hand.get_point()
        self.assertEqual(point, 21, "Should be 21")

    def test_score(self):
        hand = Hand()
        card_1 = Card('J', '♦')
        card_2 = Card('8', '♦')
        cards = [card_1, card_2]
        for card in cards:
            card.calculation_of_power()
            hand.take_a_card(card)
            hand.scoring()
        point = hand.get_point()
        self.assertEqual(point, 18, "Should be 18")


if __name__ == '__main__':
    unittest.main()