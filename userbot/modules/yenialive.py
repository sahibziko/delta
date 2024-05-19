# ApexUserbot
"""Sadece .pinstall"""

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern=".yalive")

async def merkurkedissa(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 12)

    await event.edit("𝙰 𝙿 Σ 𝚇 ✨ - Aktivdir!")

    animation_chars = [
        
            "𝙰 𝙿 Σ 𝚇 ✨ - Он активен!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Es ist aktiv!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Il est actif!",
            "𝙰 𝙿 Σ 𝚇 ✨ - アクティブです!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Aktiftir!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Ini aktif!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Je aktivní!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Dit is aktief!",
            "𝙰 𝙿 Σ 𝚇 ✨ - Den er aktiv!",
            "𝙰 𝙿 Σ 𝚇 ✨ - esta activo!",
            "𝙰 𝙿 Σ 𝚇 ✨ - It is active!",
            "✨ 𝙰   𝙿   Σ   𝚇 ✨"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
