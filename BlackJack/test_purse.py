import unittest
from Purse import *


class TestPurse(unittest.TestCase):
    def test_rate_win(self):
        purse = Purse()
        purse.make_a_bet(900)
        purse.rate_win()
        money = purse.get_money()
        self.assertEqual(money, 1100, "Should be 1100")

    def test_rate_defeat(self):
        purse = Purse()
        purse.make_a_bet(800)
        purse.rate_defeat()
        money = purse.get_money()
        self.assertEqual(money, 200, "Should be 200")

    def test_fill_up(self):
        purse = Purse()
        purse.fill_up_a_purse(7000)
        money = purse.get_money()
        self.assertEqual(money, 8000, "Should be 8000")


if __name__ == '__main__':
    unittest.main()
