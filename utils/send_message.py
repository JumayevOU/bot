from loader import bot  

async def send_to_group(chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id, text=text, parse_mode="HTML")