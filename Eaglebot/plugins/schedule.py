from asyncio import sleep

from Eaglebot import eagle

menu_category = "utils"


@eagle.eagle_cmd(
    pattern="schd (\d*) ([\s\S]*)",
    command=("schd", menu_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    eagle = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = eagle[1]
    ttl = int(eagle[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
