from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest


async def check_sub(bot: Bot, channel_id: int, user_id: int) -> bool:
    try:
        user = await bot.get_chat_member(channel_id, user_id)
        return user.status != "left"
    except TelegramBadRequest:
        return False
