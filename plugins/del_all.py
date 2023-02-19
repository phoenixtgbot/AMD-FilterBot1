# This Model Added By @ThiruXD

import asyncio
from info import *
from bot import User
from pyrogram import Client, filters, idle

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(DEL_TIME)
          await Client.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
