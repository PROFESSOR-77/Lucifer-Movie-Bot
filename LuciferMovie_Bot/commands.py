import random 
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as LuciferMovie_Bot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import LuciferMovie 
from LuciferMovie_Bot.database.users_chats_db import db

@LuciferMovie_Bot.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
             InlineKeyboardButton("đ Movie Club", url=f"https://t.me/+ZLfYBUbS-adiY2E1")
             ],[
             InlineKeyboardButton("âšī¸ Help", callback_data="help"),
             InlineKeyboardButton("đ About", callback_data="about") 
             ],[
             InlineKeyboardButton("đ­ Who Am I", callback_data="who")
             ]]
        else:
            buttons = [[
             InlineKeyboardButton("đ Movie Club", url=f"https://t.me/+ZLfYBUbS-adiY2E1")
             ],[
             InlineKeyboardButton("âšī¸ Help", callback_data="bot_owner"),
             InlineKeyboardButton("đ About", callback_data="about") 
             ],[
             InlineKeyboardButton("đ­ Who Am I", callback_data="who")
             ]]
        await message.reply_photo(photo = random.choice(BOT_PICS), caption=START_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/a0740de5f50d6ac1bc3a9.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("đ Movie Club Updates đ", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=random.choice(FORCES),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Subscribed</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get the Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
   
@LuciferMovie_Bot.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    button = [[
     InlineKeyboardButton("đ  Home", callback_data="start"),
     InlineKeyboardButton("About đ", callback_data="about")
     ]]
    await message.reply_photo(
        photo = random.choice(BOT_PICS),
        caption=LuciferMovie.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@LuciferMovie_Bot.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    button = [[
     InlineKeyboardButton("đ  Home", callback_data="start"),
     InlineKeyboardButton("Close đī¸", callback_data="close")
     ],[
     InlineKeyboardButton("đ­ Who Am I", callback_data="who")
     ]]
    await message.reply_photo(
        photo=random.choice(BOT_PICS),
        caption=LuciferMovie.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
