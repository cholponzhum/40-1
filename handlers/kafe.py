from aiogram import Router,F,types
from aiogram.filters import Command
from config import database


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

cuisines=['европейская кухня','восточная кухня','китайская кухня','турецкая кухня']

@kafe_router.message(F.text.lower().in_(cuisines))
async def show_evrope(message:types.Message):
    cuisine=message.text.lower()
    print(cuisine)
    kb=types.ReplyKeyboardRemove()
    data = await database.fetch(
        """
        SELECT foods.* FROM foods
        JOIN cuisines ON foods.cuisine_id = cuisines.id
        WHERE cuisines.name = ?
        """,
        (cuisine,),
        fetch_type='all'
    )

    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=kb)
    await message.answer(f'блюда от шеф повара для вас!{cuisine}:')
    for food in data:
        price = food['price']
        name = food['name']
        photo = types.FSInputFile(food['picture'])
        await message.answer_photo(
            photo=photo,
            caption=f'Название блюда: {name}\nPrices: {price} сом'
        )

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