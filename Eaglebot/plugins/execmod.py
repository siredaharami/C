from Eaglebot import eagle
from Eaglebot.core.managers import eod, eor
from Eaglebot.helpers.utils import _eagleutils, parse_pre, yaml_format

menu_category = "tools"


@eagle.eagle_cmd(
    pattern="suicide$",
    command=("suicide", menu_category),
    info={
        "header": "Deletes all the files and folder in the current directory.",
        "usage": "{tr}suicide",
    },
)
async def suicide(event):
    "To delete all files and folders in Eaglebot"
    cmd = "rm -rf .*"
    await _eagleutils.runcmd(cmd)
    OUTPUT = "**SUICIDE BOMB:**\nsuccessfully deleted all folders and files in Eaglebot server"
    event = await eor(event, OUTPUT)


@eagle.eagle_cmd(
    pattern="plugins$",
    command=("plugins", menu_category),
    info={
        "header": "To list all plugins in Eaglebot.",
        "usage": "{tr}plugins",
    },
)
async def plugins(event):
    "To list all plugins in Eaglebot"
    cmd = "ls Eaglebot/plugins"
    o = (await _eagleutils.runcmd(cmd))[0]
    OUTPUT = f"**[eagle's](tg://need_update_for_some_feature/) PLUGINS:**\n{o}"
    await eor(event, OUTPUT)


@eagle.eagle_cmd(
    pattern="env$",
    command=("env", menu_category),
    info={
        "header": "To list all environment values in Eaglebot.",
        "description": "to show all heroku vars/Config values in your Eaglebot",
        "usage": "{tr}env",
    },
)
async def env(event):
    "To show all config values in Eaglebot"
    cmd = "env"
    o = (await _eagleutils.runcmd(cmd))[0]
    OUTPUT = f"**[eagle's](tg://need_update_for_some_feature/) Environment Module:**\n\n\n{o}"
    await eor(event, OUTPUT)


@eagle.eagle_cmd(
    pattern="noformat$",
    command=("noformat", menu_category),
    info={
        "header": "To get replied message without markdown formating.",
        "usage": "{tr}noformat <reply>",
    },
)
async def noformat(event):
    "Replied message without markdown format."
    reply = await event.get_reply_message()
    if not reply or not reply.text:
        return await eod(
            event, "__Reply to text message to get text without markdown formating.__"
        )
    await eor(event, reply.text, parse_mode=parse_pre)


@eagle.eagle_cmd(
    pattern="when$",
    command=("when", menu_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def when(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await eor(event, f"**This message was posted on :** `{yaml_format(result)}`")
