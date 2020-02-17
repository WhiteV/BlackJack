import unittest
from GameStatistics import *


class TestStatistics(unittest.TestCase):
    def test_win_counter(self):
        statistic = GameStatistics()
        for i in range(4):
            statistic.count_victories()
        win_counter = statistic.get_game_statistics()
        self.assertEqual(win_counter["win_counter"], 4, "Should be 4")

    def test_lesions_counter(self):
        statistic = GameStatistics()
        for i in range(4):
            statistic.count_lesions()
        lesion_counter = statistic.get_game_statistics()
        self.assertEqual(lesion_counter["lesion_counter"], 4, "Should be 4")

    def test_draw_counter(self):
        statistic = GameStatistics()
        for i in range(4):
            statistic.count_draw()
        draw_counter = statistic.get_game_statistics()
        self.assertEqual(draw_counter["draw_counter"], 4, "Should be 4")

    def test_all_games_counter(self):
        statistic = GameStatistics()
        for i in range(4):
            statistic.count_victories()
            statistic.count_draw()
            statistic.count_lesions()

        statistic.count_all_games()
        all_games = statistic.get_game_statistics()
        self.assertEqual(all_games["all_games"], 12, "Should be 12")


if __name__ == '__main__':
    unittest.main()