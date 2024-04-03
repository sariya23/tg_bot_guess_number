from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import asyncio
from random import randint

from config import settings


user = {
    "amount_try": 5,
    "random_number": 0,
    "in_game": False,
    "start_game": False,
}


dp = Dispatcher()


async def process_start(message: Message):
    user["start_game"] = True
    await message.answer(
        f'Привет, {message.from_user.username}!\nХочешь сыгарать в игру "Угадай число"?\nНапишии мне Да или Нет'
    )


async def cancel_game(message: Message):
    user["in_game"] = False
    user["start_game"] = False
    await message.answer(
        "Отменяю текущую игру. Чтобы начать играть заново введи команду /start"
    )


async def start_game(message: Message):
    user["in_game"] = True
    user["random_number"] = randint(1, 100)
    await message.answer("Начнем! Я загадал число от 1 до 100. У тебя будет 5 попыток")


async def guess_number(message: Message):
    message_text = message.text

    if not message_text.isdigit():
        await message.answer(f"{message_text} - не число. Ты угадываешь числа, а не что-то другое. Не буду снимать количество попыток, может ты просто упал на клавиатуру")
        return
    elif user["amount_try"] == 1:
        await message.answer(f"Ты проиграл, у тебя кончились попытки.\nЯ загадывал число {user['random_number']}\nЧтобы сыграть еще введи команду /start")
        user["amount_try"] = 5
        user["in_game"] = False
        user["start_game"] = False
        user["random_number"] = 0
        return
    
    user_number = int(message_text)

    if user_number > user["random_number"]:
        user["amount_try"] -= 1
        await message.answer(f"Твое число больше загаданного.\nУ тебя осталось {user['amount_try']} попыток(и)")
    elif user_number < user["random_number"]:
        user["amount_try"] -= 1
        await message.answer(f"Твое число меньше загаданного.\nУ тебя осталось {user['amount_try']} попыток(и)")
    else:
        user["amount_try"] -= 1
        await message.answer(f"Ура, ты выиграл!\nТы справился за {5 - user['amount_try']} попыток(и)")
        user["amount_try"] = 5
        user["in_game"] = False
        user["start_game"] = False
        user["random_number"] = 0



async def exit_game(message: Message):
    user["in_game"] = False
    user["start_game"] = False
    await message.answer("Ну ладно(")


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp.message.register(process_start, Command(commands="start"))
    dp.message.register(cancel_game, Command(commands="cancel"))
    dp.message.register(
        start_game,
        lambda msg: msg.text.lower() in ("yes", "да", "давай", "go", "ок")
        and not user["in_game"]
        and user["start_game"],
    )
    dp.message.register(
        exit_game,
        lambda msg: msg.text.lower() in ("no", "нет", "не")
        and not user["in_game"]
        and user["start_game"],
    )
    dp.message.register(
        guess_number,
        lambda _: user["in_game"]
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
