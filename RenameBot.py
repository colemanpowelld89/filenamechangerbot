from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

import os

BOT_TOKEN = "1274502397:AAESdcI4ApmHQTnpBxHJvXrHH26R-kqWVYE"
API_ID = 1579671 #Should be an interger i.e without "
API_HASH = "56719ea0e35d2d895d1301424aa4a51d"

app = Client ("rename_bot",
                         bot_token=BOT_TOKEN,
                         api_id=API_ID,
                         api_hash=API_HASH)


@app.on_message(filters.command("start"))
async def start(client, message):
        name = message.from_user['first_name']
        user_id = message.from_user['id']
        text = f"Hey [{name}](tg://user?id={user_id}), I can help you rename a file right inside Telegram. Send me a file you want to rename and then reply `/rename NewFileName` to rename it."
        await message.reply(text)
        
        
async def user_in_chat(user_id, chat_id=-1001245607422):
    try:
        await app.get_chat_member(chat_id, user_id)
        status = True
    except:
        status = False
    return status
    
    
@app.on_message(filters.command("rename"))
async def rename(client, message):
	     if not await user_in_chat(user_id=message.from_user['id']):
	         keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Channel", url="https://t.me/samhelperproaf")]])
	         await app.send_message(chat_id=message.chat.id, text="You must be a member of the Channel to use this bot", reply_markup=keyboard)
	         return
	     reply_message = message.reply_to_message
	     if not reply_message:
	         await message.reply("Reply to the file with /remame FileName.")
	         return
	     msg = message.text
	     original_file_name = reply_message.document["file_name"]
	     file_extension = original_file_name.split(".")[1]
	     try:
	         new_file_name = msg.split(" ", 1)[1]
	     except:
	         await message.reply("Format: `/rename NewFileName`")
	         return
	         
	     await app.download_media(message=reply_message, file_name=f"{new_file_name}.{file_extension}")
	     
	     await app.send_document(chat_id=message.chat.id, document=f"downloads/{new_file_name}.{file_extension}", caption="Thanks for using this bot ... made by @samhelper")
	     os.remove(f"downloads/{new_file_name}.{file_extension}")                                                 


print("BOT RUNNING")
app.run()