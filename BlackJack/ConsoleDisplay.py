class ConsoleDisplay(object):
    def __init__(self):
        pass

    @staticmethod
    def display_game_statistics(statistics):
        print("Статистика:",
              "\nВсего игр:", statistics['all_games'],
              "\nПобед: ", statistics['win_counter'],
              "\nНичьих:", statistics['draw_counter'],
              "\nПоражений:", statistics['lesion_counter'])

    @staticmethod
    def display_result_with_first_card(player_dict, croupier_dict):
        print("Ваши карты:",
              ' '.join(player_dict['player_cards']),
              'Очки:', player_dict['player_score'],
              "\nКарты крупье:",
              ' '.join(croupier_dict['player_cards']),
              'Очки:', croupier_dict['player_score'])

    @staticmethod
    def display_result_without_first_card(player_dict, croupier_dict):
        print("Ваши карты:",
              ' '.join(player_dict['player_cards']),
              'Очки:', player_dict['player_score'],
              "\nКарты крупье: ???",
              ' '.join(croupier_dict['player_cards'][1:]))

    @staticmethod
    def continue_the_game():
        try:
            answer = input("Продолжить игру(y/n)? ")
            if answer[0] != 'y' and answer[0] != 'n':
                while answer[0] != 'y' and answer[0] != 'n':
                    answer = input("Ошибка! Хотите ли вы продолжить игру(y/n)? ")

            if answer[0] == 'y':
                return True

            elif answer[0] == 'n':
                return False

        except IndexError:
            return False

    @staticmethod
    def display_player_money(player_money):
        print("Ваш баланс:", player_money)

    @staticmethod
    def display_player_bet():
        try:
            bet = int(input("Ваша ставка (макс. 800$, мин. 100$)? "))
        except ValueError:
            bet = 100
        return bet

    @staticmethod
    def display_fill_up_a_purse():
        try:
            money = int(input("Пополните баланс(макс. 10000$, мин 1000$): "))
            if money > 10000 or money < 1000:
                return 1000
            else:
                return money
        except ValueError:
            return 1000

    @staticmethod
    def display_message_about_croupier():
        print("Крупье добирает карты!!!")

    @staticmethod
    def display_message_about_lose():
        print("Поражение!!!")

    @staticmethod
    def display_message_about_win():
        print("Победа!!!")

    @staticmethod
    def display_message_about_draw():
        print("Ничья!!!")

    @staticmethod
    def display_border():
        print('____________________________________')

