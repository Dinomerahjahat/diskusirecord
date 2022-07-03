# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Rexa

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ ɪɴɪ :\n\n@{client.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴʏɪᴍᴘᴀɴ ᴘᴏsᴛɪɴʜᴀɴ ᴀᴛᴀᴜ ғɪʟᴇ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴅɪᴀᴋsᴇs ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴋʜᴜsᴜs.\n\n 👨‍💼 ᴄʀᴇᴀᴛᴏʀ: @{OWNER}\n 🔗 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: <a href='https://github.com/Rexashh/onebuttonfilesharing'>File-Sharing-Man</a>\n 👨‍💻 ᴏᴡɴᴇʀ ʀᴇᴘᴏ: @JustRex\n\n👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ @tirexgugel</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
