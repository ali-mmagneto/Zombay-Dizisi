import json
import math

import requests
from pyrogram.handlers import MessageHandler
import re
from pyrogram.enums import ParseMode, ChatType, MessageMediaType
import asyncio
import random
from pyrogram import Client
from random import choice
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Chat, Message, User
import threading
from pyrogram.types.messages_and_media.message import Message
import logging, heroku3
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from os import environ
from pyrogram import filters, Client
from pyrogram.types import Message
broadcast_ids = {}

import random, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
import aiohttp
import pytz
from dotenv import load_dotenv
from pyrogram import types
from pyrogram.errors import UserNotParticipant

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

BOT_TOKEN: str = environ.get('BOT_TOKEN', None)
API_ID: int = int(environ.get('API_ID', None))
API_HASH: str = environ.get('API_HASH', None)
SUDO = list(set(int(x) for x in environ.get("SUDO", "1276627253").split()))
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', "-1001157048481"))
SEZON1 = int(environ.get('SEZON1', "-1001157048481"))
SEZON2 = int(environ.get('SEZON2', "-1001157048481"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1001157048481"))
ADMIN: str = environ.get('ADMIN', None)

app = Client("zombi_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, parse_mode="markdown")

@app.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    buttons = [
             [
                 InlineKeyboardButton('Bot Destek', url=f"https://t.me/{ADMIN}")
             ]
             ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
             text="Selam bu botu çalıştırdıysan bazı şeyleri biliyor olmalısın eğer bilmiyorsan /help komutundan yardım iste.\n\n **BİR ÖLÜR BİN DİRİLİRİZ!**",
             reply_markup=reply_markup,
             chat_id=message.from_user.id,
             protect_content=True,
             parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('help'))
async def help(client: Client, message: Message):
    butt = [
          [
              InlineKeyboardButton('Bot Destek', url=f"https://t.me/{ADMIN}")
          ]
          ]
    reply_mrkp = InlineKeyboardMarkup(butt)
    await client.send_message(
        text="eğer bu botu bulduysan ne işe yaradığını da biliyorsun /sezon1, /sezon2 diye devam et anlarsın zor değil.",
        reply_markup=reply_mrkp,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon2'))
async def sezon2(client: Client, message: Message):
    sezon2 = await client.create_chat_invite_link(int(SEZON2), member_limit = 1)
    sezon2btn = InlineKeyboardMarkup([[InlineKeyboardButton('2. Sezon', url=sezon2.invite_link)]])

    await client.send_message(
        text="2. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon2btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 2. Sezon linkini aldı.",
        reply_markup=sezon2btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon3'))
async def sezon1(client: Client, message: Message):
    sezon3 = await client.create_chat_invite_link(int(SEZON3), member_limit = 1)
    sezon3btn = InlineKeyboardMarkup([[InlineKeyboardButton('3. Sezon', url=sezon3.invite_link)]])
    szn3yn = message.from_user

    await client.send_message(
        text="3. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 3. Sezon linkini aldı.",
        reply_markup=sezon3btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon4'))
async def sezon1(client: Client, message: Message):
    sezon4 = await client.create_chat_invite_link(int(SEZON4), member_limit = 1)
    sezon4btn = InlineKeyboardMarkup([[InlineKeyboardButton('4. Sezon', url=sezon4.invite_link)]])
    szn4yn = message.from_user

    await client.send_message(
        text="4. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon4btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 4. Sezon linkini aldı.",
        reply_markup=sezon4btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon5'))
async def sezon1(client: Client, message: Message):
    sezon5 = await client.create_chat_invite_link(int(SEZON5), member_limit = 1)
    sezon5btn = InlineKeyboardMarkup([[InlineKeyboardButton('5. Sezon', url=sezon5.invite_link)]])
    szn5yn = message.from_user

    await client.send_message(
        text="5. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon5btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
    sezon1 = await client.create_chat_invite_link(int(SEZON1), member_limit = 1)
    sezon1btn = InlineKeyboardMarkup([[InlineKeyboardButton('1. Sezon', url=sezon1.invite_link)]])
    szn1yn = message.from_user

    await client.send_message(
        text="1. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon1btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

app.run()



