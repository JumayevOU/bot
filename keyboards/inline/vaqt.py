from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


soat_keyboard = InlineKeyboardMarkup(row_width=3)

soat_keyboard.add(
    InlineKeyboardButton(text='⏰ 10:00 - 11:00', callback_data='10:00 - 11:00'),
    InlineKeyboardButton(text='⏰ 11:00 - 12:00', callback_data='11:00 - 12:00'),
    InlineKeyboardButton(text='⏰ 12:00 - 13:00', callback_data='12:00 - 13:00'),
    InlineKeyboardButton(text='⏰ 14:00 - 15:00', callback_data='14:00 - 15:00'),
    InlineKeyboardButton(text='⏰ 15:00 - 16:00', callback_data='15:00 - 16:00'),
    InlineKeyboardButton(text='⏰ 16:00 - 17:00', callback_data='16:00 - 17:00'),
    InlineKeyboardButton(text='⏰ 17:00 - 18:00', callback_data='17:00 - 18:00'),
    InlineKeyboardButton(text='⏰ 18:00 - 19:00', callback_data='18:00 - 19:00'),
    InlineKeyboardButton(text='⏰ 19:00 - 20:00', callback_data='19:00 - 20:00')
)
