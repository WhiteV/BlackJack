import unittest
from Card import *


class TestCard(unittest.TestCase):
    def test_power_number(self):
        card = Card(5, '♦')
        card.calculation_of_power()
        power = card.get_power()
        self.assertEqual(power, 5, "Should be 5")

    def test_power_king(self):
        card = Card('K', '♦')
        card.calculation_of_power()
        power = card.get_power()
        self.assertEqual(power, 10, "Should be 10")

    def test_power_ace(self):
        card = Card('A', '♦')
        card.calculation_of_power()
        power = card.get_power()
        self.assertEqual(power, 1, "Should be 1")


if __name__ == '__main__':
    unittest.main()




