from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b0 = KeyboardButton('0')
b1 = KeyboardButton('1')
b2 = KeyboardButton('2')
b3 = KeyboardButton('3')
b4 = KeyboardButton('4')
b5 = KeyboardButton('5')
b6 = KeyboardButton('6')

kb = ReplyKeyboardMarkup()
kb.add(b0).add(b1).add(b2).add(b3).add(b4).add(b5).add(b6)
