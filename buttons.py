from aiogram.types import InlineKeyboardButton


def call_button(name):
    return InlineKeyboardButton(text=name, callback_data=name)