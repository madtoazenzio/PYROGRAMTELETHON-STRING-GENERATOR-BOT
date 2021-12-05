from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}
ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ, 
1) sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ
sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !
ʙʏ @Z_Bots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs ✨", url="https://t.me/Z_Bots")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ❔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ ᴍᴏʀᴇ ᴀᴍᴀᴢɪɴɢ ʙᴏᴛs ♥", url="https://t.me/Z_Bots")],
    ]

    # Help Message
    HELP = """
✨ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ✨
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ʀᴇsᴛᴀʀᴛ ʙᴏᴛ
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 
ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @Z_Bots
⭕ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/madtoazenzio/PYROGRAMTELETHON-STRING-GENERATOR-BOT)
⭕ ꜰʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](http://docs.pyrogram.org)
⭕ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](http://www.python.org)
⭕ ᴅᴇᴠᴇʟᴏᴘᴇʀ : @Z_Bots
    """
