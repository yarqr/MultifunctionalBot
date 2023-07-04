from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
from fluentogram import TranslatorRunner

from mybot.config import settings

router = Router()


@router.message(Command("pay"))
async def command_pay(msg: Message) -> None:
    token = settings.PROVIDER_TOKEN
    prices = [LabeledPrice(label="Product", amount=50000)]  # Price of the product in the smallest units of the currency
    await msg.answer_invoice("Title", "Description", "test_payload", token, "RUB", prices)


@router.pre_checkout_query()
async def pre_checkout_query(pcq: PreCheckoutQuery) -> None:
    await pcq.answer(ok=True)


@router.message(F.successful_payment.invoice_payload == "test_payload")
async def successful_payment(msg: Message, i18n: TranslatorRunner) -> None:
    await msg.reply(i18n.thanks())
