#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DforDarkAngel
# @DX_Botz

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton ,CallbackQuery
import os, shutil
from config import Config
from telegraph import upload_file
import logging
from translation import Translation

@Client.on_message(filters.command("start"))
async def start(bot, update):
    buttons = [[
        InlineKeyboardButton('⚙️ Help', callback_data='help_btn'),
        InlineKeyboardButton('Support Group 📌', url='https://t.me/NET_HACKER_BOTs_chat')
        ],[
        InlineKeyboardButton('youtube channel 🌟', url='https://www.youtube.com/channel/UCD-g7g3-tfvKECxXKqySq7g'),
        InlineKeyboardButton('Close 🔐', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id
    )
    
@Client.on_message(filters.command(["help"]))
async def help_user(bot, update):
    #logger.info(update)
    buttons = [[
        InlineKeyboardButton('📌 Support Group', url='https://t.me/NET_HACKER_BOTs_chat'),
        InlineKeyboardButton('Update Channel 📜', url='https://t.me/NET_HACKER_BOTs')
        ],[
        InlineKeyboardButton('♻️Share', url=''),
        InlineKeyboardButton('Close 🔐', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        reply_to_message_id=update.message_id,
        parse_mode="html")
        
@Client.on_message(filters.command(["about"]))
async def get_me_info(bot, update):
    #logger.info(update)
    buttons = [[
        InlineKeyboardButton('Channel ⚡', url='https://t.me/Network_hacker_bots'),
        InlineKeyboardButton('Close 🔐', callback_data='cancel_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
