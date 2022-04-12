# @umudmmmdov1 DTÖUserBot

"""Emoji

Available Commands:

yo$"""

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^muah$")

async def oof(e):
    t = "mua"
    for j in range(10):
        t = t[:-1] + "aaa"
        await e.edit(t + "h")
        
