# Телеграм-бот Угадай число
Бот, написанный на aiogram, суть которого в том, чтобы играть с пользователем в игру Угадай число.

## Локальный запуск
Чтобы запусить бота локально нужно для начала создать бота в [BotFather](https://t.me/BotFather). Шаги, чтобы создать бота описаны [здесь](https://botcreators.ru/blog/kak-sozdat-svoego-bota-v-botfather/#:~:text=%D0%94%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%B1%D0%BE%D1%82%D0%B0%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B8%D1%82%D0%B5%20%D0%B2,%D0%B8%20%D0%B2%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BE%20%D0%B1%D0%BE%D1%82%D0%B5.)

После того, как бот создан, нужно скопировать его токен и присвоить его переменной окружения `BOT_TOKEN`. Файл `.env` должен находится в директории `tg_bot_guess_number`. После этого можно приступать к установке зависимостей.

### poetry
```bash
poetry shell
poetry install
```

### pip
```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

После утановки зависмостей в КОРНЕ проекта нужно выполнить:
```bash
make start_bot
```