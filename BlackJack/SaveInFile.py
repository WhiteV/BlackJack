import json
import pickle


class SaveFile(object):
    def __init__(self):
        self.file_for_statistic = "statistic.json"
        self.file_for_purse = "purse.json"

    def save_statistic(self, statistic):
        file = open(self.file_for_statistic, 'w')
        json.dump(statistic, file)
        file.close()

    @staticmethod
    def save_hand(hand, file_name):
        file = open(file_name, 'wb')
        pickle.dump(hand, file, 2)
        file.close()

    def save_purse(self, purse):
        file = open(self.file_for_purse, 'w')
        json.dump(purse, file)
        file.close()


