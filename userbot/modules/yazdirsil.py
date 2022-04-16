import random
from telethon import events
from userbot.events import register
from userbot.cmdhelp import CmdHelp
@register(outgoing=True, pattern="^.yazinn ?(.*)")
async def _(event):
    arzu = event.pattern_match.group(1)
    faiz = random.randint(0, 100)
    if not arzu:
       await event.edit("` nə yazdırım qaqa :)`")
    if arzu:
       await event.edit(f"**icra olundu!**")
       
Help = CmdHelp('arzu')
Help.add_command('arzu', '<arzunuz>', 'Arzunuzun reallaşmaq ehtimalını öyrənin', 'arzu Universitetə qəbul olmaq')
Help.add_info('@UseratorOT `üçün hazırlanıb`').add()
