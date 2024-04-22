from aiogram import Router,F,types
from aiogram.filters import Command


kafe_router =Router()

@kafe_router.message(Command('kafe'))
async def kafe(message:types.Message):
    kb =types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='европейская кухня'),
                types.KeyboardButton(text='восточная кухня'),
            ],
            [
                types.KeyboardButton(text='китайская кухня'),
                types.KeyboardButton(text='турецкая кухня'),
            ]

        ],
        resize_keyboard=True
    )
    await message.answer('Выберите меню', reply_markup=kb)


@kafe_router.message(F.text.lower()=='европейская кухня')
async def show_evrope(message:types.Message):
    print(message.text)
    await message.answer('блюда от шеф повара для вас!')


@kafe_router.message(F.text.lower()=='восточная кухня')
async def show_vostoc(message:types.Message):
    print(message.text)
    await message.answer('блюда Востока  для вас!')


@kafe_router.message(F.text.lower()=='китайская кухня')
async def show_china(message:types.Message):
    print(message.text)
    await message.answer('блюда Китая  для вас!')

@kafe_router.message(F.text.lower()=='турецкая кухня')
async def show_china(message:types.Message):
    print(message.text)
    await message.answer('блюда Турции для вас!')