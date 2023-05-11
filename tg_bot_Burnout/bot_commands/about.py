from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command('about'))
async def about(message: types.Message):
    text = "Этого бота написал Савинков Владислав Олегович, студен третьего курса МГППУ, в качестве своей лабораторной" \
           " работы.\n\n Задача бота очень проста, он помогает выявить ваш профессиональный уровень выгорания. \n\n С" \
           " обратной связью можете написать мне в telegem @FrowningCat или на почту vsavinkov60@gmail.com"
    await message.answer(text=text)
