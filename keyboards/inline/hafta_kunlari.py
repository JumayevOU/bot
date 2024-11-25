from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



hafta_kunlari_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📅 Dushanba', callback_data='Dushanba'),
            InlineKeyboardButton(text='📅 Seshanba', callback_data='Seshanba'),
        ],
                [
            InlineKeyboardButton(text='📅 Chorshanba', callback_data='Chorshanba'),
            InlineKeyboardButton(text='📅 Payshanba', callback_data='Payshanba'),
        ],
                [
            InlineKeyboardButton(text='📅 Juma', callback_data='Juma'),
            InlineKeyboardButton(text='📅 Shanba', callback_data='Shanba'),
        ],
    ])

