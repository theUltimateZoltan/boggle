from board import Board
from boggle_config import GameConfig as Cfg


class Utilities:
    def __init__(self, app):
        self.__app = app
        self.__board = Board()
        self.__score = 0
        self.__correct_words = set()
        self.__wrong_words = set()

    def get_board(self):
        return self.__board

    def get_score(self):
        return self.__score

    def reset(self):
        self.__board.shuffle_board()
        self.__score = 0
        self.__correct_words.clear()
        self.__correct_words.clear()

    def add_score(self, score):
        self.__score += score

    def buy_time(self):
        self.__score -= Cfg.Buy_time_price
        """self.__remaining_time += Cfg.Buy_time_seconds"""


    def add_word(self, word):
        """
        Check if the word is valid and add it to the fitting list
        :param word: word to add
        :return: Tuple (valid, msg)
        """
        if word not in self.__correct_words and word not in self.__wrong_words:
            if self.check_valid_word(word):
                self.__correct_words.add(word)
                pts = Cfg.score_calc(word)
                self.__score += pts
                self.__app.refresh()
                return True, "Yes! "+str(pts)+" Points!"
            else:
                self.__wrong_words.add(word)
                return False, "Oops! Try again."
        return None, "You already tried that."

    @staticmethod
    def check_valid_word(word):
        """
        Checks if a given word is valid
        :return: boolean value
        """
        return word in Cfg.load_words()