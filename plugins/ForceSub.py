import asyncio
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

update_channel = UPDATES_CHANNEL
if update_channel:      
    try:
        user = await bot.get_chat_member(UPDATE_CHANNEL, msg.chat.id)
        if user.status == "kicked":
           await bot.send_message(
               chat_id=msg.chat.id,
               text="**Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/NET_HACKER_BOTs_chat).**",
               parse_mode="markdown",
               disable_web_page_preview=True
           )
           return
    except UserNotParticipant:
        await bot.send_message(
            chat_id=msg.chat.id,
            text="**Please Join My Updates Channel To Use Me!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{UPDATE_CHANNEL}")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return
    except Exception:
        await bot.send_message(
            chat_id=msg.chat.id,
            text="**Something Went Wrong. Contact My [Support Group](https://t.me/NET_HACKER_BOTs_chat).**",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
