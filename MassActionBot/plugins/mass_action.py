import asyncio
from MassActionBot import app,SUDOES
from pyrogram import filters,enums
from MassActionBot.utils.chat_status import handle_status
from MassActionBot.plugins.cancel_process import SPAM_CHATS
from pyrogram.errors import FloodWait 

@app.on_message(filters.command(["banall","unbanall"]))
@handle_status
async def _banUnban(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    SPAM_CHATS.append(chat_id)
    if message.command[0] == "banall":
        async for members in _.get_chat_members(chat_id):
            if chat_id not in SPAM_CHATS:
                break            
            if user_id in SUDOES:
                pass
            try:
                await _.ban_chat_member(chat_id,members.user.id)
                await _.send_message(chat_id,f"ʙᴀɴɴᴇᴅ {members.user.mention} ɪɴ `{message.chat.title}`.") 
            except FloodWait as ok:
                await asyncio.sleep(ok.value) 
    if message.command[0] == "unbanall":
        banned_users = []
        x = 0
        async for m in pgram.get_chat_members(chat_id,filter=enums.ChatMembersFilter.BANNED):
            banned_users.append(m.user.id)
            if chat_id not in SPAM_CHATS:
                break       
            try:               
                await pgram.unban_chat_member(chat_id,banned_users[x])
                await _.send_message(chat_id,f"ᴜɴʙᴀɴɪɴɢ ᴀʟʟ ᴍᴄ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {m.user.mention}")
                x += 1                                                                
            except FloodWait as e:
                await asyncio.sleep(e.value)           
     #   end = get_readable_time((time.time() - start))      
                
