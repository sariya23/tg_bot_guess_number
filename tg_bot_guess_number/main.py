from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import asyncio
from random import randint
import dataclasses

from config import settings


user = {
    "amount_try": 0,
    "random_number": 0,
    "in_game": False
}


dp = Dispatcher()

async def process_start(message: Message):
    await message.answer(f"Привет, {message.from_user.username}!\nХочешь сыгарать в игру \"Угадай число\"?\nНапишии мне Да или Нет")


async def cancel_game(message: Message):
    user["in_game"] = False
    await message.answer("Отменяю текущую игру. Чтобы начать играть заново введи команду /start")

async def start_game(message: Message):
    user["in_game"] = True
    user["random_number"] = randint(1, 100)
    await message.answer("Начнем! Я загадал число от 1 до 100. У тебя будет 5 попыток")


async def exit_game(message: Message):
    user["in_game"] = False
    await message.answer("Ну ладно(")


async def main():
    bot = Bot(token=settings.BOT_TOKEN)
    dp.message.register(process_start, Command(commands="start"))
    dp.message.register(cancel_game, Command(commands="cancel"))
    dp.message.register(start_game, lambda msg: msg.text.lower() in ("yes", "да", "давай", "go", "ок") and not user["in_game"])
    dp.message.register(exit_game, lambda msg: msg.text.lower() in ("no", "нет", "не") and not user["in_game"])
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())