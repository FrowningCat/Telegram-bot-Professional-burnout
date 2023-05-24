from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command("about"))
async def about(message: types.Message):
    text = "Данного бота написал Савинков Владислав Олегович, студен третьего курса МГППУ, в качестве своей лабораторной" \
           " работы.\n\nЗадача бота очень проста, он предоставляет возможность пройти несколко опросов. \n\nС" \
           " обратной связью можете написать мне в \ntelegem @FrowningCat или на \nпочту vsavinkov60@gmail.com"
    await message.answer(text=text)
