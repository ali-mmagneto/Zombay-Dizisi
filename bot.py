import json
import math

import requests
from messageFunc import sendMessage
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
import re
import asyncio
import random
from pyrogram import Client
from random import choice
from typing import Callable, Coroutine, Dict, List, Union
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Chat, Message, User
import threading
from pyrogram.types.messages_and_media.message import Message
import logging, heroku3
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from os import environ
from typing import Dict, List
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
from unidecode import unidecode

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


BOT_TOKEN: str = environ.get('BOT_TOKEN', None)
API_ID: int = int(environ.get('API_ID', None))
API_HASH: str = environ.get('API_HASH', None)
SUDO = list(set(int(x) for x in os.environ.get("SUDO", "1276627253").split()))
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', "-1001157048481"))
SEZON1 = inr(environ.get('SEZON1', "-1001157048481"))
SEZON2 = inr(environ.get('SEZON2', "-1001157048481"))

@Client.on_message(filters.command('start'):
async def start(client: Client, message: Message):
  if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            date = message.date + 120
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL), expire_date=date, member_limit = 1)
        except ChatAdminRequired:
            logger.error("Bot'un AUTH_CHANNEL kanalında yönetici olduğundan emin olun")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "🤖 Kanala Katılın", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton(" 🔄 Tekrar deneyin", callback_data=f"checksub#{message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**Zombi Dizisi İzlemek için kanalıma katılman gerek!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown",
            protect_content=True
            )
        return
@Client.on_callback_query()
async def button(bot, update):
    İf cb_data == "help":
        await update.message.edit_caption(
            text="Kardeşim /sezon1, /sezon2 diye kullan komutları devamını tahmin etmek zor değil",
            disable_web_page_preview=True
        )
    elif cb_data == "close":
        await update.message.delete()

   buttons = [
            [
                InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            ],
            [
                InlineKeyboardButton('Bot Destek', url=f"https://t.me/ADMIN"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   await client.send_photo(
            chat_id=message.from_user.id,
            photo=random.choice(PICS),
            caption="Selam bu botu çalıştırdıysan bazı şeyleri biliyor olmalısın eğer bilmiyorsan aşağıdaki butondan yardım iste.\n\n **BİR ÖLÜR BİN DİRİLİRİZ!**",
            reply_markup=reply_markup,
            parse_mode='html',
            protect_content=True
   ) 



