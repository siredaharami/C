from telethon import Button

from Eaglebot import Config, eagle, eagleversion

from ..core.logger import logging
from ..helpers import reply_id
from ..plugins import mention
from ..sql_helper.bot_blacklists import check_is_black_list
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


PM_IMG = "https://telegra.ph/file/56557dc496d3032450455.jpg"
pm_caption = f"⚜『♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆』 ɪs ᴏɴʟɪɴᴇ⚜ \n\n"
pm_caption += f"♡_🫧𝆺꯭𝅥˶‌‌֟፝★𝑂ᴡ𝑁𝑒𝑟⁂★🍷┼❤️༆ 『{mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣♡_🫧𝆺꯭𝅥˶‌‌֟፝★𝑇𝑒𝐋𝒆𝐓𝐻𝑜𝑛𝑒⁂★🍷┼❤️༆ `1.15.0` \n"
pm_caption += f"┣『♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆』~ `{eagleversion}` \n"
pm_caption += f"┣♡_🫧𝆺꯭𝅥˶‌‌֟፝★𝐶𝒉𝑎𝑁𝐧𝑬𝐿⁂★🍷┼❤️༆ ~ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/HEROKUBIN_01)\n"
pm_caption += f"┣**♡_🫧𝆺꯭𝅥˶‌‌֟፝★𝐿𝑖𝑐𝐧𝐒𝒆⁂★🍷┼❤️༆** ~ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](github.com/Badhacker98/EAGLEBOT/blob/Bad/LICENSE)\n"
pm_caption += f"┣♡_🫧𝆺꯭𝅥˶‌‌֟፝★𝐶𝒐𝑝𝑦𝒓𝐼𝒈ℎ𝑇⁂★🍷┼❤️༆ ~ ʙʏ  [『♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆』 ](https://t.me/PBX_CHAT)\n"
pm_caption += f"┣Assistant ~ By [⏤͟͟͞͞‌ٖ🥀➣Bᴀᴅ❤︎ ᴍᴜɴᴅᴀ ➻ >•⏤͟͟͞͞‌ٖٖ](https://t.me/ll_BAD_MUNDA_ll)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『♡_🫧𝆺꯭𝅥˶‌‌֟፝★Ｅ𝓪𝘨ļ૯⁂★🍷┼❤️༆』](https://t.me/PBX_CHAT) «««"


@eagle.bot_cmd(
    pattern=f"^/alive({botusername})?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    chat = await event.get_chat()
    await eagle.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    buttons = [
        (Button.url("🚬 ʀᴇᴘᴏ 🌸", "https://github.com/Badhacker98/EAGLEBOT/fork"),),
    ]
    try:
        await event.client.send_file(
            chat.id,
            PM_IMG,
            caption=pm_caption,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Error**\nThere was a error while using **alive**. `{e}`",
            )
