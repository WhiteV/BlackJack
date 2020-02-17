class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.power = 0
        self.face = str(self.value) + str(self.suit)
        self.shirt = '???'

    def calculation_of_power(self):
        try:
            self.power = int(self.value)
        except ValueError:
            if self.value == 'A':
                self.power = 1
            else:
                self.power = 10

    def get_power(self):
        return self.power

    def get_face(self):
        return self.face

    def get_shirt(self):
        return self.shirt
