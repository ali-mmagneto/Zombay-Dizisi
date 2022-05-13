import json
import math

import requests
from pyrogram.handlers import MessageHandler
import re
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
ADMIN: str = environ.get('ADMIN', None)
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

app = Client("zombi_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, parse_mode="markdown")

@app.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    update_channel = AUTH_CHANNEL
    if update_channel:
        try:
            link = await client.create_chat_invite_link(int(AUTH_CHANNEL), member_limit = 1)
            user = await client.get_chat_member(update_channel, message.from_user.id)
            if user.status == ChatMemberStatus.Banned:
               await client.delete_messages(
                 chat_id=message.from_user.id,
                 message_ids=message.from_message_id,
                 revoke=True
               )
               return
        except UserNotParticipant:
            await client.reply_text(
                text="**Zombi Dizisini İzlemek için Kanalıma katılman gerek!**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="Kanala Katil", url=link.invite_link)]
                ])
            )
            return

        buttons = [
                 [
                     InlineKeyboardButton('Bot Destek', url=f"https://t.me/ADMIN")
                 ]
                 ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_photo(
                 chat_id=message.from_user.id,
                 photo=random.choice(PICS),
                 caption="Selam bu botu çalıştırdıysan bazı şeyleri biliyor olmalısın eğer bilmiyorsan /help komutundan yardım iste.\n\n **BİR ÖLÜR BİN DİRİLİRİZ!**",
                 reply_markup=reply_markup,
                 parse_mode='html',
                 protect_content=True
        )

@app.on_message(filters.command('help'))
async def help(client: Client, message: Message):
    butt = [
                 [
                     InlineKeyboardButton('Bot Destek', url=f"https://t.me/ADMIN")
                 ]
                 ]
    reply_mrkp = InlineKeyboardMarkup(butt)
    await client.send_message(
        chat_id=message.from_user.id,
        text="eğer bu botu bulduysan ne işe yaradığını da biliyorsun /sezon1, /sezon2 diye devam et anlarsın zor değil.",
        reply_markup=reply_mrkp
    ) 

app.run()



