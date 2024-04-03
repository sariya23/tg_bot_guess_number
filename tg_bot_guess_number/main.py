from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import asyncio
from random import randint

from config import settings
from match_info import MatchInfo


match_info = MatchInfo()
dp = Dispatcher()


async def process_start(message: Message):
    match_info.start_game = True
    await message.answer(
        f'Привет, {message.from_user.username}!\nХочешь сыгарать в игру "Угадай число"?\nНапишии мне Да или Нет'
    )


async def cancel_game(message: Message):
    match_info.set_default_values()
    await message.answer(
        "Отменяю текущую игру. Чтобы начать играть заново введи команду /start"
    )


async def start_game(message: Message):
    match_info.start_game = True
    match_info.in_game = True
    match_info.guessed_number = randint(1, 100)
    await message.answer("Начнем! Я загадал число от 1 до 100. У тебя будет 5 попыток")


async def guess_number(message: Message):
    message_text = message.text

    if not message_text.isdigit():
        await message.answer(f"{message_text} - не число. Ты угадываешь числа, а не что-то другое. Не буду снимать количество попыток, может ты просто упал на клавиатуру")
        return
    elif match_info.amount_try == 1:
        await message.answer(f"Ты проиграл, у тебя кончились попытки.\nЯ загадывал число {match_info.guessed_number}\nЧтобы сыграть еще введи команду /start")
        match_info.set_default_values()
        return
    
    user_number = int(message_text)

    if user_number > match_info.guessed_number:
        match_info.amount_try -= 1
        await message.answer(f"Твое число больше загаданного.\nУ тебя осталось {match_info.amount_try} попыток(и)")
    elif user_number < match_info.guessed_number:
        match_info.amount_try -= 1
        await message.answer(f"Твое число меньше загаданного.\nУ тебя осталось {match_info.amount_try} попыток(и)")
    else:
        match_info.amount_try -= 1
        await message.answer(f"Ура, ты выиграл!\nТы справился за {5 - match_info.amount_try} попыток(и)")
        match_info.set_default_values()



async def exit_game(message: Message):
    match_info.in_game = False
    match_info.start_game = False
    await message.answer("Ну ладно(")


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp.message.register(process_start, Command(commands="start"))
    dp.message.register(cancel_game, Command(commands="cancel"))
    dp.message.register(
        start_game,
        lambda msg: msg.text.lower() in ("yes", "да", "давай", "go", "ок")
        and not match_info.in_game
        and match_info.start_game,
    )
    dp.message.register(
        exit_game,
        lambda msg: msg.text.lower() in ("no", "нет", "не")
        and not match_info.in_game
        and match_info.start_game,
    )
    dp.message.register(
        guess_number,
        lambda _: match_info.in_game
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
