from aiogram.filters import Command
from aiogram import Router,types


myinfo_router=Router()


@myinfo_router.message(Command('myinfo'))
async def myinfo(message:types.Message):
    await message.answer(f'Hello \nYour ID:{message.from_user.id})\nName: {message.from_user.first_name}')