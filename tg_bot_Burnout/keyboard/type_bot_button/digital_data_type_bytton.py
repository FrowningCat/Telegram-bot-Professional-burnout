from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def towers():
    list_button_name = ['1', '2', '3', '4', '5', '6']

    buttons_list = []
    for item in list_button_name:
        l = []
        for i in item:
            l.append(InlineKeyboardButton(text=i, callback_data=i))
        buttons_list.append(l)

    keyboard_inline_buttons = InlineKeyboardMarkup(inline_keyboard=buttons_list)
    return keyboard_inline_buttons

def towers2():
    list_button_name = ['1', '2', '3', '4', '5', '6']

    buttons_list = []
    for item in list_button_name:
        l = []
        for i in item:
            l.append(InlineKeyboardButton(text=i, callback_data=i))
        buttons_list.append(l)

    keyboard_inline_buttons = InlineKeyboardMarkup(inline_keyboard=buttons_list)
    return keyboard_inline_buttons
