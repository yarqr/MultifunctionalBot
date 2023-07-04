from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot) -> None:
    bot_commands = [
        BotCommand(command="pay", description="Show invoice"),
        BotCommand(command="check_sub", description="Subscription checking")
    ]
    await bot.set_my_commands(bot_commands)
