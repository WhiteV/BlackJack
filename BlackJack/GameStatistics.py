import json


class GameStatistics(object):
    def __init__(self):
        self.win_counter = 0
        self.lesion_counter = 0
        self.draw_counter = 0
        self.all_games = 0

    def upload_statistic(self, file_name):
        try:
            file = open(file_name, 'r')
            json_data = json.load(file)
            file.close()
            self.all_games = int(json_data['all_games'])
            self.win_counter = int(json_data['win_counter'])
            self.draw_counter = int(json_data['draw_counter'])
            self.lesion_counter = int(json_data['lesion_counter'])

        except FileNotFoundError:
            self.win_counter = 0
            self.lesion_counter = 0
            self.draw_counter = 0
            self.all_games = 0

    def get_game_statistics(self):
        statistics = {"win_counter": self.win_counter,
                      "lesion_counter": self.lesion_counter,
                      "draw_counter": self.draw_counter,
                      "all_games": self.all_games
                      }
        return statistics

    def count_all_games(self):
        self.all_games = self.win_counter + self.draw_counter + self.lesion_counter

    def count_victories(self):
        self.win_counter += 1

    def count_lesions(self):
        self.lesion_counter += 1

    def count_draw(self):
        self.draw_counter += 1
