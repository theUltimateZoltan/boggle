
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
