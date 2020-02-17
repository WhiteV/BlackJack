import time
import os
from Deck import *
from Hand import *
from ConsoleDisplay import *
from GameStatistics import *
from SaveInFile import *
from Purse import *


class BlackJack(object):
    def __init__(self, display):
        self.game_status = True
        self.deck = Deck()
        self.player = Hand()
        self.purse = Purse()
        self.croupier = Hand()
        self.display = display()
        self.statistics = GameStatistics()
        self.save = SaveFile()

    # ______________________deck______________________ #

    def compilation_of_a_deck(self):
        self.deck.creation_of_deck()

    # ______________________display______________________ #

    def display_result_without_first_card(self):
        player_info = self.player.get_info()
        croupier_info = self.croupier.get_info()
        self.display.display_result_without_first_card(player_info, croupier_info)

    def display_result_with_first_card(self):
        player_info = self.player.get_info()
        croupier_info = self.croupier.get_info()
        self.display.display_result_with_first_card(player_info, croupier_info)

    def display_message_about_win(self):
        self.display.display_message_about_win()

    def display_message_about_lose(self):
        self.display.display_message_about_lose()

    def display_message_about_draw(self):
        self.display.display_message_about_draw()

    def display_message_about_croupier(self):
        self.display.display_message_about_croupier()

    def display_border(self):
        self.display.display_border()

    def display_continue_the_game(self):
        return self.display.continue_the_game()

    # ______________________hand______________________ #

    def get_random_card_for_player(self, hand):
        random_card = self.deck.give_a_card()
        hand.take_a_card(random_card)
        hand.scoring()

    def save_player_hand(self):
        self.save.save_hand(self.player, 'player_hand.txt')

    def save_croupier_hand(self):
        self.save.save_hand(self.croupier, 'croupier_hand.txt')

    def upload_player_hand(self):
        return self.player.upload_hand('player_hand.txt')

    def upload_croupier_hand(self):
        return self.player.upload_hand('croupier_hand.txt')

    # ______________________statistic______________________ #

    def count_victories(self):
        self.statistics.count_victories()
        self.statistics.count_all_games()

    def count_draw(self):
        self.statistics.count_draw()
        self.statistics.count_all_games()

    def count_lesion(self):
        self.statistics.count_lesions()
        self.statistics.count_all_games()

    def count_all_games(self):
        self.statistics.count_all_games()

    def display_statistic(self):
        statistics = self.statistics.get_game_statistics()
        self.display.display_game_statistics(statistics)

    def get_statistic(self):
        return self.statistics.get_game_statistics()

    def upload_statistic(self):
        self.statistics.upload_statistic('statistic.json')

    def save_statistic(self):
        statistic = self.statistics.get_game_statistics()
        self.save.save_statistic(statistic)

    # ______________________purse______________________ #
    def place_a_bet(self):
        bet = self.display.display_player_bet()
        self.purse.make_a_bet(bet)

    def display_player_money(self):
        money = self.purse.get_money()
        self.display.display_player_money(money)

    def fill_up_a_purse(self):
        money = self.purse.get_money()
        if money < 500:
            recharge = self.display.display_fill_up_a_purse()
            self.purse.fill_up_a_purse(recharge)

    def rate_win(self):
        self.purse.rate_win()

    def rate_defeat(self):
        self.purse.rate_defeat()

    def save_purse(self):
        purse_dict = self.purse.get_purse_dict()
        self.save.save_purse(purse_dict)

    def upload_purse(self):
        file_name = "purse.json"
        self.purse.upload_purse(file_name)

    # ______________________check and result______________________ #

    def check_21(self):
        player_point = self.player.get_point
        if player_point == 21:
            return True
        else:
            return False

    def check_overflow_hand(self):
        player_point = self.player.get_point()
        if player_point > 21:
            return True
        else:
            return False

    def count_result(self):

        player_point = self.player.get_point()
        croupier_point = self.croupier.get_point()

        if croupier_point > 21 and player_point <= 21:
            self.count_victories()
            self.display_message_about_win()
            self.rate_win()

        elif player_point > 21:
            self.count_lesion()
            self.display_message_about_lose()
            self.rate_defeat()

        elif player_point > croupier_point:
            self.count_victories()
            self.display_message_about_win()
            self.rate_win()

        elif player_point == croupier_point:
            self.count_draw()
            self.display_message_about_draw()

        else:
            self.count_lesion()
            self.display_message_about_lose()
            self.rate_defeat()

    # ______________________game______________________ #

    def start_game(self):

        self.display_border()
        self.upload_statistic()

        self.upload_purse()
        self.fill_up_a_purse()
        self.display_player_money()

        try:
            self.player = self.upload_player_hand()
            self.croupier = self.upload_croupier_hand()

        except AttributeError:
            self.place_a_bet()
            self.save_purse()
            self.player = Hand()
            self.croupier = Hand()
            hands = [self.player, self.croupier]
            for hand in hands:
                count = 0
                while count != 2:
                    self.get_random_card_for_player(hand)
                    count += 1

        self.save_player_hand()
        self.save_croupier_hand()

        self.display_result_without_first_card()

        check_21 = self.check_21()

        if check_21 == True:
            self.display_message_about_win()
            self.count_victories()

        else:
            answer = self.display_continue_the_game()

            while answer == True:
                self.get_random_card_for_player(self.player)

                self.save_player_hand()
                self.display_border()
                self.display_result_without_first_card()

                overflow_check = self.check_overflow_hand()
                if overflow_check == True:
                    break

                else:
                    answer = self.display_continue_the_game()

            self.display_border()
            self.display_message_about_croupier()
            self.display_border()
            croupier_point = self.croupier.get_point()

            while croupier_point < 17:
                self.get_random_card_for_player(self.croupier)
                croupier_point = self.croupier.get_point()

            self.display_result_with_first_card()
            self.count_result()

        self.display_border()
        self.display_player_money()
        self.save_purse()
        self.display_border()

        self.display_statistic()
        self.save_statistic()

        os.remove('player_hand.txt')
        os.remove('croupier_hand.txt')

        self.display_border()
        time.sleep(1.2)


if __name__ == '__main__':
    BJ = BlackJack(ConsoleDisplay)
    BJ.compilation_of_a_deck()
    while True:
        BJ.start_game()
        for i in range(2):
            print('\n')
