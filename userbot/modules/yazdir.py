import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests
import datetime

from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    BOTLOG,
    BOTLOG_CHATID
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp
import asyncio
from telethon import events
from userbot import BRAIN_CHECKER, WHITELIST
from userbot.events import register

@register(incoming=True, from_users=BRAIN_CHECKER, pattern="^.gg$")
@register(incoming=True, from_users=WHITELIST, pattern="^.gg$")
async def _(q):
    variable = q.pattern_match.group(1)
    await q.client.send_message(q.chat_id, variable)
