from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import asyncio
from random import randint

from config import settings
from match_info import MatchInfo
from bot_answers import BotAnswers

match_info = MatchInfo()
dp = Dispatcher()


async def process_start(message: Message):
    match_info.start_game = True
    await message.answer(BotAnswers.greet(message.from_user.username))


async def cancel_game(message: Message):
    match_info.set_default_values()
    await message.answer(BotAnswers.CANCEL_GAME)

async def start_game(message: Message):
    match_info.start_game = True
    match_info.in_game = True
    match_info.guessed_number = randint(1, 100)
    await message.answer(BotAnswers.START_MATCH)


async def guess_number(message: Message):
    message_text = message.text

    if not message_text.isdigit():
        await message.answer(BotAnswers.not_digit)
        return
    elif match_info.amount_try == 1:
        await message.answer(BotAnswers.lose_match(match_info.guessed_number))
        match_info.set_default_values()
        return
    
    user_number = int(message_text)

    if user_number > match_info.guessed_number:
        match_info.amount_try -= 1
        await message.answer(BotAnswers.greater_guessed_number(match_info.amount_try))
    elif user_number < match_info.guessed_number:
        match_info.amount_try -= 1
        await message.answer(BotAnswers.less_guessed_number(match_info.amount_try))
    else:
        match_info.amount_try -= 1
        await message.answer(BotAnswers.win_match(match_info.amount_try))
        match_info.set_default_values()



async def exit_game(message: Message):
    match_info.in_game = False
    match_info.start_game = False
    await message.answer(BotAnswers.EXIT_GAME)


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
