from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AddyX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""Tap Here To Dm Bot Owner""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sexy Coder", url=f"https://t.me/SexyCoder")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""Tap Here To Dm Bot Owner """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sexy Coder", url=f"https://t.me/SexyCoder")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("mukku")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/40f6128e4820b94264870.jpg",
        caption=f"""🦋•────────────────•🦋 \n          Fun All Time 
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

Life Is Very Important [ Chat With Me] Push Up ...

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "AD", url=f"https://t.me/Bio_Ad")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("kittu")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/40f6128e4820b94264870.jpg",
        caption=f"""🦋•────────────────•🦋 \n          Fun All Time 
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

Life Is Very Important [ Chat With Me] Push Up ...

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "AD", url=f"https://t.me/Bio_AD")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
        caption=f"""Chatting Group """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Link", url=f"https://t.me/Unknown2Friends")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
        caption=f"""Chatting Group""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Link", url=f"https://t.me/Unknown2Friends")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5cb5424eef2c11b5bbc9b.jpg",
        caption=f"""Chatting Group""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Link", url=f"https://t.me/Unknown2Friends")
                ]
            ]
        ),
    )

