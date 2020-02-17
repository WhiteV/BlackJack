import pickle


class Hand(object):
    def __init__(self):
        self.hand = []
        self.point = 0

    def hand_restart(self):
        self.hand = []
        self.point = 0

    def get_point(self):
        return self.point

    def upload_hand(self, file_name):
        try:
            file = open(file_name, 'rb')
            hand = pickle.load(file)
            file.close()
            return hand

        except FileNotFoundError:
            self.hand = []
            self.point = 0

    def get_info(self):
        player_cards = []
        for card in self.hand:
            card_face = card.get_face()
            player_cards.append(card_face)
        player_dict = {'player_cards': player_cards,
                       'player_score': self.point}
        return player_dict

    def take_a_card(self, card):
        self.hand.append(card)

    def scoring(self):
        self.point = 0
        for card in self.hand:
            check_face = card.get_face()
            if check_face[0] == 'A':
                if self.point + 11 > 21:
                    self.point += 1
                else:
                    self.point += 11
            else:
                card_power = card.get_power()
                self.point += card_power
