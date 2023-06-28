import os

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message

from mybot.config import settings
from mybot.services.utils import check_sub


class SubChecker(BaseFilter):
    async def __call__(self, msg: Message, bot: Bot) -> bool:
        sub = await check_sub(bot, os.getenv("CHANNEL_ID") or settings.CHANNEL_ID, msg.from_user.id)
        if sub:
            return True
        await msg.answer("You aren't subscribed to the channel!")
        return False
