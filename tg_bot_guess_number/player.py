class MatchInfo:
    """
    Класс представляет собой партию в игру Угадай число.

    Он хранит информацию о партии, такую как загаданное число, количесто оставшихся попыток
    у пользователя, находится ли он в игре и хочет ли он начал игру.
    """
    def __init__(self, guessed_number: int, amount_try: int, in_game: bool, start_game: bool):
        self.guessed_number = guessed_number
        self.in_game = in_game
        self.start_game = start_game
        self.amount_try = amount_try
    
    def set_default_values(self):
        self.guessed_number = 0
        self.in_game = False
        self.start_game = False
        self.amount_try = 5