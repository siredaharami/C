

import os

from Eaglebot import eagle

from ..core.managers import eod, eor
from ..helpers import reply_id
from ..helpers.utils import _eagleutils
from . import make_gif

menu_category = "utils"


@eagle.eagle_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", menu_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9> <reply to  ani sticker/mp4.",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    eagleinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    eagleid = await reply_id(event)
    event = await eor(event, "```Wait A Minute Its Collaging😁```")
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    eaglesticker = await reply.download_media(file="./temp/")
    if not eaglesticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(eaglesticker)
        await event.edit("`Media format is not supported...`")
        return
    if eagleinput:
        if not eagleinput.isdigit():
            os.remove(eaglesticker)
            await event.edit("`You input is invalid, check help`")
            return
        eagleinput = int(eagleinput)
        if not 0 < eagleinput < 10:
            os.remove(eaglesticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        eagleinput = 3
    if eaglesticker.endswith(".tgs"):
        hmm = await make_gif(event, eaglesticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(eaglesticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = eaglesticker
    endfile = "./temp/collage.png"
    eaglecmd = f"vcsi -g {eagleinput}x{eagleinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _eagleutils.runcmd(eaglecmd))[:2]
    if not os.path.exists(endfile):
        for files in (eaglesticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await eod(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=eagleid,
    )
    await event.delete()
    for files in (eaglesticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
