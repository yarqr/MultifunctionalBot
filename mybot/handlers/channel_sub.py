import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import LabeledPrice, Message

from mybot.config import settings
from mybot.filters.subscription import SubChecker

router = Router()
router.message.filter(SubChecker())


@router.message(Command("check_sub"))
async def command_pay(msg: Message):
    await msg.answer("All is good!")
