from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

from mybot.filters.subscription import SubChecker

router = Router()
router.message.filter(SubChecker())


@router.message(Command("check_sub"))
async def command_pay(msg: Message, i18n: TranslatorRunner) -> None:
    await msg.answer(i18n.check.sub())
