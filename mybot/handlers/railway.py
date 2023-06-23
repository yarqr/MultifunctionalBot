from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("railway"))
async def command_railway(msg: Message):
    await msg.reply("Hello from Railway!")
