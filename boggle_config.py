
class GameConfig:

    @staticmethod
    def load_words(file='boggle_dict.txt'):
        """
        Loads a list of words from boggle_dict.txt file
        :param file: The file of words
        :return: A list containing all the words from the file
        """
        with open(file) as f:
            words = {line.strip() for line in f}
        return words
    Buy_time_price = 10
    Buy_time_seconds = 10

    game_time = 180  # seconds

    def score_calc(self, word):
        length = len(word)
        return length ** 2