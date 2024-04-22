from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from db.database import Database




bot = Bot(token =getenv('TOKEN'))
dp = Dispatcher()
database=Database(
    Path(__file__).parent /"db.sqlite"
)



async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start",description="начинать"),
        types.BotCommand(command="picture",description="Показывать картинку рандомно"),
        types.BotCommand(command="shop",description="Магазин"),
        types.BotCommand(command="kafe",description="Кафе"),
        types.BotCommand(command="survey",description="Опрос"),
        types.BotCommand(command="otziv",description="Отзыв"),
        types.BotCommand(command="myinfo",description="inform"),

    ])
 