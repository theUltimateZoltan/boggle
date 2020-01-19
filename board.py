from boggle_board_randomizer import randomize_board
from boggle_config import GameConfig as Cfg
import math


class Board:

    def __init__(self):
        self.__board = [['A', 'H', 'P', 'O'], ['I', 'V', 'D', 'S'], ['G', 'H', 'D', 'T'], ['Y', 'E', 'H', 'N']]
        self.__valid_words = Cfg.load_words()
        self.__current_word = str()
        self.__selected_indices = list()  # list of tuples [(1,2), (3,4),...]

    @staticmethod
    def shuffle_board():
        """
        Returns randomized board
        :return: 2D list of letters
        """
        return randomize_board()

    def get_board(self):
        """
        :return: board (2D List)
        """
        return self.__board

    def get_current_word(self):
        """
        :return: current combination (string)
        """
        return self.__current_word

    def clear_current_word(self):
        self.__current_word = ""
        self.__selected_indices = []

    def check_valid_position(self, row, col):
        """
        Checks if a given letter is adjacent to the last selected
        letter in board.
        :return: boolean value
        """
        # no possible constraints if current word combination is empty
        if not self.__selected_indices:
            return True

        # makes sure we don't add the same letter twice
        if (row, col) in self.__selected_indices:
            return False

        # stores the last selected letter's index
        i, j = self.__selected_indices[-1][0], self.__selected_indices[-1][0]

        # checks if current letter position is adjacent to last one
        if math.fabs(row - i) <= 1 or math.fabs(col - j) <= 1:
            return True
        return False

    def add_letter(self, position):
        """
        Adds a single letter to the current word combination and updates
        the indices list by the given letter position in board,
        only if letter is valid.
        :param position: index of a letter in board (row,col)
        :return: None
        """
        try:  # checks position's range
            letter = self.__board[position[0]][position[1]]
        except IndexError:
            return  # there is no such position in board

        # check proximity
        if self.check_valid_position(*position):
            self.__current_word += letter
            self.__selected_indices.append(position)

    def check_valid_word(self, word):
        """
        Checks if a given word is valid
        :return: boolean value
        """
        return word in self.__valid_words

    def get_indices(self):
        return self.__selected_indices


b = Board()
print(b.get_board())
b.add_letter((-23, 0))
print("Combination :", b.get_current_word(), "\nIndexes: ", b.get_indices())
b.add_letter((0, 1))
print("Combination :", b.get_current_word(), "\nIndexes: ", b.get_indices())
b.add_letter((0, 2))
print("Combination :", b.get_current_word(), "\nIndexes: ", b.get_indices())
b.add_letter((0, 3))
print("Combination :", b.get_current_word(), "\nIndexes: ", b.get_indices())
b.add_letter((0, 0))
print("Combination :", b.get_current_word(), "\nIndexes: ", b.get_indices())
b.add_letter((0, 0))
print("Combination :", b.get_current_word(), "\nIndexes: ", b.get_indices())



