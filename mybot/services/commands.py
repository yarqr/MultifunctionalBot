from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    bot_commands = [
        BotCommand(command="pay", description="Show invoice"),
        BotCommand(command="railway", description="Show railway"),
        BotCommand(command="check_sub", description="Subscription checking")
    ]
    await bot.set_my_commands(bot_commands)
