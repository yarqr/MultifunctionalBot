import asyncio

from aiogram import Bot, Dispatcher
from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub
from loguru import logger

from mybot.config import settings
from mybot.handlers import errors, payments, channel_sub
from mybot.middlewares.i18n import TranslatorRunnerMiddleware
from mybot.services.commands import set_commands


async def main() -> None:
    logger.success('Bot started')

    bot = Bot(settings.BOT_TOKEN)
    dp = Dispatcher()

    translator_hub = TranslatorHub(
        {
            "en": ("en",)
        },
        [
            FluentTranslator("en", translator=FluentBundle.from_files("en-US", filenames=["translations/en/main.ftl"]))
        ]
    )

    await set_commands(bot)
    dp.message.outer_middleware(TranslatorRunnerMiddleware())
    dp.include_routers(errors.router, payments.router, channel_sub.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), close_bot_session=True,
                           _translator_hub=translator_hub)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logger.error('Bot stopped')
