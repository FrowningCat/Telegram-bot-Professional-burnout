import json

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram import types
from answers import CallbackOnStart
from keyboard.types_bot_button.digital_data_type_bytton import towers


@dp.message_handler(Command('on_start_burnout_test'))
async def on_start_test(message: types.Message):
    id = message.from_user.id
    with open('users_test_one.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            if int(i) == id:
                user = False
            break
        else:
            user = True
    if user:
        await message.answer('Сколько вам лет?\nНапишите ответ (только число)', reply_markup=ReplyKeyboardRemove())
        await CallbackOnStart.Q1.set()
    else:
        await message.answer(text="Вы уже проходили тест")


@dp.message_handler(state=CallbackOnStart.Q1)
async def tower(message: types.Message, state: FSMContext):
    b = towers()
    answer = message.text
    await state.update_data(name=answer)
    await message.answer(
        text="Вопрос №1\nЯ чувствую себя эмоционально опустошены\nВыберите по шкале от 0 до 6, где 0 это 'Не чусвую совсем себя опустошенным', а 6 'Постоянно чуствую себя опустошенным'",
        reply_markup=b)
    await CallbackOnStart.next()


@dp.callback_query_handler(state=CallbackOnStart.Q2)
async def end(call: types.Message, state: FSMContext):
    answer = call.data
    await state.update_data(full_name=call.from_user.full_name)
    await state.update_data(repost=answer)
    data = await state.get_data()
    user = {call.from_user.id: data}
    text = []
    for i in data:
        text.append(f'{data[i]}\n')
    await call.message.answer(text="Ваши ответы:", reply_markup=ReplyKeyboardRemove())
    await call.message.answer('\n'.join(text))
    with open('users_test_one.json', encoding='utf-8') as file:
        data = json.load(file)
        data.update(user)
        with open('users_test_one.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
    await state.finish()
