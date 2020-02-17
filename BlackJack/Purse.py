import json


class Purse(object):
    def __init__(self):
        self.money = 1000
        self.bet = 100

    def upload_purse(self, file_name):
        try:
            file = open(file_name, 'r')
            json_data = json.load(file)
            file.close()
            self.money = int(json_data['player_money'])
            self.bet = int(json_data['bet'])

        except FileNotFoundError:
            self.money = 1000
            self.bet = 10

    def get_purse_dict(self):
        purse_dict = {'player_money': self.money,
                      'bet': self.bet}
        return purse_dict

    def make_a_bet(self, player_bet):
        if player_bet >= self.money:
            self.bet = self.money
        elif player_bet > 800 or player_bet < 100:
            self.bet = 100
        else:
            self.bet = player_bet

    def fill_up_a_purse(self, player_money):
        if player_money > 10000 or player_money < 1000:
            self.money += 1000
        else:
            self.money += player_money

    def rate_win(self):
        self.money += self.bet

    def rate_defeat(self):
        self.money -= self.bet

    def get_money(self):
        return self.money


