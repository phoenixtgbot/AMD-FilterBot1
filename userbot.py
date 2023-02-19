from info import *
from pyrogram import Client, idle

User = Client(session_name="userbot",
              session_string=DEL_SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )

hmf = User()
hmf.run()

idle()
