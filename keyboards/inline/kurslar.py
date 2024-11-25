from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



kurslar_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💻 BackEnd', callback_data='backend'),
        ],
        [
            InlineKeyboardButton(text='🌐 FrontEnd',callback_data='frontend'),
        ],
        [
            InlineKeyboardButton(text="👾 Kiber xavfsizlik",callback_data='cyber'),
        ],
    ])

