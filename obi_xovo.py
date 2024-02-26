import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types , F 
from aiogram.types import Message , FSInputFile
from aiogram.filters import Command
from aiogram.enums import ParseMode
from bs4 import BeautifulSoup as BS

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import and_f
logging.basicConfig(level=logging.INFO)
import time

bot = Bot(token="6962226645:AAHmGWZlfEQ7wd9_8y3XuiAGHVI_rSGOyKA")
dp = Dispatcher()




@dp.message(Command("start"))
async def rasmy(message: types.Message):
    
    kb = [
        
        [types.KeyboardButton(text="🌦 Ob - Havo")],
        [types.KeyboardButton(text="🕌 Ramazon Taqvimi")],
        
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        
    )
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)



t = requests.get('https://sinoptik.ua/погода-Ургенч')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]
    print(t_min, t_max)

@dp.message(F.text.lower() == "urganch")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELjeZl256qhmpsubqNBXQ10P2HDcE9rQAChQIAAvTrGURAMLYI2z7wbTQE")
    await message.reply(f"⛅️ Bugun Urganchda Ob Havo \n\n 🌝 Kunduzi  {t_max} \n 🌚Kechqurun {t_min} \n\n 💫 Boʻlishi kutilmoqda ")

t = requests.get('https://sinoptik.ua/погода-андижан')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min1 = el.select('.temperature .min')[0].text
    max1 = el.select('.temperature .max')[0].text
    t_min1 = min1[4:]
    t_max1 = max1[5:]
@dp.message(F.text.lower() == "andijon")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Andijonda Ob Havo \n\n 🌝 Kunduzi  {t_max1} \n 🌚Kechqurun {t_min1} \n\n 💫 Boʻlishi kutilmoqda ")


@dp.message(F.text.lower() == "🌦 ob - havo")
async def with_puree(message: types.Message):
    
    knopka = [
            [
                types.KeyboardButton(text="Urganch"),
        ],
        [
                types.KeyboardButton(text="Andijon"),
                types.KeyboardButton(text="Buxoro"),
                types.KeyboardButton(text="Farg'ona"),
        ],
        [
                types.KeyboardButton(text="Guliston"),
                types.KeyboardButton(text="Jizzax"),
                types.KeyboardButton(text="Namangan"),
        ],
         [
                types.KeyboardButton(text="Navoiy"),
                types.KeyboardButton(text="Qarshi"),
                types.KeyboardButton(text="Samarqand"),
        ],
         [
                types.KeyboardButton(text="Temiz"),
                types.KeyboardButton(text="Toshkent"),
                types.KeyboardButton(text="Zarafshon"),
        ]
        ]


    keyboard = types.ReplyKeyboardMarkup(
        keyboard=knopka,
        resize_keyboard=True,

    )
    await message.answer(f"<b>{message.from_user.full_name}</b> \n hududni tanlang",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)


 # [types.InlineKeyboardButton(text="silka", url="https://t.me/j_dev")]

menyu = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="1",callback_data = "bir"),
        types.InlineKeyboardButton(text="2",callback_data = "ikki"),
        types.InlineKeyboardButton(text="3",callback_data = "uch"),
        types.InlineKeyboardButton(text="4",callback_data = "tort"),
        types.InlineKeyboardButton(text="5",callback_data = "besh")],
        
        [types.InlineKeyboardButton(text="6",callback_data = "olti"),
        types.InlineKeyboardButton(text="7",callback_data = "yetti"),
        types.InlineKeyboardButton(text="8",callback_data = "sakkiz"),
        types.InlineKeyboardButton(text="9",callback_data = "toqqiz"),
        types.InlineKeyboardButton(text="10",callback_data = "on")],
         
        [types.InlineKeyboardButton(text="11",callback_data = "onbir"),
        types.InlineKeyboardButton(text="12",callback_data = "onikki"),
        types.InlineKeyboardButton(text="13",callback_data = "onuch"),
        types.InlineKeyboardButton(text="14",callback_data = "ontort"),
        types.InlineKeyboardButton(text="15",callback_data = "onbesh")],

        [types.InlineKeyboardButton(text="16",callback_data = "onolti"),
        types.InlineKeyboardButton(text="17",callback_data = "onyetti"),
        types.InlineKeyboardButton(text="18",callback_data = "onsakkiz"),
        types.InlineKeyboardButton(text="19",callback_data = "ontoqqiz"),
        types.InlineKeyboardButton(text="20",callback_data = "yigirma")],
        
        [types.InlineKeyboardButton(text="21",callback_data = "yigirmabir"),
        types.InlineKeyboardButton(text="22",callback_data = "yigirmaikki"),
        types.InlineKeyboardButton(text="23",callback_data = "yigirmauch"),
        types.InlineKeyboardButton(text="24",callback_data = "yigirmatort"),
        types.InlineKeyboardButton(text="25",callback_data = "yigirmabesh")],

        
        [types.InlineKeyboardButton(text="26",callback_data = "yigirmaolti"),
        types.InlineKeyboardButton(text="27",callback_data = "yigirmayetti"),
        types.InlineKeyboardButton(text="28",callback_data = "yigirmasakkiz"),
        types.InlineKeyboardButton(text="29",callback_data = "yigirmatoqqiz"),
        types.InlineKeyboardButton(text="30",callback_data = "yigirmatoqqiz")]
    ]
        
)



@dp.message(Command("ok"))
async def cmd_random(message: types.Message):
    

    await message.answer(
        "111",
        reply_markup=menyu
    )

@dp.callback_query(F.data == "bir")
async def send_random_value(callback: types.CallbackQuery):
    
    await callback.answer(
        text=f"pogoda{t_max} c",
        show_alert=True
    )

@dp.message(F.text=="salom", F.chat.type == "supergroup")
async def get_guruh(message: types.Message):
    await message.answer(f"{message.chat.title}\n{message.chat.type}\n{message.chat.id}",reply_markup=menyu)
    
    

@dp.message(and_f(F.chat.type == 'supergroup', F.new_chat_members))
async def get_new_chat(message: types.Message):
    for new_chat in message.new_chat_members:
        await message.answer(f"Assalomu alaykum shepim {new_chat.full_name} 🫡")
        await message.delete()



@dp.message(and_f(F.chat.type == 'supergroup', F.left_chat_member ))
async def get_left_chat(message: types.Message):
    await message.answer(f" 🥹xayr shepim {message.left_chat_member.full_name}")
    
    await message.delete()

@dp.message(F.chat.type == 'supergroup', and_f(F.text == "🪓yozma💀", F.reply_to_message))
async def get_banned_chat(message: types.Message): 
   user_id = message.reply_to_message.from_user.id
   permsions = types.ChatPermissions(can_send_messages=False)
   await message.chat.restrict(user_id, permsions)
   await message.reply(f"shepim yozish huquqidan ayrildi😢 {message.reply_to_message.from_user.full_name}")
 


@dp.message(F.chat.type == 'supergroup',and_f(F.text == "yozavar yaxshi🥱", F.reply_to_message))
async def get_not_ban_chat(message: types.Message):
   user_id = message.reply_to_message.from_user.id
   permsions = types.ChatPermissions(can_send_messages=True)
   await message.chat.restrict(user_id, permsions)
   await message.reply(f"Shepim  {message.reply_to_message.from_user.full_name}\n endi yoza oladi🥳🥳🥳")

@dp.message(F.chat.type == "supergroup",and_f(F.text == "yoqall💩", F.reply_to_message))
async def get_bann_chat(message: types.Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.ban_sender_chat(user_id)
   await message.reply(f"nega shepimni grdan chiqardingiz 🥺")



@dp.message(F.chat.type == "supergroup",and_f(F.text == "yoz", F.reply_to_message))
async def get_unbann_chat(message: types.Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.unban_sender_chat(user_id)
   await message.reply(f"Siz endi guruhga qo'shila olasiz\n 🆗 {message.reply_to_message.from_user.full_name}")

from aiogram import types




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())