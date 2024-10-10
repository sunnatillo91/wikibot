import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

# wikipedia.set_lang('uz')

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7466032534:AAFpWAzQiipegNSoWudnsvxv5df2OaK9kq0"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(Command(commands=['start', 'help']))
async def start(message: types.Message):
    await message.answer("Wikipeida Botiga Xush Kelibsiz!")

# All handlers should be attached to the Router (or Dispatcher)

@dp.message()
# async  def sendWiki(message: types.Message):
#     try:
#         result = wikipedia.summary(message.text)
#         await message.answer(result)
#     except:
#         await message.answer("So'rovingizga bog'liq ma'lumot wikipediadan topilmadi")

# import requests


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())