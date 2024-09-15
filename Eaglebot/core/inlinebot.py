import json
import math
import os
import random
import re
import time
from uuid import uuid4

from telethon import Button, custom, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from youtubesearchpython import VideosSearch

from ..Config import Config
from ..core.session import legend
from ..helpers.functions import rand_key
from ..helpers.functions.utube import (
    download_button,
    get_yt_video_id,
    get_ytthumb,
    result_formatter,
    ytsearch_data,
)
from ..plugins import ALIVE_NAME, USERID, Legend_grp, mention
from ..sql_helper.globals import gvarstatus
from . import CMD_INFO, GRP_INFO, PLG_INFO, check_owner
from .logger import logging

LOGS = logging.getLogger(__name__)

MEDIA_PATH_REGEX = re.compile(r"(:?\<\bmedia:(:?(?:.*?)+)\>)")
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
tr = Config.HANDLER


def get_thumb(name=None, url=None):
    if url is None:
        url = f"https://github.com/siredaharami/C/tree/Bad/Eaglebot/helpers/resources/pics/{name}?raw=true"
    return types.InputWebDocument(
        url=url, size=0, mime_type="image/jpeg", attributes=[]
    )


def main_menu():
    text = f" ᴇᴀɢʟᴇ ᴜsᴇʀʙᴏᴛ\
        \n𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗯𝘆 {mention}"
    buttons = [
        (Button.inline("ℹ️ Info", data="check"),),
        (
            Button.inline(f"👮‍♂️ Admin ({len(GRP_INFO['admin'])})", data="admin_menu"),
            Button.inline(f"🤖 Bot ({len(GRP_INFO['bot'])})", data="bot_menu"),
        ),
        (
            Button.inline(f"🎨 Fun ({len(GRP_INFO['fun'])})", data="fun_menu"),
            Button.inline(f"🧩 Misc ({len(GRP_INFO['misc'])})", data="misc_menu"),
        ),
        (
            Button.inline(f"🧰 Tools ({len(GRP_INFO['tools'])})", data="tools_menu"),
            Button.inline(f"🗂 Utils ({len(GRP_INFO['utils'])})", data="utils_menu"),
        ),
        (
            Button.inline(f"➕ Extra ({len(GRP_INFO['extra'])})", data="extra_menu"),
            Button.inline("🔒 Close Menu", data="close"),
        ),
    ]
    if Config.BADCAT:
        switch_button = [
            (
                Button.inline(f"➕ Extra ({len(GRP_INFO['extra'])})", data="extra_menu"),
                Button.inline(
                    f"⚰️ Useless ({len(GRP_INFO['useless'])})", data="useless_menu"
                ),
            ),
            (Button.inline("🔒 Close Menu", data="close"),),
        ]
        buttons = buttons[:-1] + switch_button

    return text, buttons


def main_menu():
    tol = gvarstatus("BOT_USERNAME")
    text = f"⚜ {mention}  ⚜"
    buttons = [
        [custom.Button.inline("👨‍💻 Info 👨‍💻", data="check")],
        [
            custom.Button.inline("🔰 Plugins 🔰", data="help_k_minu"),
            Button.url("✨ Assistant ✨", f"https://t.me/{tol}"),
        ],
        [
            custom.Button.inline("⚜ Alive ⚜", data="stats"),
            Button.url("Support 🇮🇳", "https://t.me/LegendBot_AI"),
        ],
        [custom.Button.inline("❌", data="clise")],
    ]
    return text, buttons

async def build_article(
    event,
    media=None,
    title=None,
    text=None,
    description=None,
    buttons=None,
    thumbnail=None,
    parse_mode="md",
    link_preview=False,
):
    builder = event.builder
    photo_document = None
    if media:
        if not media.endswith((".jpg", ".jpeg", ".png")):
            # Return a document object with the provided media URL
            return builder.document(
                media,
                title=title,
                description=description,
                text=text,
                buttons=buttons,
            )
        # Create an InputWebDocument object for the media file
        photo_document = get_thumb(url=media)
    if thumbnail and isinstance(thumbnail, str):
        thumbnail = get_thumb(url=thumbnail)
    # Return an article object with the provided properties
    return builder.article(
        title=title,
        description=description,
        type="photo" if photo_document else "article",
        file=media,
        thumb=thumbnail or photo_document,
        content=photo_document,
        text=text,
        buttons=buttons,
        link_preview=link_preview,
        parse_mode=parse_mode,
    )


async def help_article(event):
    help_info = main_menu()
    return await build_article(
        event,
        title="Help Menu",
        description="Help menu for Eaglebot.",
        thumbnail=get_thumb("help.png"),
        text=help_info[0],
        buttons=help_info[1],
    )


async def age_verification_article(event):
    buttons = [
        Button.inline(text="Yes I'm 18+", data="age_verification_true"),
        Button.inline(text="No I'm Not", data="age_verification_false"),
    ]
    return await build_article(
        event,
        title="Age verification",
        text="**ARE YOU OLD ENOUGH FOR THIS ?**",
        buttons=buttons,
        media="https://i.imgur.com/Zg58iXc.jpg",
    )



def command_in_category(cname):
    cmds = 0
    for i in GRP_INFO[cname]:
        for _ in PLG_INFO[i]:
            cmds += 1
    return cmds


def paginate_help(
    page_number,
    loaded_plugins,
    prefix,
    plugins=True,
    category_plugins=None,
    category_pgno=0,
):  # sourcery no-metrics  # sourcery skip: low-code-quality
    try:
        number_of_rows = int(gvarstatus("NO_OF_ROWS_IN_HELP") or 5)
    except (ValueError, TypeError):
        number_of_rows = 5
    try:
        number_of_cols = int(gvarstatus("NO_OF_COLUMNS_IN_HELP") or 2)
    except (ValueError, TypeError):
        number_of_cols = 2
    HELP_EMOJI = gvarstatus("HELP_EMOJI") or " "
    helpable_plugins = [p for p in loaded_plugins if not p.startswith("_")]
    helpable_plugins = sorted(helpable_plugins)
    if len(HELP_EMOJI) == 2:
        if plugins:
            modules = [
                Button.inline(
                    f"{HELP_EMOJI[0]} {x} {HELP_EMOJI[1]}",
                    data=f"{x}_prev(1)_command_{prefix}_{page_number}",
                )
                for x in helpable_plugins
            ]
        else:
            modules = [
                Button.inline(
                    f"{HELP_EMOJI[0]} {x} {HELP_EMOJI[1]}",
                    data=f"{x}_cmdhelp_{prefix}_{page_number}_{category_plugins}_{category_pgno}",
                )
                for x in helpable_plugins
            ]
    elif plugins:
        modules = [
            Button.inline(
                f"{HELP_EMOJI} {x} {HELP_EMOJI}",
                data=f"{x}_prev(1)_command_{prefix}_{page_number}",
            )
            for x in helpable_plugins
        ]
    else:
        modules = [
            Button.inline(
                f"{HELP_EMOJI} {x} {HELP_EMOJI}",
                data=f"{x}_cmdhelp_{prefix}_{page_number}_{category_plugins}_{category_pgno}",
            )
            for x in helpable_plugins
        ]
    if number_of_cols == 1:
        pairs = list(zip(modules[::number_of_cols]))
    elif number_of_cols == 2:
        pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    else:
        pairs = list(
            zip(
                modules[::number_of_cols],
                modules[1::number_of_cols],
                modules[2::number_of_cols],
            )
        )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    elif len(modules) % number_of_cols == 2:
        pairs.append((modules[-2], modules[-1]))
    max_num_pages = math.ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if plugins:
        if len(pairs) > number_of_rows:
            pairs = pairs[
                modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
            ] + [
                (
                    Button.inline("⌫", data=f"{prefix}_prev({modulo_page})_plugin"),
                    Button.inline("⚙️ Main Menu", data="mainmenu"),
                    Button.inline("⌦", data=f"{prefix}_next({modulo_page})_plugin"),
                )
            ]
        else:
            pairs = pairs + [(Button.inline("⚙️ Main Menu", data="mainmenu"),)]
    elif len(pairs) > number_of_rows:
        if category_pgno < 0:
            category_pgno = len(pairs) + category_pgno
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                Button.inline(
                    "⌫",
                    data=f"{prefix}_prev({modulo_page})_command_{category_plugins}_{category_pgno}",
                ),
                Button.inline(
                    "⬅️ Back ",
                    data=f"back_plugin_{category_plugins}_{category_pgno}",
                ),
                Button.inline(
                    "⌦",
                    data=f"{prefix}_next({modulo_page})_command_{category_plugins}_{category_pgno}",
                ),
            )
        ]
    else:
        if category_pgno < 0:
            category_pgno = len(pairs) + category_pgno
        pairs = pairs + [
            (
                Button.inline(
                    "⬅️ Back ",
                    data=f"back_plugin_{category_plugins}_{category_pgno}",
                ),
            )
        ]
    return pairs
    

@eagle.tgbot.on(CallbackQuery(data=re.compile(b"close")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [
        (Button.inline("Open Menu", data="mainmenu"),),
    ]
    await event.edit("Menu Closed", buttons=buttons)


@eagle.tgbot.on(CallbackQuery(data=re.compile(b"check")))
async def on_plugin_callback_query_handler(event):
    text = f"𝙿𝚕𝚞𝚐𝚒𝚗𝚜: {len(PLG_INFO)}\
        \n𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜: {len(CMD_INFO)}\
        \n\n{tr}𝚑𝚎𝚕𝚙 <𝚙𝚕𝚞𝚐𝚒𝚗> : 𝙵𝚘𝚛 𝚜𝚙𝚎𝚌𝚒𝚏𝚒𝚌 𝚙𝚕𝚞𝚐𝚒𝚗 𝚒𝚗𝚏𝚘.\
        \n{tr}𝚑𝚎𝚕𝚙 -𝚌 <𝚌𝚘𝚖𝚖𝚊𝚗𝚍> : 𝙵𝚘𝚛 𝚊𝚗𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚒𝚗𝚏𝚘.\
        \n{tr}𝚜 <𝚚𝚞𝚎𝚛𝚢> : 𝚃𝚘 𝚜𝚎𝚊𝚛𝚌𝚑 𝚊𝚗𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜.\
        "
    await event.answer(text, cache_time=0, alert=True)


@eagle.tgbot.on(CallbackQuery(data=re.compile(b"(.*)_menu")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    category = str(event.pattern_match.group(1).decode("UTF-8"))
    buttons = paginate_help(0, GRP_INFO[category], category)
    text = f"**Category: **{category}\
        \n**Total plugins :** {len(GRP_INFO[category])}\
        \n**Total Commands:** {command_in_category(category)}"
    await event.edit(text, buttons=buttons)


@eagle.tgbot.on(
    CallbackQuery(
        data=re.compile(b"back_([a-z]+)_([a-z_1-9]+)_([0-9]+)_?([a-z1-9]+)?_?([0-9]+)?")
    )
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    mtype = str(event.pattern_match.group(1).decode("UTF-8"))
    category = str(event.pattern_match.group(2).decode("UTF-8"))
    pgno = int(event.pattern_match.group(3).decode("UTF-8"))
    if mtype == "plugin":
        buttons = paginate_help(pgno, GRP_INFO[category], category)
        text = f"**Category: **`{category}`\
            \n**Total plugins :** __{len(GRP_INFO[category])}__\
            \n**Total Commands:** __{command_in_category(category)}__"
    else:
        category_plugins = str(event.pattern_match.group(4).decode("UTF-8"))
        category_pgno = int(event.pattern_match.group(5).decode("UTF-8"))
        buttons = paginate_help(
            pgno,
            PLG_INFO[category],
            category,
            plugins=False,
            category_plugins=category_plugins,
            category_pgno=category_pgno,
        )
        text = f"**Plugin: **`{category}`\
                \n**Category: **__{getkey(category)}__\
                \n**Total Commands:** __{len(PLG_INFO[category])}__"
    await event.edit(text, buttons=buttons)


@eagle.tgbot.on(CallbackQuery(data=re.compile(rb"mainmenu")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    _result = main_menu()
    await event.edit(_result[0], buttons=_result[1])


@eagle.tgbot.on(
    CallbackQuery(data=re.compile(rb"(.*)_prev\((.+?)\)_([a-z]+)_?([a-z]+)?_?(.*)?"))
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    category = str(event.pattern_match.group(1).decode("UTF-8"))
    current_page_number = int(event.data_match.group(2).decode("UTF-8"))
    htype = str(event.pattern_match.group(3).decode("UTF-8"))
    if htype == "plugin":
        buttons = paginate_help(current_page_number - 1, GRP_INFO[category], category)
    else:
        category_plugins = str(event.pattern_match.group(4).decode("UTF-8"))
        category_pgno = int(event.pattern_match.group(5).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1,
            PLG_INFO[category],
            category,
            plugins=False,
            category_plugins=category_plugins,
            category_pgno=category_pgno,
        )
        text = f"**Plugin: **`{category}`\
                \n**Category: **__{getkey(category)}__\
                \n**Total Commands:** __{len(PLG_INFO[category])}__"
        try:
            return await event.edit(text, buttons=buttons)
        except Exception as e:
            LOGS.error(str(e))
    await event.edit(buttons=buttons)


@eagle.tgbot.on(
    CallbackQuery(data=re.compile(rb"(.*)_next\((.+?)\)_([a-z]+)_?([a-z]+)?_?(.*)?"))
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    category = str(event.pattern_match.group(1).decode("UTF-8"))
    current_page_number = int(event.data_match.group(2).decode("UTF-8"))
    htype = str(event.pattern_match.group(3).decode("UTF-8"))
    category_plugins = event.pattern_match.group(4)
    if category_plugins:
        category_plugins = str(category_plugins.decode("UTF-8"))
    category_pgno = event.pattern_match.group(5)
    if category_pgno:
        category_pgno = int(category_pgno.decode("UTF-8"))
    if htype == "plugin":
        buttons = paginate_help(current_page_number + 1, GRP_INFO[category], category)
    else:
        buttons = paginate_help(
            current_page_number + 1,
            PLG_INFO[category],
            category,
            plugins=False,
            category_plugins=category_plugins,
            category_pgno=category_pgno,
        )
    await event.edit(buttons=buttons)


@eagle.tgbot.on(
    CallbackQuery(
        data=re.compile(b"(.*)_cmdhelp_([a-z_1-9]+)_([0-9]+)_([a-z]+)_([0-9]+)")
    )
)
@check_owner
async def on_plug_in_callback_query_handler(event):
    cmd = str(event.pattern_match.group(1).decode("UTF-8"))
    category = str(event.pattern_match.group(2).decode("UTF-8"))
    pgno = int(event.pattern_match.group(3).decode("UTF-8"))
    category_plugins = str(event.pattern_match.group(4).decode("UTF-8"))
    category_pgno = int(event.pattern_match.group(5).decode("UTF-8"))
    buttons = [
        (
            Button.inline(
                "⬅️ Back ",
                data=f"back_command_{category}_{pgno}_{category_plugins}_{category_pgno}",
            ),
            Button.inline("⚙️ Main Menu", data="mainmenu"),
        )
    ]
    text = f"**Command :** `{tr}{cmd}`\
        \n**Plugin :** `{category}`\
        \n**Category :** `{category_plugins}`\
        \n\n**✘ Intro :**\n{CMD_INFO[cmd][0]}"
    await event.edit(text, buttons=buttons)


async def inline_search(event, query):
    answers = []
    builder = event.builder
    if found := [i for i in sorted(list(CMD_INFO)) if query in i]:
        for cmd in found:
            title = f"Command:  {cmd}"
            plugin = get_key(cmd)
            try:
                info = CMD_INFO[cmd][1]
            except IndexError:
                info = "None"
            description = f"Plugin:  {plugin} \nCategory:  {getkey(plugin)}\n{info}"
            text = await cmdinfo(cmd, event)
            result = builder.article(
                title=title,
                description=description,
                thumb=get_thumb("plugin_cmd.jpg"),
                text=text,
            )
            answers.append(result)

    if found := [i for i in sorted(list(PLG_INFO.keys())) if query in i]:
        for plugin in found:
            count = len(PLG_INFO[plugin])
            if count > 1:
                title = f"Plugin:  {plugin}"
                text = await plugininfo(plugin, event, "-p")
                result = builder.article(
                    title=title,
                    description=f"Category:  {getkey(plugin)}\nTotal Cmd: {count}",
                    thumb=get_thumb("plugin.jpg"),
                    text=text,
                )
                answers.append(result)
    return answers
