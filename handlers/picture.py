from aiogram import Router,types
from aiogram.filters import Command
import random
import os

picture_router=Router()


@picture_router.message(Command('picture'))
async def send_picture(message:types.Message):
    photo = types.FSInputFile('images/' + random.choice(os.listdir('images')))
    await message.answer_photo(photo=photo)