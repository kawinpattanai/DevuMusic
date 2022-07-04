# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚


import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command("rmf") & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    if ls_dir := os.listdir(downloads):
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("`🗑️ʀᴇᴍᴏᴠᴇᴅ ᴀʟʟ ғɪʟᴇs ғʀᴏᴍ ᴅᴏᴡɴʟᴏᴀᴅ`")
    else:
        await message.reply_text("`sʜʜ, ɴᴛɢ ɪs ғᴏᴜɴᴅ ᴛᴏ ᴄʟᴇᴀɴ🙄`")

        
@Client.on_message(command("rmw") & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    if ls_dir := os.listdir(raw_files):
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("`ᴄʟᴇᴀɴɪɴɢ sɪʟᴇɴᴛ ᴅʙ🗑️`")
    else:
        await message.reply_text("`ᴀʟʀᴇᴀᴅʏ ᴄʟᴇᴀɴᴇᴅ🙋‍♀️`")


@Client.on_message(command(["dclean"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    if ls_dir := os.listdir(pth):
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("`🧚‍♀️ʜᴜʜ ᴄʟᴇᴀɴᴇᴅ`")
    else:
        await message.reply_text("`💬ғɪɴᴇ, ᴀʟʟ ᴏᴋ ᴀʟʀᴇᴀᴅʏ`")
