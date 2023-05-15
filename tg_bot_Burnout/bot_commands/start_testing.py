import json

from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram import types
from answers import CallbackOnStart
from keyboard import kb

list = ['0', '1', '2', '3', '4', '5', '6']
arr1 = []
arr2 = []
arr3 = []


@dp.message_handler(Command('on_start_burnout_test'))
async def on_start_test(message: types.Message):
    id = message.from_user.id
    with open('interviewed.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            if int(i) == id:
                user = False
                break
            else:
                user = True
    if user:
        await message.answer('Сколько вам лет?\nНапишите ответ (только число)',
                             reply_markup=ReplyKeyboardRemove())
        await CallbackOnStart.Q1.set()
    else:
        await message.answer(text="Вы уже проходили тест")


@dp.message_handler(state=CallbackOnStart.Q1)
async def tower(message: types.Message):
    # anse = False
    # if message.text not in list:
    await message.answer(
        text="Вопрос №1\nЯ чувствую себя эмоционально опустошены\nВыберите по шкале от 0 до 6, где 0 это 'Не чусвую совсем себя опустошенным', а 6 'Постоянно чуствую себя опустошенным'",
        reply_markup=kb)
    #     await message.answer('Введите число')
    # else:
    #     anse = True
    # if anse:
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q2)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №2\nПосле работы я чувствую себя как 'выжатый лимон'",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q3)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №3\nУтром я чувствую усталость и не желание идти на работу ",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q4)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №4\nЯ хорошо понимаю, что чувствуют мои подчиненные и коллеги, и стараюсь учитывать это в интересах дела",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q5)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №5\nЯ чувствую, что общаюсь с некоторыми подчиненными и коллегами как с предметами (без теплоты и расположения к ним)",
        reply_markup=kb)
    arr2.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q6)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №6\nПосле работы на некоторое время хочется уединиться от всех и всего",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q7)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №7\nЯ умею находить правильное решение в конфликтных ситуациях, возникающих при общении с коллегами",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q8)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №8\nЯ чувствую угнетенность и апатию",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q9)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №9\nЯ уверен, что моя работа нужна людям",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q10)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №10\nВ последнее время я стал более «черствым» по отношению к тем, с кем работаю",
        reply_markup=kb)
    arr2.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q11)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №11\nЯ замечаю, что моя работа ожесточает меня",
        reply_markup=kb)
    arr2.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q12)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №12\nУ меня много планов на будущее, и я верю в их осуществление",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q13)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №13\nМоя работа все больше меня разочаровывает",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q14)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №14\nМне кажется, что я слишком много работаю",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q15)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №15\nБывает, что мне действительно безразлично то, что происходит c некоторыми моими подчиненными и коллегами",
        reply_markup=kb)
    arr2.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q16)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №16\nМне хочется уединиться и отдохнуть от всего и всех",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q17)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №17\nЯ легко могу создать атмосферу доброжелательности и сотрудничества в коллективе",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q18)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №18\nВо время работы я чувствую приятное оживление",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q19)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №19\nБлагодаря своей работе я уже сделал в жизни много действительно ценного",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q20)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №20\nЯ чувствую равнодушие и потерю интереса ко многому, что радовало меня в моей работе",
        reply_markup=kb)
    arr1.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q21)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №21\nНа работе я спокойно справляюсь с эмоциональными проблемами",
        reply_markup=kb)
    arr3.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q22)
async def tower(message: types.Message):
    await message.answer(
        text="Вопрос №22\nВ последнее время мне кажется, что коллеги и подчиненные все чаще перекладывают на меня груз своих проблем и обязанностей",
        reply_markup=kb)
    arr2.append(message.text)
    await CallbackOnStart.next()


@dp.message_handler(state=CallbackOnStart.Q23)
async def end(message: types.Message):
    await message.answer(text="Ваш результат:", reply_markup=ReplyKeyboardRemove())
    x = [int(s) for s in arr1]
    X = sum(x)
    y = [int(s) for s in arr2]
    Y = sum(y)
    z = [int(s) for s in arr3]
    Z = sum(z)
    if (X < 16):
        await message.answer("Ваш уровень эмоционального истощения: 1")
    elif (X > 15) and (X < 25):
        await message.answer("Ваш уровень эмоционального истощения: 2")
    else:
        await message.answer("Ваш уровень эмоционального истощения: 3")
    if (Y < 6):
        await message.answer("Ваш уровень деперсонализации: 1")
    elif (Y > 5) and (Y < 11):
        await message.answer("Ваш уровень деперсонализации: 2")
    else:
        await message.answer("Ваш уровень деперсонализации: 3")
    if (Z > 36):
        await message.answer("Ваш уровень редукции профессионализма: 1")
    elif (Z > 30) and (Z < 37):
        await message.answer("Ваш уровень редукции профессионализма: 2")
    else:
        await message.answer("Ваш уровень редукции профессионализма: 3")
