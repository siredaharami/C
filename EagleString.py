import os
import base64
import ipaddress
import random
import struct
from random import randint

try:
    from pyrogram import Client as PClient
except:
    os.system("pip install pyrogram")
    from pyrogram import Client as PClient

try:
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient
except:
    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient


def main():
    print("ᴛᴇᴀᴍ ᴘʙxʙᴏᴛ   ! !")
    print("ʜᴇʟʟᴏ!! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ\n")
    print("ʜᴜᴍᴀɴ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʀᴇQᴜɪʀᴇᴅ !!")
    while True:
        verify = int(randint(1, 50))
        okvai = int(input(f"Enter {verify} to continue: "))
        if okvai == verify:
            print("\nᴄʜᴏᴏꜱᴇ ᴛʜᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ᴛʏᴘᴇ: \n1. ᴛᴇʟᴇᴛʜᴏɴ \n2. ᴘʏʀᴏɢʀᴀᴍ ")
            while True:
                library = input("\nYour Choice: ")
                if library == "1":
                    generate_telethon_session()
                    break
                elif library == "3":
                    generate_pyro_session()
                    break
                else:
                    print("Please enter integer values (1/2 only).")
            break
        else:
            print("Verification Failed! Try Again:")


def generate_pyro_session():
    print("Pyrogram Session for Music Bot!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with PClient(name="Pbxuser", api_id=APP_ID, api_hash=API_HASH, in_memory=True) as Pbxbot:
        print("\nYour PBXBot Session Is sent in your Telegram Saved Messages.")
        Pbxbot.send_message(
            "me",
            f"#PBXBOT #PYROGRAM\n\n`{Pbxbot.export_session_string()}`",
        )


def generate_telethon_session():
    print("\nTelethon Session For Pbxbot!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as Pbxbot:
        print("\nYour PbxBot Session Is sent in your Telegram Saved Messages.")
        Hell.send_message(
            "me",
            f"#PBXBOT #TELETHON \n\n`{Pbxbot.session.save()}`",
        )




def challenge_code(username, choice):
    while True:
        otp = input("Enter the OTP sent to your Email: ")
        if otp.isdigit():
            break
        else:
            print("Enter digits only!")
    return otp


def Pbxbot(text):
    res = ''.join(
        map(
            random.choice,
            zip(text.lower(), text.upper()),
        )
    )
    return res.strip()


def Pbxbot_session(session):
    pyro_format = {
        351: ">B?256sI?",
        356: ">B?256sQ?",
        362: ">BI?256sQ?",
    }

    ipv4_dc = {
        1: "149.154.175.53",
        2: "149.154.167.51",
        3: "149.154.175.100",
        4: "149.154.167.91",
        5: "91.108.56.130",
    }

    error_msg = "Error in generating session! Report it in Pbx Chats"

    # converting pyrogram session
    if len(session) in pyro_format.keys():
        if len(session) in [351, 356]:
            dc_id, _, auth_key, _, _ = struct.unpack(
                pyro_format[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )
        else:
            dc_id, _, _, auth_key, _, _ = struct.unpack(
                pyro_format[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )

       
        new_session = CURRENT_VERSION + StringSession.encode(
            struct.pack(
                _STRUCT_PREFORMAT.format(4),
                dc_id,
                ipaddress.ip_address(ipv4_dc[dc_id]).packed,
                443,
                auth_key
            )
        )
        return f"=={Pbxbot('Pbx')}{new_session}{Pbxbot('bot')}=="
    else:
        return error_msg


main()
    
