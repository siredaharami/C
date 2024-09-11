import sys

import Eaglebot
from Eaglebot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import eagle
from .start import killer
from .utils import (
    add_bot_to_logger_group,
    hekp,
    install_externalrepo,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("ᴇᴀɢʟᴇ ᴜsᴇʀʙᴏᴛ")

print(Eaglebot.__copyright__)
print("𝐿𝑖𝑐𝑒𝑛𝑠𝑒𝑑 𝑈𝑛𝑑𝑒𝑟 𝑇ℎ𝑒 𝑇𝑒𝑟𝑚𝑠 𝑂𝑓 𝑇ℎ𝑒 " + Eaglebot.__license__)

cmdhr = Config.HANDLER


try:
    LOGS.info("𝑆𝑡𝑟𝑎𝑖𝑛𝑔 𝐸𝑎𝑔𝑙𝑒 𝑈𝑠𝑒𝑟𝑏𝑜𝑡")
    eagle.loop.run_until_complete(setup_bot())
    LOGS.info("𝑇𝑔 𝐵𝑜𝑡 𝑆𝑒𝑡𝑢𝑝 𝐶𝑜𝑚𝑝𝑙𝑒𝑡𝑒𝑑")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()
async def startup_process():
    try:
        await verifyLoggerGroup()
        await load_plugins("plugins")
        await load_plugins("assistant")
        await killer()
        LOGS.info(
        "============================================================================"
    )
        LOGS.info("||               ʏᴀʏ ʏᴏᴜʀ ᴜꜱᴇʀʙᴏᴛ ɪꜱ ᴏꜰꜰɪᴄɪᴀʟʟʏ ᴡᴏʀᴋɪɴɢ.!!!"
    )
        LOGS.info(
        f"||   ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ, ɴᴏᴡ ᴛʏᴘᴇ {cmdhr}ᴀʟɪᴠᴇ ᴛᴏ ꜱᴇᴇ ᴍᴇꜱꜱᴀɢᴇ ɪꜰ ᴇᴀɢʟᴇ ɪꜱ ʟɪᴠᴇ"
    )
        LOGS.info("||   ɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ, ʜᴇᴀᴅ ᴛᴏ https://t.me/PBX_CHAT")
        LOGS.info(
        "============================================================================"
    )
        await verifyLoggerGroup()
        await add_bot_to_logger_group(BOTLOG_CHATID)
        if PM_LOGGER_GROUP_ID != -100:
            await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
        await startupmessage()
        await hekp()
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


eagle.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    eagle.disconnect()
else:
    try:
        eagle.run_until_disconnected()
    except ConnectionError:
        pass
        
