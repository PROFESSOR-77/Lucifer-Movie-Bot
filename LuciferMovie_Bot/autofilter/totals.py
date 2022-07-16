import logging
from pyrogram import Client as LuciferMovie_Bot, filters as Worker
from LuciferMovie_Bot.database.autofilter_db import Media
from config import ADMINS
logger = logging.getLogger(__name__)

@LuciferMovie_Bot.on_message(Worker.command('total') & Worker.user(ADMINS))
async def total(bot, message):

    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Total Files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')
