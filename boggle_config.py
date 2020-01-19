
class GameConfig:
    Buy_time_price = 10
    Buy_time_seconds = 10

    game_time = 180  # seconds

    def score_calc(self, word):
        length = len(word)
        return length ** 2