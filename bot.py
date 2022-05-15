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

BOT_TOKEN: str = environ.get('BOT_TOKEN', None)
API_ID: int = int(environ.get('API_ID', None))
API_HASH: str = environ.get('API_HASH', None)
SUDO = list(set(int(x) for x in environ.get("SUDO", "1276627253").split()))
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', "-1001157048481"))
SEZON1 = int(environ.get('SEZON1', "-1001157048681"))
SEZON2 = int(environ.get('SEZON2', "-1001157948481"))
SEZON3 = int(environ.get('SEZON3', "-1001157748481"))
SEZON4 = int(environ.get('SEZON4', "-1001157048401"))
SEZON5 = int(environ.get('SEZON5', "-1001157048581"))
SEZON6 = int(environ.get('SEZON6', "-1001157048481"))
SEZON7 = int(environ.get('SEZON7', "-1001157848481"))
SEZON8 = int(environ.get('SEZON8', "-1001157328481"))
SEZON9 = int(environ.get('SEZON9', "-1001157046481"))
SEZON10 = int(environ.get('SEZON10', "-1001159048481"))
SEZON11 = int(environ.get('SEZON11', "-1001159848481")) 
ORIGINS = int(environ.get('ORIGINS', "-1001159848481"))
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
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
             text="Selam bu botu çalıştırdıysan bazı şeyleri biliyor olmalısın eğer bilmiyorsan /help komutundan yardım iste.\n\nBİR ÖLÜR BİN DİRİLİRİZ!\nBotu Yazan: @mmagneto",
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

@app.on_message(filters.command("restart"))
async def restart(_, m: Message):
    restart_message = await m.reply_text(text="`Ölmek üzereyim...\nbana hayat verdiğin için teşekkürler😢`")
    try:
        if HEROKU_API_KEY is not None:
            heroku_conn = heroku3.from_key(HEROKU_API_KEY)
            server = heroku_conn.app(HEROKU_APP_NAME)
            server.restart() 
            await restart_message.edit('`Senin ellerinde can verdim kurt bakışlım.`')
            time.sleep(2)
        else:
            await restart_message.edit("`Heroku Api Key ve uygulama adını ekleyin.`")
    except Exception as e:
        await restart_message.edit(f"**İntihar bile edemedim:** `{e}`")

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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
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
        text="eğer bu botu bulduysan ne işe yaradığını da biliyorsun /sezon1, /sezon2 diye devam et anlarsın zor değil.",
        reply_markup=reply_mrkp,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 

@app.on_message(filters.command('sezon1'))
async def sezon1(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
            protect_content=True
        )
        return
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
        text="#yenilink\n {message.from_user.firstname} Kişisi 1. Sezon linkini aldı.",
        reply_markup=sezon1btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon2'))
async def sezon2(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
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
        text="#yenilink\n message.from_user.username Kişisi 2. Sezon linkini aldı.",
        reply_markup=sezon2btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon3'))
async def sezon3(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
            protect_content=True
        )
        return
    sezon3 = await client.create_chat_invite_link(int(SEZON3), member_limit = 1)
    sezon3btn = InlineKeyboardMarkup([[InlineKeyboardButton('3. Sezon', url=sezon3.invite_link)]])
    szn3yn = message.from_user

    await client.send_message(
        text="3. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon3btn,
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
async def sezon4(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
            protect_content=True
        )
        return
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
async def sezon5(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
            protect_content=True
        )
        return
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
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 5. Sezon linkini aldı.",
        reply_markup=sezon5btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon6'))
async def sezon6(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    sezon6 = await client.create_chat_invite_link(int(SEZON6), member_limit = 1)
    sezon6btn = InlineKeyboardMarkup([[InlineKeyboardButton('6. Sezon', url=sezon6.invite_link)]])
    szn6yn = message.from_user

    await client.send_message(
        text="6. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon6btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 6. Sezon linkini aldı.",
        reply_markup=sezon6btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon7'))
async def sezon7(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    sezon7 = await client.create_chat_invite_link(int(SEZON7), member_limit = 1)
    sezon7btn = InlineKeyboardMarkup([[InlineKeyboardButton('7. Sezon', url=sezon7.invite_link)]])
    szn7yn = message.from_user

    await client.send_message(
        text="7. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon7btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 7. Sezon linkini aldı.",
        reply_markup=sezon7btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon8'))
async def sezon8(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    sezon8 = await client.create_chat_invite_link(int(SEZON8), member_limit = 1)
    sezon8btn = InlineKeyboardMarkup([[InlineKeyboardButton('8. Sezon', url=sezon8.invite_link)]])
    szn8yn = message.from_user

    await client.send_message(
        text="8. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon8btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 8. Sezon linkini aldı.",
        reply_markup=sezon8btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon9'))
async def sezon9(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    sezon9 = await client.create_chat_invite_link(int(SEZON9), member_limit = 1)
    sezon9btn = InlineKeyboardMarkup([[InlineKeyboardButton('9. Sezon', url=sezon9.invite_link)]])
    szn9yn = message.from_user

    await client.send_message(
        text="9. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon9btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 9. Sezon linkini aldı.",
        reply_markup=sezon9btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon10'))
async def sezon10(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    sezon10 = await client.create_chat_invite_link(int(SEZON10), member_limit = 1)
    sezon10btn = InlineKeyboardMarkup([[InlineKeyboardButton('10. Sezon', url=sezon10.invite_link)]])
    szn10yn = message.from_user

    await client.send_message(
        text="10. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon10btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id=message.from_user.id Kişisi 10. Sezon linkini aldı.",
        reply_markup=sezon10btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('sezon11'))
async def sezon11(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML, 
            protect_content=True
        )
        return
    sezon11 = await client.create_chat_invite_link(int(SEZON11), member_limit = 1)
    sezon11btn = InlineKeyboardMarkup([[InlineKeyboardButton('11. Sezon', url=sezon11.invite_link)]])
    szn11yn = message.from_user

    await client.send_message(
        text="11. Sezonu izlemek için aşağıdaki butona tıkla!",
        reply_markup=sezon11btn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id={message.from_user.id} Kişisi 11. Sezon linkini aldı.",
        reply_markup=sezon11btn,
        parse_mode=ParseMode.HTML
    )

@app.on_message(filters.command('origins'))
async def origins(client: Client, message: Message):
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
            text="Merhaba bu botu sadece gruba üye olanlar kullanabilir eğer gruba üye olmak istiyorsan aşağıdaki butondan istek gönder eğer fake isim koyarsan yada profil fotoğrafını yoksa seni gruba kabul edemem!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Kanalım", url=forcsub.invite_link)
                    ]
                ]
            ),
            parse_mode=ParseMode.HTML,
            protect_content=True
        )
        return
    origins = await client.create_chat_invite_link(int(ORIGINS), member_limit = 1)
    originsbtn = InlineKeyboardMarkup([[InlineKeyboardButton('Origins', url=origins.invite_link)]])
    origins = message.from_user

    await client.send_message(
        text="Origins izlemek için aşağıdaki butona tıkla!",
        reply_markup=originsbtn,
        chat_id=message.from_user.id,
        protect_content=True,
        parse_mode=ParseMode.HTML
    ) 
    await client.send_message(
        chat_id=LOG_CHANNEL,
        text="#yenilink\n tg://openmessage?user_id={message.from_user.id} Kişisi Origins linkini aldı.",
        reply_markup=originsbtn,
        parse_mode=ParseMode.HTML
    )

@app.on_chat_member_updated(filters.chat(AUTH_CHANNEL))
async def user_accepted(bot:Client, cmu: ChatMemberUpdated):
    if not cmu.new_chat_member: return
    if cmu.new_chat_member.user.is_bot: return
    yeni = cmu.new_chat_member.user
    try:
        if YOU_JOINED:
            await client.send_message(yeni.id, "Kanala katıldın. Şimdi beni kullanabilirsin.")
    except Exception as e:
        await client.send_message(
            chat_id=SUDO,
            text=(str(e)),
            parse_mode=ParseMode.HTML
        ) 

app.run()
