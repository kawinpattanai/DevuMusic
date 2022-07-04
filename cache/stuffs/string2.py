from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text="Updates", url="https://t.me/SILENT_BOTS"),
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Owner", url=f"https://t.me/{OWNER_USERNAME}"
        ),
        InlineKeyboardButton(text="Source✨", callback_data="repo_k"),
    ],
    [
        InlineKeyboardButton(text="Help & Commands!", callback_data="help_"),
    ],
]



button2 = [
    [
        InlineKeyboardButton(text="Basic!", callback_data="basic_"),
        InlineKeyboardButton(text="Advance!", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="Close", callback_data="close_"),
        InlineKeyboardButton(text="Back", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="Source", url="https://github.com/ItsmeHyper13/DevuMusic"),
        InlineKeyboardButton(text="Back", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="Close", callback_data="close_"),
        InlineKeyboardButton(text="Back", callback_data="help_"),
    ],
]





