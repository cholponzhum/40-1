from aiogram import Router,types
import logging

echo_router=Router()


@echo_router.message()
async def echo(message:types.Message):
    logging.info(message)
    await message.answer("I dont understand try again: \n"
                         "/start-start dialog \n"
                         "/myinfo-about info \n"
                         "/picture-send pictute \n"
                         "/otziv-otziv \n"
                         "/survey-opros \n"
                         "/shop-magazin \n"
                         "/kafe-choose menu \n")