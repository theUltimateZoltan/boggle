
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

    def run(self):
        """
        Start running the game with default settings.
        :return: None
        """
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

    def add_letter(self, row, col):
        self.__board.check_valid_position(row, col)

    def times_up(self):
        self.__timer.cancel()
        # screen - show end game message

    def start_play(self):
        pass



if __name__ == "__main__":
    board = Board()
    runner = GameRunner()
    screen = Screen(runner, board)
    screen.start_screen()