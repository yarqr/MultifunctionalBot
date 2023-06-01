from aiogram import Router
from aiogram.types import ErrorEvent
from loguru import logger

router = Router()


@router.errors()
async def error_handler(error: ErrorEvent) -> None:
    logger.warning(f"«Telegram Error»: {error.exception}")
