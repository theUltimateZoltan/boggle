
from board import Board
from screen import Screen
from boggle_config import GameConfig as Cfg
from threading import Timer
import sys


class GameRunner:
    def __init__(self):
        self.__score = 0
        self.__timer = Timer(1.0, self.every_second)
        self.__remaining_time = Cfg.game_time
        self.__correct_words = set()
        self.__wrong_words = set()

    def set_screen(self, screen):
        self.__screen = screen

    def run(self):
        """
        Start running the game with default settings.
        :return: None
        """
        self.__screen.start_screen()
        self.__timer.start()

    def every_second(self):
        self.__remaining_time -= 1
        # screen - change timer printed
        if self.__remaining_time <= 0:
            self.times_up()

    def reset(self):
        pass

    def exit(self):
        pass

    def add_score(self, score):
        # screen - print "well done" message
        self.__score += score

    def buy_time(self):
        self.__score -= Cfg.Buy_time_price
        self.__remaining_time += Cfg.Buy_time_seconds

    def times_up(self):
        self.__timer.cancel()
        # screen - show end game message

    def start_play(self):
        pass

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


if __name__ == "__main__":
    runner = GameRunner()
    board = Board()
    screen = Screen(runner, board)
    screen.start_screen()
