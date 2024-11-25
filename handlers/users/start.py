from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.kurslar import kurslar_Keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}\n<b>Tramplin</b> IT akademiyasi Supportlarni band qilish botiga xush kelibsiz!")
    await message.answer(f"Kurslarni tanlang⤵️",reply_markup=kurslar_Keyboard)
