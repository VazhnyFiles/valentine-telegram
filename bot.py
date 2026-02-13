from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "8371536086:AAF_CtFwgg3-qA4bekMSk3jfCTwJGmB40NI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Бот запущен ")
    
@dp.message(F.web_app_data)
async def webapp_handler(message: Message):
    if message.web_app_data.data == "VALENTINE_ACCEPTED":
        await message.answer("She said YES!!! ")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

