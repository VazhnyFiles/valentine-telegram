import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)

BOT_TOKEN = "8371536086:AAF_CtFwgg3-qA4bekMSk3jfCTwJGmB40NI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_all_messages(message: Message):

    # Если это /start
    if message.text == "/start":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Open Valentine 💌",
                    web_app=WebAppInfo(
                        url="https://vazhnyfiles.github.io/valentine-telegram/"
                    )
                )
            ]
        ])

        await message.answer("Click to open ❤️", reply_markup=keyboard)
        return

    # Если пришли данные из Mini App
    if message.web_app_data:
        if message.web_app_data.data == "VALENTINE_ACCEPTED":
            await message.answer("She said YES!!! ❤️🔥")
        else:
            await message.answer("Unknown data received.")


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
