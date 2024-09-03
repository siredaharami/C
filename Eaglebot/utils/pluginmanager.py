import importlib
import sys
from pathlib import Path

from Eaglebot import CMD_HELP, LOAD_PLUG

from ..Config import Config
from ..core import LOADED_CMDS, PLG_INFO
from ..core.logger import logging
from ..core.managers import eod, eor
from ..core.session import eagle
from ..helpers.tools import media_type
from ..helpers.utils import _format, _eagletools, _eagleutils, install_pip, reply_id
from .decorators import admin_cmd, sudo_cmd

LOGS = logging.getLogger("EagleUserBot")


def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"Eaglebot/plugins/{shortname}.py")
        checkplugins(path)
        name = "Eaglebot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:
        if plugin_path is None:
            path = Path(f"Eaglebot/plugins/{shortname}.py")
            name = f"Eaglebot.plugins.{shortname}"
        else:
            path = Path((f"{plugin_path}/{shortname}.py"))
            name = f"{plugin_path}/{shortname}".replace("/", ".")
        checkplugins(path)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = eagle
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = eagle.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._eagleutils = _eagleutils
        mod._eagletools = _eagletools
        mod.media_type = media_type
        mod.eod = eod
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.eor = eor
        mod.logger = logging.getLogger(shortname)
        mod.borg = eagle
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["Eaglebot.plugins." + shortname] = mod
        LOGS.info("EagleBot " + shortname)


def remove_plugin(shortname):
    try:
        cmd = []
        if shortname in PLG_INFO:
            cmd += PLG_INFO[shortname]
        else:
            cmd = [shortname]
        for cmdname in cmd:
            if cmdname in LOADED_CMDS:
                for i in LOADED_CMDS[cmdname]:
                    eagle.remove_event_handler(i)
                del LOADED_CMDS[cmdname]
        return True
    except Exception as e:
        LOGS.error(e)
    try:
        for i in LOAD_PLUG[shortname]:
            eagle.remove_event_handler(i)
        del LOAD_PLUG[shortname]
    except BaseException:
        pass
    try:
        name = f"Eaglebot.plugins.{shortname}"
        for i in reversed(range(len(eagle._event_builders))):
            ev, cb = eagle._event_builders[i]
            if cb.__module__ == name:
                del eagle._event_builders[i]
    except BaseException:
        raise ValueError


def checkplugins(filename):
    with open(filename, "r") as f:
        filedata = f.read()
    filedata = filedata.replace("sendmessage", "send_message")
    filedata = filedata.replace("sendfile", "send_file")
    filedata = filedata.replace("editmessage", "edit_message")
    with open(filename, "w") as f:
        f.write(filedata)
