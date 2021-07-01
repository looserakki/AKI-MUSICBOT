import logging
from VCsMusicBot.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from VCsMusicBot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
    def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️𝐏𝐔𝐒𝐇 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏⚙️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "𝐒𝐔𝐏𝐏𝐎𝐑𝐓🏷️", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "𝐔𝐏𝐃𝐀𝐓𝐄🗞️", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "𝐌𝐔𝐒𝐈𝐂 𝐖𝐎𝐑𝐋𝐃🌍", url=f"https://{SOURCE_CODE}")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command(["start","start@ERAGANGMUSICBOT"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**𝐌𝐔𝐒𝐈𝐂𝐀𝐋 𝐄𝐑𝐀 𝐎𝐍 𝐅𝐈𝐑𝐄 🔥.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐔𝐏𝐏𝐎𝐑𝐓🏷️", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "𝐘𝐓 𝐒𝐄𝐀𝐑𝐂𝐇🔍", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐥𝐨𝐬𝐞🆑", callback_data="close"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '𝐍𝐄𝐗𝐓', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("⚙️𝐏𝐔𝐒𝐇 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏⚙️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '𝐒𝐔𝐏𝐏𝐎𝐑𝐓🏷️', url=f"https://t.me/{SUPPORT_GROUP}"),
             InlineKeyboardButton(text = '𝐔𝐏𝐃𝐀𝐓𝐄🗞️', url=f"https://t.me/{UPDATES_CHANNEL}")],
            [InlineKeyboardButton(text = '𝐌𝐔𝐒𝐈𝐂 𝐖𝐎𝐑𝐋𝐃🌍', url=f"https://t.me/frndsXworld")],
            [InlineKeyboardButton(text = '𝐁𝐀𝐂𝐊', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️𝐁𝐀𝐂𝐊', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '𝐍𝐄𝐗𝐓▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command(["help","help@ERAGANGMUSICBOT"]) & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**𝐇𝐞𝐥𝐥𝐨 𝐭𝐡𝐞𝐫𝐞🎸...
𝐀𝐦 𝐬𝐩𝐞𝐜𝐢𝐚𝐥𝐥𝐲 𝐦𝐚𝐝𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞𝐜𝐡𝐚𝐭.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐍𝐄𝐄𝐃 𝐇𝐄𝐋𝐏🌂", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )

