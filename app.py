from aiogram import executor
from utils.send_message import send_to_group
from data.config import GROUP_ID
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):

    await set_default_commands(dispatcher)


    await on_startup_notify(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

