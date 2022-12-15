from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton(text="FRANCE INFO", callback_data="france_info")
button2 = InlineKeyboardButton(text="FRANCE INTER", callback_data="france_inter")
button3 = InlineKeyboardButton(text="FRANCE CULTURE", callback_data="france_culture")
button4 = InlineKeyboardButton(text="BRUIT BLANC", callback_data="bruit_blanc")
button5 = InlineKeyboardButton(text="CONTROLE DU SON", callback_data="controle_son")
keyboard_inline1 = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5)

button6 = InlineKeyboardButton(text="◾", callback_data="stop")
button7 = InlineKeyboardButton(text="►", callback_data="play")
button8 = InlineKeyboardButton(text="PLAYLIST", callback_data="playlist")
keyboard_inline2 = InlineKeyboardMarkup().add(button6, button7, button8)

bot = Bot(token='5625161246:AAHF1eDw49OcEeCi2VbrrAO6f1TiYJPyRoc')
dp = Dispatcher(bot)

@dp.message_handler(text=["hi"])
async def welcome_answer(message: types.Message):
    await message.reply("Salut, choisis la playlist que tu veux", reply_markup=keyboard_inline1)

@dp.callback_query_handler(text=["france_info", "france_inter", "controle_son", "playlist", "france_culture", "bruit_blanc"])
async def random_value(call: types.CallbackQuery):
    if call.data == "france_info":
        await call.message.answer("France Info dans un instant...", reply_markup=keyboard_inline2)
        await call.message.reply("France Info dans un instant...", reply_markup=keyboard_inline2)
    if call.data == "france_inter":
        await call.message.answer("France Inter dans un instant...", reply_markup=keyboard_inline2)
    if call.data == "france_culture":
        await call.message.answer("France Culture dans un instant...", reply_markup=keyboard_inline2)
    if call.data == "bruit_blanc":
        await call.message.answer("Bruit Blanc dans un instant...", reply_markup=keyboard_inline2)
    if call.data == "controle_son":
        await call.message.answer("Contrôle du son", reply_markup=keyboard_inline2)
    if call.data == "playlist":
        await call.message.answer("Playlist", reply_markup=keyboard_inline1)
    await call.answer()

executor.start_polling(dp)