from boggle_board_randomizer import randomize_board


class Board:

    def __init__(self):
        self.__board = self.shuffle_board()
        self.__current_word = str()
        self.__valid_words = list()

    @staticmethod
    def shuffle_board():
        return randomize_board()

    def get_board(self):
        return self.__board

    def get_current_word(self):
        return self.__current_word

    def load_words(self):
        pass

    def check_valid_letter(self):
        pass

