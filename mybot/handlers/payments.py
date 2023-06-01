from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

from mybot.config import settings

router = Router()


@router.message(Command("pay"))
async def command_pay(msg: Message):
    prices = [LabeledPrice(label="Product", amount=50000)]  # Price of the product in the smallest units of the currency
    await msg.reply_invoice("Title", "Description", "test_payload", settings.PROVIDER_TOKEN, "RUB", prices)


@router.pre_checkout_query()
async def pre_checkout_query(pcq: PreCheckoutQuery):
    await pcq.answer(ok=True)


@router.message(F.successful_payment.invoice_payload == "test_payload")
async def successful_payment(msg: Message):
    await msg.reply("Thank you!")
