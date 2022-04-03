import requests
from characters import main as choose_character
from buttons import call_button
from aiogram import Dispatcher, Bot, executor, types
from aiogram.utils.markdown import text, bold
from aiogram.types import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


tg_bot = "5205686868:AAFG8S_45cYe-E-9ltV1CISpb9VpKRxazGk"

bot = Bot(token=tg_bot)
dp = Dispatcher(bot)

character1 = InlineKeyboardMarkup(row_width=3).add(
    call_button("Morty Smith"),
    call_button("Rick Sanchez"),
    call_button("Summer Smith"),
    call_button("Jerry Smith"),
    call_button("Squanchy"),
    call_button("Beth Smith"),
    call_button("Krombopulos Michael"),
    call_button("Reverse Giraffe"),
    call_button("Birdperson")
)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(bold("Привет, пользователь 😎"), parse_mode=ParseMode.MARKDOWN)
    await message.answer("Выбери персонажа и кайфуй 🔥", reply_markup=character1)


@dp.callback_query_handler(text='Morty Smith')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Morty Smith"))


@dp.callback_query_handler(text='Rick Sanchez')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Rick Sanchez"))


@dp.callback_query_handler(text='Summer Smith')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Summer Smith"))


@dp.callback_query_handler(text='Jerry Smith')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Jerry Smith"))


@dp.callback_query_handler(text='Squanchy')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Squanchy"))


@dp.callback_query_handler(text='Beth Smith')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Beth Smith"))


@dp.callback_query_handler(text='Krombopulos Michael')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Krombopulos Michael"))


@dp.callback_query_handler(text='Reverse Giraffe')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Reverse Giraffe"))


@dp.callback_query_handler(text='Birdperson')
async def morty_sm(callback: types.CallbackQuery):
    await callback.message.answer(choose_character("Birdperson"))

if __name__ == '__main__':
    executor.start_polling(dp)