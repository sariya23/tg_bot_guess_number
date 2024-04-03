from dataclasses import dataclass

@dataclass
class MatchInfo:
    """
    Класс представляет собой партию в игру Угадай число.

    Он хранит информацию о партии, такую как загаданное число, количесто оставшихся попыток
    у пользователя, находится ли он в игре и хочет ли он начал игру.
    """
    guessed_number: str
    amount_try: str
    in_game: bool
    start_game: bool

    def set_default(self):
        self.guessed_number = 0
        self.in_game = False
        self.start_game = False
        self.amount_try = 5