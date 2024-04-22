from aiogram import Router,F,types
from aiogram.filters import Command


shop_router =Router()



@shop_router.message(Command('shop'))
async def shop(message:types.Message):
    kb =types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Drama'),
                types.KeyboardButton(text='Romance'),
            ],
            [
                types.KeyboardButton(text='horror'),
                types.KeyboardButton(text='Fantastic'),
            ]

        ],
        resize_keyboard=True
    )
    await message.answer('choose janr', reply_markup=kb)


genres=['drama','romantika','horror','fantastika']


@shop_router.message(F.text.lower().in_(genres))
async def show_horor(message:types.Message):
    genre=message.text.lower()
    print(genre)
    kb=types.ReplyKeyboardRemove()
    print(message.text)
    await message.answer('all books horrors')