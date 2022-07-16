import asyncio 

from pyrogram import Client as LuciferMovie_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid

from LuciferMovie_Bot.admins.index_files import index_files_to_db
from LuciferMovie_Bot.database.autofilter_db import get_file_details
from LuciferMovie_Bot.database._utils import get_size, is_subscribed
from LuciferMovie_Bot.database._utils import lucifer_temp

from translation import LuciferMovie
from config import BUTTONS, FORCES_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS, team_name, team_link

from LuciferMovie_Bot.modules._text_ import module

lock = asyncio.Lock()

@LuciferMovie_Bot.on_callback_query()
async def cb_handler(client: LuciferMovie_Bot, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id

    if (clicked == typed):

# # ---------- 🔘 [ | 𝗚𝗥𝗢𝗨𝗣 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- # #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 Check Bot PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 Check Bot PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 Check Bot PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="🤖 Check Bot PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# # ---------- 🔘 [ | 𝗕𝗢𝗧 𝗣𝗠 𝗙𝗜𝗟𝗧𝗘𝗥𝗦 | ] 🔘 ---------- # #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again 🙏",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("🔙 Back Page", callback_data=f"backbot_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page ➡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"{int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("🗑️", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- 📁 [ | 𝗚𝗘𝗧 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data.startswith("LuciferMovie_Bot"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)
          
            try:
                if FORCES_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=caption
                        )
                    await query.answer('Check Bot PM, I have Sent Your Files In PM 📩',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- 📁 [ | 𝗣𝗠 𝗙𝗜𝗟𝗘𝗦 | ] 📁 ---------- #

        elif query.data.startswith("pmfile"):
            if FORCES_SUB and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                
                caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

                buttons = [[
                  InlineKeyboardButton('🔗 Movies Club', url='https://t.me/NewMoviesClub2022')
                  ]]                 
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- 📁 [ | 𝗠𝗢𝗗𝗨𝗟𝗘𝗦 | ] 📁 ---------- #


        elif query.data == "start":
            if query.from_user.id not in ADMINS: 
                buttons = [[
                 InlineKeyboardButton("🔗 Movie Club", url=f"https://t.me/+ZLfYBUbS-adiY2E1")
                 ],[
                 InlineKeyboardButton("ℹ️ Help", callback_data="help"),
                 InlineKeyboardButton("😎 About", callback_data="about") 
                 ],[
                 InlineKeyboardButton("🎭 Who Am I", callback_data="who")
                 ]]
            else:
                buttons = [[
                 InlineKeyboardButton("🔗 Movie Club", url=f"https://t.me/+ZLfYBUbS-adiY2E1")
                 ],[
                 InlineKeyboardButton("ℹ️ Help", callback_data="bot_owner"),
                 InlineKeyboardButton("😎 About", callback_data="about") 
                 ],[
                 InlineKeyboardButton("🎭 Who Am I", callback_data="who") 
                 ]]
            await query.message.edit(text=START_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
          
        elif query.data == "help":
            buttons = [[
              InlineKeyboardButton("🏠 Home", callback_data="start"),
              InlineKeyboardButton("About 😎", callback_data="about")
              ]]               
            await query.message.edit(text=LuciferMovie.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "about":
            buttons = [[
             InlineKeyboardButton("🏠 Home", callback_data="start"),
             InlineKeyboardButton("Close 🗑️", callback_data="close")
             ]]               
            await query.message.edit(text=LuciferMovie.PROFESSOR-77.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "close":
            await query.message.delete()
        
        elif query.data == "who":
            buttons = [[ 
             InlineKeyboardButton("🏠 Home", callback_data="start"),       
             InlineKeyboardButton("Close 🗑️", callback_data="close")
             ]]
            await query.message.edit(text=LuciferMovie.WHO_AM_I.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
        
        elif query.data == "close":
            await query.message.delete()
        
        elif query.data == "donate":
            buttons = [[ 
             InlineKeyboardButton("🏠 Home", callback_data="start"),       
             InlineKeyboardButton("Close 🗑️", callback_data="close")
             ]]
            await query.message.edit(text=LuciferMovie.DONATE.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
        
        elif query.data == "close":
            await query.message.delete()

        elif query.data == "bot_owner":
            buttons = [[
             InlineKeyboardButton('🏠 Home', callback_data="start"),
             InlineKeyboardButton('About 😎', callback_data="about")
             ]]               
            await query.message.edit(text=LuciferMovie.PROFESSOR_77.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)


        elif query.data == "autofilter":
            buttons = [[ InlineKeyboardButton('🔙 Back', callback_data="help") ]]          
            await query.message.edit(module.autofilter_text.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "ban":
            buttons = [[ InlineKeyboardButton('🔙 Back', callback_data="help") ]]          
            await query.message.edit(module.ban_text.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "mute":
            buttons = [[ InlineKeyboardButton('🔙 Back', callback_data="help") ]]          
            await query.message.edit(module.mute_text.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "pin":
            buttons = [[ InlineKeyboardButton('🔙 Back', callback_data="help") ]]          
            await query.message.edit(module.pin_message.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "close":
            await query.message.delete()

# ---------- ⚠️ [ | Other | ] ⚠️ ---------- #

        elif query.data.startswith("index"):
            bot = client 
            if query.data.startswith('index_cancel'):
                lucifer_temp.CANCEL = True
                return await query.answer("Cancelling Indexing")
            _, raju, chat, lst_msg_id, from_user = query.data.split("#")
            if raju == 'reject':
                await query.message.delete()
                await client.send_message(int(from_user),
                                       f'Your Submission for indexing {chat} has been decliened by our moderators.',
                                       reply_to_message_id=int(lst_msg_id))
                return

  
            if lock.locked():
                return await query.answer('🗣️ Wait until previous process complete ✔️', show_alert=True)
            msg = query.message
            await query.answer('Uploading...⏳', show_alert=True)
            if int(from_user) not in ADMINS:
                await bot.send_message(int(from_user),
                                       f'Your Submission for indexing {chat} has been accepted by our moderators and will be added soon.',
                                       reply_to_message_id=int(lst_msg_id))
            await msg.edit(
                "Starting Indexing",
                reply_markup=InlineKeyboardMarkup(
                  [[InlineKeyboardButton('✗ Cancel', callback_data='index_cancel')]]
                  )
            )
            try:
                chat = int(chat)
            except:
                chat = chat
            await index_files_to_db(int(lst_msg_id), chat, msg, bot)




        elif query.data == "pages":
            await query.answer("@LuciferMovie_Bot")


    else:
        await query.answer("This Is Not Your Message 🤗",show_alert=True)




