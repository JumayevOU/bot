from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



band_qilish_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📅 Band qilish', callback_data='band'),
        ],
    ])


check_Keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Tasdiqlash', callback_data='check'),
        ],
                [
            InlineKeyboardButton(text='❌ Bekor qilish', callback_data='bekor_qilish'),
        ],
    ])


username_Keyboard = InlineKeyboardMarkup(row_width=2)
username_Keyboard.add(
    InlineKeyboardButton("✅ Tasdiqlayman", callback_data="confirm_username"),
    InlineKeyboardButton("❌ Yo'q, o'zim kiritaman", callback_data="edit_username")
)