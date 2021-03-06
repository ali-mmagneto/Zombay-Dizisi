import json
import math

import requests
from pyrogram.handlers import MessageHandler
import re
from pyrogram.enums import ParseMode, ChatType, MessageMediaType
import asyncio
import random
from pyrogram.types import ChatMemberUpdated
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
from pyrogram.enums import ChatMemberStatus 
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

def is_enabled(value:str):
    return bool(str(value).lower() in ["true", "1", "e", "d"])

BOT_TOKEN: str = environ.get('BOT_TOKEN', None)
API_ID: int = int(environ.get('API_ID', None))
API_HASH: str = environ.get('API_HASH', None)
SUDO = list(set(int(x) for x in environ.get("SUDO", "1276627253").split()))
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', "-1001157048481"))
BOLUMKANALI = int(environ.get('BOLUMKANALI', "-1001159848481"))
BOLUMONAYLAMA = int(environ.get('BOLUMONAYLAMA', "-1001159848481"))
HEROKU_APP_NAME = environ.get('HEROKU_APP_NAME', None)
HEROKU_API_KEY = environ.get('HEROKU_API_KEY', None)
YOU_JOINED = is_enabled(environ.get("YOU_JOINED", True))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1001157048481"))
ADMIN: str = environ.get('ADMIN', None)

app = Client("zombi_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, parse_mode="markdown")

@app.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    try:
        forcsub = await client.create_chat_invite_link(AUTH_CHANNEL, creates_join_request=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return
    try:
        user = await client.get_chat_member(AUTH_CHANNEL, message.from_user.id)
        if user.status == ChatMemberStatus.BANNED:
            await client.delete_messages(
                chat_id=message.from_user.id,
                revoke=True,
                parse_mode=ParseMode.HTML
            )
            return
    except UserNotParticipant:
        await client.send_message(
            chat_id=message.from_user.id,
            text="Merhaba bu botu sadece gruba ??ye olanlar kullanabilir e??er gruba ??ye olmak istiyorsan a??a????daki butondan istek g??nder e??er fake isim koyarsan yada profil foto??raf??n?? yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanal??m", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    buttons = [
             [
                 InlineKeyboardButton('Bot Destek', url=f"https://t.me/{ADMIN}")
             ]
             ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
             text="Merhaba teliften dolay?? art??k b??l??m kanal??n?? ??cretli yapt??k bilgi almak i??in /help komutunu kullan!.\n\nB??R ??L??R B??N D??R??L??R??Z!\nBotu Yazan: @mmagneto",
             reply_markup=reply_markup,
             chat_id=message.from_user.id,
             protect_content=True,
             parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('log'))
async def sendLogs(client, message):
    with open('log.txt', 'rb') as f:
        try:
            await client.send_document(document=f,
                                       file_name=f.name, reply_to_message_id=message.message_id,
                                       chat_id=message.chat.id, caption=f.name)
        except Exception as e:
            await message.reply_text(str(e))

@app.on_message(filters.command("restart") & filters.user(SUDO))
async def restart(_, m: Message):
    restart_message = await m.reply_text(text="`??lmek ??zereyim...\nbana hayat verdi??in i??in te??ekk??rler????`")
    try:
        if HEROKU_API_KEY is not None:
            heroku_conn = heroku3.from_key(HEROKU_API_KEY)
            server = heroku_conn.app(HEROKU_APP_NAME)
            server.restart() 
            await restart_message.edit('`Senin ellerinde can verdim kurt bak????l??m.`')
            time.sleep(2)
        else:
            await restart_message.edit("`Heroku Api Key ve uygulama ad??n?? ekleyin.`")
    except Exception as e:
        await restart_message.edit(f"**??ntihar bile edemedim:** `{e}`")

@app.on_message(filters.command('help'))
async def help(client: Client, message: Message):
    try:
        forcsub = await client.create_chat_invite_link(AUTH_CHANNEL, creates_join_request=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return
    try:
        user = await client.get_chat_member(AUTH_CHANNEL, message.from_user.id)
        if user.status == ChatMemberStatus.BANNED:
            await client.delete_messages(
                chat_id=message.from_user.id,
                revoke=True,
                parse_mode=ParseMode.HTML
            )
            return
    except UserNotParticipant:
        await client.send_message(
            chat_id=message.from_user.id,
            text="Merhaba bu botu sadece gruba ??ye olanlar kullanabilir e??er gruba ??ye olmak istiyorsan a??a????daki butondan istek g??nder e??er fake isim koyarsan yada profil foto??raf??n?? yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanal??m", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML
        )
        return
    butt = [
          [
              InlineKeyboardButton('Bot Destek', url=f"https://t.me/{ADMIN}")
          ]
          ]
    reply_mrkp = InlineKeyboardMarkup(butt)
    await client.send_message(
        text="Merhaba bu botu sadece onayl?? ??yeler kullanabilir onayl?? ??ye olmak i??in bana mesaj at:\n@Alifirat001\n\nNot: Onayl?? ??ye olmak i??in ??cret 1TL idir.",
        reply_markup=reply_mrkp,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    )
    return

@app.on_message(filters.command('kanal'))
async def sezon1(client: Client, message: Message):
    try:
        forcsub = await client.create_chat_invite_link(AUTH_CHANNEL, creates_join_request=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return
    try:
        user = await client.get_chat_member(BOLUMONAYLAMA, message.from_user.id)
        if user.status == ChatMemberStatus.BANNED:
            await client.delete_messages(
                chat_id=message.from_user.id,
                revoke=True,
                parse_mode=ParseMode.HTML
            )
            return
    except UserNotParticipant:
        destek = [
              [
                  InlineKeyboardButton('Bot Destek', url=f"https://t.me/{ADMIN}")
              ]
              ]
        reply_markup = InlineKeyboardMarkup(destek)
        await client.send_message(
            chat_id=message.from_user.id,
            text="Paray?? Veren D??d?????? ??alar e??er diziyi izlemek istiyorsan a??a????daki buton arac??l??????yla sahibimle ileti??ime ge??. (??cret: 1 T??rk Liras??)", 
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML
        ) 
        return
    kanal= await client.create_chat_invite_link(int(BOLUMKANALI), member_limit = 1)
    kanalbtn = InlineKeyboardMarkup([[InlineKeyboardButton('B??l??mler', url=kanal.invite_link)]])

    await client.send_message(
        text="Diziyi izlemek i??in a??a????daki butona t??kla!",
        reply_markup=kanalbtn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n {message.from_user.firstname} Ki??isi 1. Sezon linkini ald??.",
        reply_markup=kanalbtn,
        parse_mode=ParseMode.HTML
    )
    
@app.on_chat_member_updated(filters.chat(AUTH_CHANNEL))
async def user_accepted(bot:Client, cmu: ChatMemberUpdated):
    if not cmu.new_chat_member: return
    if cmu.new_chat_member.user.is_bot: return
    yeni = cmu.new_chat_member.user
    if YOU_JOINED:
        await bot.send_message(
            chat_id=yeni.id,
            text="Kanala kat??ld??n. ??imdi beni kullanabilirsin.", 
            parse_mode=ParseMode.HTML
        ) 
        await asyncio.sleep(1)
        await bot.send_message(
            chat_id=SUDO,
            text=(str(e)),
            parse_mode=ParseMode.HTML
        ) 

app.run()
