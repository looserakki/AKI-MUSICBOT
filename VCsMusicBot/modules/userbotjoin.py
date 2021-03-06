from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from VCsMusicBot.helpers.decorators import authorized_users_only, errors
from VCsMusicBot.services.callsmusic.callsmusic import client as USER
from VCsMusicBot.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ššš š¦š šš¬ ššš¦š¢š§ šØš š²šØš« š š«šØš®š© šš¢š«š¬š­</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "MusicBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>š šš„šØšØš ššš¢š­ šš«š«šØš« š \n šš¬šš«  {user.first_name} ššØš®š„šš§'š­ š£šØš¢š§ š²šØš®š« š š«šØš®š© šš®š š­šØ š”šššÆš² š£šØš¢š§ š«ššŖš®šš¬š­š¬ ššØš« š®š¬šš«ššØš­! ššš¤š š¬š®š«š š®š¬šš« š¢š¬ š§šØš­ ššš§š§šš š¢š§ š š«šØš®š©."
            "\n\nšš« š¦šš§š®šš„š„š² ššš @AKKI_ASSISTANT š­šØ š²šØš®š« šš«šØš®š© šš§š š­š«š² šš šš¢š§ </b>",
        )
        return
    await message.reply_text(
        "<b>ššš„š©šš« šš¬šš«ššØš­ ššØš¢š§šš ššØš®š« šš”šš­</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>šš¬šš« ššØš®š„šš§'š­ š„šššÆš š²šØš®š« š š«šØš®š©! ššš² šš šš„šØšØšš°šš¢š­š¬."
            "\n\nšš« š¦šš§š®šš„š„š² š¤š¢šš¤ š¦š šš«šØš¦ š­šØ š²šØš®š« šš«šØš®š©</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("šš¬ šš”šš­ ššÆšš§ š„š¢š§š¤šš")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ššš š¦š šš¬ ššš¦š¢š§ šØš š²šØš« šš”šš§š§šš„ šš¢š«š¬š­</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "AKKI_ASSISTANT"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>š”šš„š©šš« šš„š«šššš² š¢š§ š²šØš®š« šš”šš§š§šš„</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>š šš„šØšØš ššš¢š­ šš«š«šØš« š \n šš¬šš«  {user.first_name} ššØš®š„šš§'š­ š£šØš¢š§ š²šØš®š« š š«šØš®š© šš®š š­šØ š”šššÆš² š£šØš¢š§ š«ššŖš®šš¬š­š¬ ššØš« š®š¬šš«ššØš­! ššš¤š š¬š®š«š š®š¬šš« š¢š¬ š§šØš­ ššš§š§šš š¢š§ š š«šØš®š©."
            "\n\nšš« š¦šš§š®šš„š„š² ššš @AKKI_ASSISTANT š­šØ š²šØš®š« šš«šØš®š© šš§š š­š«š² šš šš¢š§ </b>",
        )
        return
    await message.reply_text(
        "<b>š”šš„š©šš« š®š¬šš«ššØš­ š£šØš¢š§šš š²šØš®š« šš”šš§š§šš„</b>",
    )
    
