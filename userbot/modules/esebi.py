#Sahib - Ayxan
#Tg account - @Ayxhangang
# U S Σ R Δ T O R

from telethon import events
import asyncio
from userbot.events import register
from userbot import DTO_VERSION
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.esebi (.*)")
async def so(event):
    if event.fwd_from:
        return
    ani_first_interval = 3
    ani_sec = range(0, 12)
    u_name = event.pattern_match.group(1)
    await event.edit(f"{u_name} -a Nə demisiniz?")
    ani_first = [
            f"{u_name}  Əsəbləri uje korlanır👿...",
            f"{u_name} artığ Dəliyə dönürrr😡....",
            f"{u_name}  Əsəblərinin Sakitləşməsi üçün Gözləyin",
            f"{u_name} üçün sakitləşdirmə aktiv edildi... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            f"{u_name} üçün sakitləşdirmə aktiv edildi...%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            f"{u_name} üçün sakitləşdirmə aktiv edildi... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",    
            f"{u_name} üçün sakitləşdirmə aktiv edildi... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            f"{u_name} üçün sakitləşdirmə aktiv edildi... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            f"{u_name} üçün sakitləşdirmə aktiv edildi... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
            f"{u_name} üçün sakitləşdirmə aktiv edildi... 84%\n█████████████████████▒▒▒▒ ",
            f"{u_name} Artıq demək olar sakitləşib... 100%\n█████████Həyata qayıdır███████████ ",
            f"{u_name} Tamamı ilə Sakitləşdi\n\nOnu Birdaha Əsəbləşdirməyin🤬🤬🤬\n Beyni çöndüsə daha mən kömək ola bilməyəcəmm🤭...`"
        ]
    for j in ani_sec:
        await asyncio.sleep(ani_first_interval)
        await event.edit(ani_first[j % 12])

Help = CmdHelp('esebi')
Help.add_command('esebi', '<ad>', 'Əsəbləşdiyini göstər')
Help.add_info(
  '**@Ayxhangang tərəfindən yaradılıb.**'
).add()
