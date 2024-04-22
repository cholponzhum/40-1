from aiogram import Router,F,types
from aiogram.filters import Command



start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message:types.Message):
    
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="наш сайт", url="https://restoran.kg/cafe")
            ],

            [    types.InlineKeyboardButton(text="наш instagram", url="https://restoran.kg/cafe")
            ],
            [
                types.InlineKeyboardButton(text="Про нас",callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Адрес,контакты ",callback_data="adress")
            ],
            [
                types.InlineKeyboardButton(text= "Пройти опрос", callback_data="survey")
            ],
            [
                types.InlineKeyboardButton(text= "Оставьте отзыв", callback_data="otziv")
            ]
        ]
    )


    await message.answer(f'Hello ,{message.from_user.first_name}',reply_markup=kb)



@start_router.callback_query(F.data=="about_us")
async def about_us(cb:types.CallbackQuery):
    await cb.answer()
    await cb.message.answer("Кафе:Кухня-Европейская,восточная,китаская,турецкая")

@start_router.callback_query(F.data=="adress")
async def aadres(cb:types.CallbackQuery):
    await cb.answer()
    await cb.message.answer("Адрес:ул. Суюмбаева, 192, уг. ул. Никитина")