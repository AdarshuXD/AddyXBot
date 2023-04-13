from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ Add Me Babe ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Settings️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ Add Me Babe ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Owner", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Support", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="Upadate", url=f"https://t.me/AddyUpdate",
            )
        ],
        [
            InlineKeyboardButton(
                text="Network",
                url=f"https://t.me/U2FNetwork",
            )
        ],
     ]
    return buttons
