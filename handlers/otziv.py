from aiogram import Router,F,types
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import sqlite3
from config import database


otziv_router=Router()


db=sqlite3.connect("db.sqlite")
cursor=db.cursor()


class BookOtziv(StatesGroup):
    name=State()
    number=State()
    vizit=State()
    rate =State()
    clean =State()
    comments =State()


@otziv_router.message(Command("stop"))
@otziv_router.message(F.text.lower()=="stop")
async def stop(message:types.Message,state:FSMContext):
    await state.clear()
    


@otziv_router.callback_query(F.data=="otziv")
async def start_otziv(cb:types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(BookOtziv.name)
    await cb.message.answer("Как вас зовут?")


@otziv_router.message(BookOtziv.name)
async def process_name(message:types.Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookOtziv.number)
    await message.answer(f"Оставьте ваш номер телефона пожалуйста,{message.text}?")


@otziv_router.message(BookOtziv.number)
async def process_number(message:types.Message,state:FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(BookOtziv.vizit)
    await message.answer("Напишите пожалуйста дату посещения нашего заведения")   


@otziv_router.message(BookOtziv.vizit)
async def process_vizit(message:types.Message,state:FSMContext):
    vizit=message.text
    if not vizit.isdigit():
        await message.answer("Пожалуйста , ведите число")
        return
    if int(vizit) < 1 or int(vizit)>31:
        await message.answer("Введите число от 1-31")
        return
    await state.update_data(vizit=int(vizit))
    await state.set_state(BookOtziv.rate)
    kb = [
       [   
            types.KeyboardButton(text="Отлично"),
            types.KeyboardButton(text="хорошо")
      ],
      [
          types.KeyboardButton(text="Плохо"),
          types.KeyboardButton(text="Удовлетворительно")

      ]
     ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Нажмите для рейтинга кнопки"
    )
    await message.answer("Как оценивете качество еды?", reply_markup=keyboard)


@otziv_router.message(BookOtziv.rate)
async def process_rate(message:types.Message,state:FSMContext):
    await state.update_data(rate=message.text)
    await state.set_state(BookOtziv.clean)
    await message.answer("Оцените чистоту заведения")


@otziv_router.message(BookOtziv.clean)
async def process_clean(message:types.Message,state:FSMContext):
    await state.update_data(clean=message.text)
    await state.set_state(BookOtziv.comments)
    await message.answer("Оставьте пожалуйста ваши комментарии")

@otziv_router.message(BookOtziv.comments)
async def process_comments(message:types.Message,state:FSMContext):
    await state.update_data(comments=message.text)
    data=await state.get_data()
    print ("~",data)


    await database.execute(
        "INSERT INTO otziv (name,number,vizit,rate,clean,comments) VALUES(?,?,?,?,?,?)",
         (data["name"], data["number"], data["vizit"], data["rate"], data["clean"], data["comments"]))
    await message.answer("спасибо за пройденный опрос")
    await state.clear()