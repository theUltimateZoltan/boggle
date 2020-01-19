
from board import Board
from screen import Screen
from boggle_config import GameConfig
import sys


class GameRunner:
    def __init__(self):
        self.__board = Board()
        self.__score = 0
        self.__time = 0
        self.__correct_words = set()
        self.__wrong_words = set()

    def run(self):
        pass

    def reset(self):
        pass

    def exit(self):
        pass

    def set_score(self):
        pass

    def add_word(self):
        pass

    def buy_time(self):
        pass

    def add_letter(self):
        pass

    def times_up(self):
        pass


if __name__ == "__name__":
    runner = GameRunner()
    runner.run()
