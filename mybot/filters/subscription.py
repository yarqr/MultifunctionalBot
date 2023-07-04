from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message
from fluentogram import TranslatorRunner

from mybot.config import settings
from mybot.services.utils import check_sub


class SubChecker(BaseFilter):
    async def __call__(self, msg: Message, bot: Bot, i18n: TranslatorRunner) -> bool:
        sub = await check_sub(bot, settings.CHANNEL_ID, msg.from_user.id)
        if sub:
            return True
        await msg.answer(i18n.bad.sub())
        return False
