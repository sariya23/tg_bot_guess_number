class BotAnswers:
    CANCEL_GAME = "Отменяю текущую игру. Чтобы начать играть заново введи команду /start"
    START_MATCH = "Начнем! Я загадал число от 1 до 100. У тебя будет 5 попыток"
    EXIT_GAME = "Ну ладно("

    @classmethod
    def greet(cls, username: str) -> str:
        return f"Привет, {username}!\nХочешь сыгарать в игру \"Угадай число\"?\nНапишии мне Да или Нет" 
    
    @classmethod
    def not_digit(cls, user_input: str) -> str:
        return f"{user_input} - не число. Ты угадываешь числа, а не что-то другое. Не буду снимать количество попыток, может ты просто упал на клавиатуру"
    
    @classmethod
    def no_attempts(cls, guessed_number: int) -> str:
        return f"Ты проиграл, у тебя кончились попытки.\nЯ загадывал число {guessed_number}\nЧтобы сыграть еще введи команду /start"

    @classmethod
    def greater_guessed_number(cls, amount_try: int) -> str:
        return f"Твое число больше загаданного.\nУ тебя осталось {amount_try} попыток(и)"

    @classmethod
    def less_guessed_number(cls, amount_try: int) -> str:
        return f"Твое число меньше загаданного.\nУ тебя осталось {amount_try} попыток(и)"
    
    @classmethod
    def win_game(cls, amount_try: int) -> str:
        return f"Ура, ты выиграл!\nТы справился за {5 - amount_try} попыток(и)"
    