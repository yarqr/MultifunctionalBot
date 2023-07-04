from aiogram import BaseMiddleware
from aiogram.types import Message


class TranslatorRunnerMiddleware(BaseMiddleware):
    async def __call__(self, handler: callable, event: Message, data: dict) -> None:
        language = "en"  # get from db or from event: event.from_user.language_code
        data['i18n'] = data['_translator_hub'].get_translator_by_locale(language)
        await handler(event, data)
