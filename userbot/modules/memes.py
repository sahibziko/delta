# U S Î£ R Î T O R / ÃmÃ¼d


""" Memes """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time
import asyncio

from collections import deque

import requests

from cowpy import cow

from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from userbot.cmdhelp import CmdHelp

# ================= CONSTANT =================
EMOJIS = [
    "ð",
    "ð",
    "ð",
    "â",
    "ð",
    "ð",
    "ð",
    "ð¯",
    "ð¶",
    "ð",
    "ð",
    "ð",
    "ð",
    "ð",
    "ð",
    "ð¥",
    "ð´",
    "ð¦",
    "ð¦",
    "ð",
    "ð",
    "ð©",
    "ð",
    "ðð",
    "ð",
    "ð",
    "ð©",
    "ð°",
]

UWUS = [
    "(ã»`ÏÂ´ã»)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)â â",
    "(Ã´_Ã´)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(â¥_â¥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "Êâ¿Ê",
    "ã¾(-_- )ã",
    "(ã£ËÚ¡ËÏ)",
    "(Â´Ð¶ï½Ï)",
    "( à²  ÊÌ¯ à² )",
    "(Â° ÍÊÍ¡Â°)â­â©â®",
    "(áµàº¶ï¸µ áµàº¶)",
    "(à¸ã)à¸§",
    "Ê(â¢ï½",
    "(ã£âÂ¯â)ã¤",
    "(â ï¹â )",
    "( Í¡à²  ÊÌ¯ Í¡à² )",
    "( à°  ÍÊ à° )",
    "(â©ï½-Â´)âââï¾.*ï½¥ï½¡ï¾",
    "(âï½¡â¢Ìâ¿â¢Ìï½¡)â",
    "(._.)",
    "{â¢Ì_â¢Ì}",
    "(áµá´¥áµ)",
    "â¨_â¨",
    "â¥.â¥",
    "Ø­Ëà¯°Ëã¥ ",
    "(Òâ¡_â¡)",
    "Æª(Ú×²)âÆªââ",
    "(ã£â¢Ìï½¡â¢Ì)âªâ¬",
    "âáµá´¥áµâ âª â« ",
    "(âï¾ã®ï¾)â",
    "[Â¬Âº-Â°]Â¬",
    "(Ô¾â¸ Ô¾)",
    "(â¢Ìá´â¢Ì)Ù ÌÌ",
    "ã¾(Â´ã`)ï¾âªâªâª",
    "(à¸'Ì-'Ì)à¸",
    "á(â¢Ìâ¢Ìá)",
    "Ê â¢ÌØâ¢Ì â",
    "âªâª ã½(ËâË )ã",
    "Ñï¼ï¾Ðï¾Ñï¼",
    "( Ëà·´Ë )",
    "ë_ë",
    "(à¹â¢Ì â â¢Ìà¹) ",
    "( Ë Â³Ë)â¥ ",
    "Ô(ââ¿âÔ)",
    "â¥â¿â¥",
    "â_â",
    "â½â½à¬( ËáµË )à¬â¾â¾",
    "ä¹( â à±ªâ)ã      â(ï¿£Ð ï¿£)â",
    "( à° àµ à°  )ï¾",
    "Ù©(à¹_à¹)Û¶",
    "â(ãã¨ã)Ê",
    "à° _à° ",
    "(ã¥ï½¡ââ¿â¿âï½¡)ã¥",
    "(ãà²  â©à² )ãå½¡( \\oÂ°o)\\",
    "âã½(Â´â½ï½)ãâ",
    "à¼¼ à¼àº¶ à·´ à¼àº¶à¼½",
    "ï½¡ï¾( ï¾à®â¸à®ï¾)ï¾ï½¡",
    "(ã¥ï¿£ Â³ï¿£)ã¥",
    "(â.â)7",
    "á( á )á",
    "t(-_-t)",
    "(à²¥â£à²¥)",
    "ã½à¼¼ à² çà²  à¼½ï¾",
    "à¼¼âµà¼½ à¼¼â¨à¼½ à¼¼â¢à¼½ à¼¼â¤à¼½",
    "ãâï¹âã",
    "(â_â)",
    "Â¿â§_â§ï®",
    "à² _à² ",
    "(Â´ï½¥_ï½¥`)",
    "á¦(Ã²_Ã³Ë)á¤",
    "âï¹â",
    "(â¯Â°â¡Â°ï¼â¯ï¸µ â»ââ»",
    r"Â¯\_(âï¸¿â)_/Â¯",
    "Ù©âÌ¯âÛ¶",
    "Â°â¿â¿Â°",
    "á(ââ¸â¼â¶)á",
    "â(ââ¿â)ã¤",
    "Vâ¢á´¥â¢V",
    "q(ââ¿â)p",
    "à²¥_à²¥",
    "à¸^â¢ï»â¢^à¸",
    "à²¥ï¹à²¥",
    "ï¼ ^_^ï¼oèªèªoï¼^_^ ï¼",
    "à² â¿à² ",
    "ã½(Â´â½`)/",
    "áµá´¥áµ#",
    "( Í¡Â° ÍÊ Í¡Â°)",
    "â¬ââ¬ï»¿ ã( ã-ãã)",
    "ã½(Â´ã¼ï½)ã",
    "â(ââ½â)â",
    "Îµ=Îµ=Îµ=â(;*Â´Ð`)ï¾",
    "(â¬ à² çà² )",
    "â¬ââ¬â°Í¡â(áµáµáµÍâ)",
    "â»ââ» ï¸µã½(`ÐÂ´)ï¾ï¸µï»¿ â»ââ»",
    r"Â¯\_(ã)_/Â¯",
    "Êáµá´¥áµÊ",
    "(`ï½¥Ïï½¥Â´)",
    "Êâ¢á´¥â¢Ê",
    "á(ï½ã¼Â´á)",
    "ÊÊÌÍÊÌÊ",
    "ï¼ãï¾Ðï¾ï¼",
    r"Â¯\(Â°_o)/Â¯",
    "(ï½¡ââ¿âï½¡)",
]

RUNS_STR = [
        "Hey! Hara gedirsÉn?",
    "Ha? NÉ? QaÃ§dÄ±lar ?",
    "ZZzzZZzz... Noldu? oh, yenÉ onlarimiÅ, boÅ ver.",
    "Geri gÉl!",
    "QaÃ§Ä±n OneBot gÉlir !!",
    "Divara diqqÉt elÉ !",
    "MÉni onlarnan tÉk saxlama !!",
    "QaÃ§san, Ã¶lÉrsÉn.",
    "Ay sÉni zarafatcÄ±Ä±l, mÉn hÉr yerdÉyÉm.",
    "Bunu elÉdiyivÉ gÃ¶rÉ peÅman olacaÄsan...",
    "/kickme butonunu da yoxlaya bilÉrsÉn, ÉylÉncÉli olduÄunu sÃ¶ylÉyirlÉr.",
    "Get baÅqa birini narahat elÉ, burda heÃ§kimin vecinÉ deyilsÉn.",
    "QaÃ§a bilÉrsÉn amma gizlÉnÉ bilmÉzsÉn.",
    "ElÉyÉbildiklÉrin elÉ bu qÉdÉrdi ?",
    "Arxandayam...",
    "QonaÄlarÄ±n var!",
    "Bunu asan yoldan edÉ bilÉriy, yada Ã§Étin yoldan.",
    "BaÅa dÃ¼ÅmÃ¼rsÉn, elÉ mi?",
    "Haha, qaÃ§san yaxÅÄ± olar.!",
    "ZÉhmÉt olmasa, xatÄ±rlat mÉnÉ nÉ qÉdÉr vecimÉsÉn?",
    "SÉnin yerindÉ olsam daha da sÃ¼rÉtli qaÃ§ardÄ±m.",
    "Bu tamamiylÉ axtardÄ±ÄÄ±mÄ±z robotdu.",
    "BÉlkÉ bÉxt sÉnÉ gÃ¼lÉr.",
    "TanÄ±nmÄ±Å son sÃ¶zlÉr.",
    "VÉ sonsuza qÉdÉr itkin dÃ¼ÅdÃ¼lÉr, heÃ§ gÃ¶runmÉdilÉr.",
    "\"Hey, mÉnÉ baxÄ±n ! Bottan qaÃ§a bilirÉm Ã§ox Élayam!\" - bu adam",
    "BÉli bÉli, /kickme butonuna indidÉn bas.",
    "BaxÄ±n, bu Ã¼zÃ¼yÃ¼ alÄ±n vÉ Mordor'a gedin.",
    "ÆfsanÉyÉ gÃ¶rÉ onlar hÉlÉ dÉ iÅlÉyir...",
    "Harry Potter'Ä±n ÉksinÉ, valideyinlÉrin sÉni mÉndÉn qoruya bilmÉz.",
    "Qorxu ÉsÉbÉ, ÉsÉb nifrÉtÉ, nifrÉt acÄ±ya yol aÃ§ar. Qorxu iÃ§indÉ qaÃ§maya davam elÉsÉn,"
    "bir sonraki Vader sÉn olabilÉrsÉn.",
    "BirdÉn Ã§ox hesablama edildikdÉn sonra, dalaverelerine olan maraÄÄ±mÄ±n tam olaraÄ 0âa bÉrabÉr olduÄuna qÉrar verdim.",
    "ÆfsanÉyÉ gÃ¶rÉ onlar hÉlÉ dÉ iÅlÉyir.",
    "Davam elÉ, sÉni burda istÉdiyimizÉ Émin deyilÉm.",
    "SÉn bir sihirb- Oh. GÃ¶zlÉ. Sen Harry deyilsÉn, davam elÉ.",
    "KARÄ°DORDA QAÃMAYIN!",
    "GÃ¶rÃ¼ÅÉriy bÉbÉyim.",
    "Kim itlÉri buraxdÄ± ?",
    "GÃ¼lmÉlidi Ã§Ã¼nkÃ¼ heÃ§kimin vecinÉ deyil.",
    "Ah, nÉ bÃ¶yÃ¼k itki. Bu sÉfÉrkini sevmiÅdim.",
    "AÃ§Ä±ÄÄ± canÄ±m, vecimÉ deyil.",
    "SÃ¼dÃ¼m bÃ¼tÃ¼n oÄlanlarÄ± avluya Ã§Ékir... Biraz da bÉrk qaÃ§!",
    "DoÄrularÄ± qaldÄ±ra BÄ°LMÆZSÆN!",
    "KeÃ§miÅ zamanlarda, Ã§ox Ã§ox uzaÄ bir qalaksidÉ kimsÉ vecinÉ ala bilÉrdi. Amma artÄ±Ä ele deyil.",
    "Hey, onlara bax! QaÃ§Ä±nÄ±lmaz banhammer'dÉn qaÃ§Ä±rlar... NÉ qÉdÉr dÉ Åirin.",
    "Han ÉvvÉl vuruldu. MÉn dÉ elÉ edÉcÉm",
    "AÄ dovÅanÄ±n, arxasÄ±nda nÉ edirsÉn ?",
    "HÉkimin dÉ sÃ¶ylÉdiyi kimi... QAÃ!",
]

HELLOSTR = [
    "Salamm!",
    "NÉ var nÉ yox MÃ¼dÃ¼r!",
    "NecÉsÉnâ?",
    "âHey NÉ baÅ verir?",
    "Salam, salam, salam!",
    "Salamm, kim var orda?, MÉn danÄ±ÅÄ±ram.",
    "Bunun kim olduÄunu bilirsÉn",
    "Hey Yo!",
    "NÉ var nÉ yox.",
    "Salamlar vÉ salamlar !",
    "Salam, gÃ¼niÅÄ±ÄÄ±!",
    "Hey, nÉ var nÉ yox, salam!",
    "NecÉ gedirâ, balaca civciv?",
    "Ce-e!",
    "NecÉsÉn-doody!",
    "Salam, birinci sinif kÃ¼Ã§Ã¼yÃ¼!",
    "BarÄ±ÅaÄ!",
    "Salam, dostum!",
    "S-salam!",
]

SHGS = [
    "â(Â´Ð´ï½)â",
    "â(Â´ï½ï½)â",
    "â(Â´ã¼ï½)â",
    "â(ï¿£ãï¿£)â",
    "â®(â¯ââ°)â­",
    "â®(â¯_â°)â­",
    "â(Â´Ð´`)â",
    "â(Â´âï½)â",
    "Ê(Ìâ¡â)Ê",
    "â(ï¾ï½ï¾)â",
    "â('Ð´')â",
    "â(âï½`;)â",
    "ã(Â´ï¼ï½;)ã",
    "â( -â-)â",
    "Êï¼Â´âà±ªâï¼Ê",
    "ã½(ãï½ão)ã",
    "ã½(~ï½~ )ã",
    "â(~ã¼~;)â",
    "â(-ãã¼;)â",
    r"Â¯\_(ã)_/Â¯",
    r"Â¯\_(â_Êâ)_/Â¯",
    r"Â¯\_à¼¼ à²¥ â¿ à²¥ à¼½_/Â¯",
    "ä¹( â°Í¡  Ä¹Ì¯ â°Í¡ ) ã",
]

CRI = [
    "Ø£â¿Ø£",
    "â¥ï¹â¥",
    "(;ï¹;)",
    "(ToT)",
    "(â³Ðâ³)",
    "(à²¥ï¹à²¥)",
    "ï¼ï¼ã¸ï¼ï¼",
    "(Tï¼¿T)",
    "ï¼Ïã¼Ïï¼",
    "(ï¼´â½ï¼´)",
    "(âï¹â)",
    "ï¼ï½Ðï½ï¼",
    "(Â´Ðâã½",
    "(;Ð;)",
    "ï¼>ï¹<ï¼",
    "(TÐ´T)",
    "(ã¤ï¹â)",
    "à¼¼â¯ï¹â¯à¼½",
    "(ãï¹ã½)",
    "(ãAã½)",
    "(â¥_â¥)",
    "(TâT)",
    "(à¼àº¶âà¼àº¶)",
    "(âï¹â°)ï½¡",
    "(à²¥_Êà²¥)",
    "(ã¤Ð´â)",
    "(âÍ_âÌ¥)",
    "(à®ï¹à®`ï½¡)",
    "à¼¼à²¢_à²¢à¼½",
    "à¼¼ à¼àº¶ à·´ à¼àº¶à¼½",
]

SLAP_TEMPLATES = [
     "{victim} istifadÉÃ§isini {item} ilÉ {hits} .",
    "{victim} istifadÉÃ§isini {item} ilÉ Ã¼zÃ¼nÉ {hits} .",
    "{victim} istifadÉÃ§isini {item} ilÉ biraz {hits} .",
    "{victim} istifadÉÃ§isinÉ {item} {throws} .",
    "{victim} istifadÉÃ§isini {item} ilÉ Ã¼zÃ¼nÉ {throws} .",
    "{victim} istifadÉÃ§isinÉ tÉrÉf {item} atÄ±r.",
    "{victim} axmaqÄ±na {item} ilÉ ÅillÉ vurur.",
    "{victim} istifadÉÃ§isini yere sabitlÉyib ard-arda {item} ilÉ {hits} .",
    "{item} alaraÄ {victim} {hits}.",
    "{victim} istifadÉÃ§isini stola baÄlayÄ±b {item} {throws} .",
    "{victim} istifadÉÃ§isini dostca itÉlÉyÉrÉk lavada Ã¼zmÉyi Ã¶yrÉdir."
]

ITEMS = [
        "dÉmir tava",
    "bÃ¶yÃ¼k alabalÄ±Ä",
    "beyzbol Ã§ubuÄu",
    "kriket Ã§ubuÄu",
    "taxta baston",
    "mismar",
    "yazÄ±cÄ±",
    "lapatka",
    "boru monitoru",
    "fizika dÉftÉri",
    "krem aparatÄ±",
    "Richard Stallman'Ä±n portreti",
    "televizor",
    "beÅ ton kamaz",
    "koli bandajÄ±",
    "kitab",
    "dizÃ¼stÃ¼ komputer",
    "kÃ¶hnÉ televizor",
    "daÅlÄ± kisÉ",
    "gÃ¶yqurÅaÄÄ± alabalÄ±ÄÄ±",
    "plastik cÃ¼cÉ",
    "mismarlÄ± Ã§ubuÄ",
    "yanÄÄ±n sÃ¶ndÃ¼rÃ¼cÃ¼",
    "aÄÄ±r daÅ",
    "kir yÄ±ÄÄ±nÄ±",
    "arÄ± yuvasÄ±",
    "Ã§Ã¼rÃ¼y Ét parÃ§asÄ±",
    "ayÄ±",
    "tonlarca kÉrpic",
]

THROW = [
    "atÄ±r",
    "fÄ±rladÄ±r",
    "tullayÄ±r",
    "yaÄdÄ±rÄ±r",
]

HIT = [
    "vurur",
    "sÉrt vurur",
    "ÅillÉlÉyir",
    "yumruÄlayÄ±r",
    "keÃ§irdir",
]

# ===========================================

@register(outgoing=True, pattern="^.heyvan ?(.*)")
async def hayvan(e):
    arg = e.pattern_match.group(1)
    if arg == "piÅik":
        args = "cat"
    elif arg == "it":
        args = "dog"
    elif arg == "quÅ":
        args = "birb"
    elif arg == "qurd":
        args = "fox"
    elif arg == "panda":
        args = "panda"
    else:
        arg = "piÅik"
        args = "cat"

    foto = requests.get(f'https://some-random-api.ml/img/{args}').json()["link"]
    await e.delete()
    await e.client.send_message(
        e.chat_id,
        f"`TÉsadufi bir {arg} fotosu`",
        file=foto
    )

@register(outgoing=True, pattern="^.qerar$")
async def karar(e):
    msaj = ""
    if e.reply_to_msg_id:
        rep = await e.get_reply_message()
        replyto = rep.id
        msaj += f"[Dostum](tg://user?id={rep.from_id}), "
    else:
        e.edit("`XaiÅ bir mesaja cavab verin`")
        return
    yesno = requests.get('https://yesno.wtf/api').json()
    if yesno["answer"] == "yes":
        cevap = "bÉli"
    else:
        cevap = "xeyr"
    msaj += f"DeyÉsÉn buna {cevap} deyÉcÉyÉm."

    await e.delete()
    await e.client.send_message(
        e.chat_id,
        msaj,
        reply_to=replyto,
        file=yesno["image"]
    )

@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ .cowsay"""
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', 'Â´')}`")


@register(outgoing=True, pattern="^:/$", ignore_unsafe=True)
async def kek(keks):
    """  ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ .slap, """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Bu istifadÉÃ§ini ÅillÉlÉyÉ bilmÉrÉm, yanÄ±ma bita vÉ daÅ almalÄ±yam !!`"
        )


async def slap(replied_user, event):
    """ !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = choice(SLAP_TEMPLATES)
    item = choice(ITEMS)
    hit = choice(HIT)
    throw = choice(THROW)

    caption = "DTÃUserBot " + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw)

    return caption


@register(outgoing=True, pattern="^-_-$", ignore_unsafe=True)
async def lol(lel):
    """ Tamam... """
    okay = "-_-"
    for i in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern="^;_;$", ignore_unsafe=True)
async def fun(e):
    t = ";_;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    """ Utanmaq ð¤¦ââ """
    await e.edit("ð¤¦ââ")


@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ !! """
    await e.edit(choice(CRI))


@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ copypasta """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`ðMÉnÉð¯BiRâï¸mÆð±ï¸InðVerð`")
        return

    reply_text = choice(EMOJIS)
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "ð±ï¸"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ ! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await vpr.edit("`M É n É ï½ï½ï½ m É t i n ï½ï½ï½!`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ ."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`MÉÉÉÉnÉÉÉÉ biiiiir mÉÉÉÉÉtiiiiin veeeeer!`")
        return

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUï½ï½ï½ï½ï½ï¼¡ï¼¥ï¼©ï¼¯ï¼µÐ°ÐµÐ¸Ð¾ÑÑÑÑÑÑ])", (r"\1" * count),
                     message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ . """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`ï¼¢Í¬Ìºï½ÍÌ ï½ÌµÌï½Ì¬Í ï½ÍÌ¶ï½Ì¼Íï½ÍÍ ï½Ì¼Íï½Ì¨Ìï½ÍÍï½Í®Ì¢ï½ÌÍ ï½Í¢Íï½ÍÌï½Í®Ì´`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            charac += choice(ZALG_LIST[randint(0,2)]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))
    

@register(outgoing=True, pattern="^.hi$")
async def hoi(hello):
    """ salamda salam """
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await owo.edit("` UwU mÉnÉ bir mÉtin ver! `")
        return

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ . """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" Â¯\_(ã)_/Â¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern="^.run$")
async def runner_lol(run):
    await run.edit(choice(RUNS_STR))


@register(outgoing=True, pattern="^oof$")
async def oof(e):
    t = "oof"
    for j in range(16):
        t = t[:-1] + "of"
        await e.edit(t)

                      
@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(16):
        t = t[:-1] + "of"
        await e.edit(t)


@register(outgoing=True, pattern="^skrrt$")
async def oof(e):
    t = "skrrt"
    for j in range(16):
        t = t[:-1] + "rt"
        await e.edit(t)
        

@register(outgoing=True, pattern="^Skrrt$")
async def oof(e):
    t = "Skrrt"
    for j in range(16):
        t = t[:-1] + "rt"
        await e.edit(t)


@register(outgoing=True, pattern="^.fuk")
async def fuk(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    animation_chars = [
            "ð       ðï¸",
            "ð     ðï¸",
            "ð  ðï¸",
            "ððï¸ð¦"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@register(outgoing=True, pattern="^.urek (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    deq = deque(list("ï¸â¤ï¸ð§¡ððððð¤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
    await event.edit("â¤ï¸ð§¡ð" + input_str + "ðððð¤")

@register(outgoing=True, pattern="^.mizah$")
async def mizahshow(e):
    await e.edit(
    "â ï¸â ï¸â ï¸MmMmMmMizahh Åowwð¨ð¨ð¨ð¨ð±ð±ð±ð±ð± \n"
    "ð±ð±â ï¸â ï¸ ððððððððððððððð±ðµ \n"
    "ððððððððððððððð MiZah \n"
    "ÅÉLaLesNdÆn b1r yUdm aLdÄ±mâï¸âï¸âï¸âï¸ \n"
    "AHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHA \n"
    "HAHAHAHAHAHAHHAHAHAHAHAHAHAðððððððð \n"
    "ð GÃLDÃM ALA GÃLDÃÃM \n"
    "hALaL LaN âï¸âï¸âï¸âï¸âï¸âï¸âï¸âï¸ðððððððð \n"
    "ð ÆfSaNÉ mMmMiZah Åooooovv ððððððððð \n"
    "ððððððâ ï¸ \n"
    "ð¯ð¯ð¯ð¯ð¯ð¯ð¯ð¯ð¯ \n"
    "DSTM EYNI BÄ°Ä°Ä°Z ððððð \n"
    "ð¯ð¯â ï¸â ï¸â¿ï¸AÃ YOLU POST SAHÄ°BÄ° VE ONU â¿ï¸QORUYANLAR \n"
    "GÆLÄ°R â¿ï¸â¿ï¸ DÃÃTTâ¿ï¸ \n"
    "DÃÃÃÃTâ¿ï¸DÃÃTâ¿ï¸ð¯ð¯â ï¸ \n"
    "â¿ï¸GÃLMÆLÄ°DÄ° â¿ï¸ \n"
    "CJWJCJWJXJJWDJJQUXJAJXJAJXJWJFJWJXJAJXJWJXJWJFIWIXJQJJQJASJAXJ \n"
    "AJXJAJXJJAJXJWJFWJJFWIIFIWICIWIFIWICJAXJWJFJEICIIEICIEIFIWICJSXJJS \n"
    "CJEIVIAJXBWJCJIQICIWJXð¯ð¯ð¯ð¯ð¯ð¯ððððððð \n"
    "ðâ ï¸ððððððâ ï¸â ï¸â ï¸ððððâ¿ï¸â¿ï¸â¿ï¸ðð \n"
    "ðððð¯â ï¸ðâ¿ï¸ð¨"
    )    


@register(outgoing=True, pattern="^.moon$")
async def moon(event):
    deq = deque(list("ðððððððð"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.clock$")
async def clock(event):
    deq = deque(list("ððððððððððð"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ . """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await mock.edit("`mÆNÉ bIr mÆTin vEr!`")
        return

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ ! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await memereview.edit("`Hah, mÉnasÄ± olmadan alqÄ±ÅlamÄ±ram!`")
        return
    reply_text = "ð "
    reply_text += message.replace(" ", " ð ")
    reply_text += " ð"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern=r"^.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)
    await event.edit(pay)

@register(outgoing=True, pattern=r"^.Ä (.*)")
async def payg(event):
    g = """
     ã¤ 
          â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸

          â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸
     â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸
   â¤ï¸â¤ï¸                     â¤ï¸â¤ï¸
 â¤ï¸â¤ï¸
â¤ï¸â¤ï¸                â¤ï¸â¤ï¸â¤ï¸â¤ï¸
â¤ï¸â¤ï¸                â¤ï¸â¤ï¸â¤ï¸â¤ï¸
 â¤ï¸â¤ï¸                        â¤ï¸â¤ï¸
   â¤ï¸â¤ï¸                     ââ¤ï¸â¤ï¸
     â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸
          â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸â¤ï¸
"""
    paytext = event.pattern_match.group(1)
    await event.edit(g.replace('â¤ï¸', paytext))

@register(outgoing=True, pattern=r"^.bo[sÅ]luq")
async def bosluk(event):
    await event.delete()
    await event.reply('ã¤')

@register(outgoing=True, pattern="^.lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Ä°Åte, keyfine bak.\
    \n[{query}]({r.json()['shorturl']})")


@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ !! """
    options = [
        'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
        'photo', 'document', 'cancel'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if (scam_time > 0):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r".type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ . """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await typew.edit("`MÉnÉ bir mÉtin ver!`")
        return
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)

CmdHelp('memes').add_command(
    'heyvan', 'piÅik/it/panda/quÅ/qurd', 'TÉsadufi bir heyvan fotosu atar.'
).add_command(
    'cowsay', None, 'Bir ÅeylÉr danÄ±Åan inÉk'
).add_command(
    ':/', None, 'Rihad\'Ä±n 3 aydÄ±r qÄ±zÄ±n adÄ±nÄ± Ã¶yrÉnmÉdiyi aÄlÄ±na gÉlir.'
).add_command(
    'qerar', None, 'QÉrar verin.'
).add_command(
    '-_-', None, 'TamamdÄ±r.\n-BirdÉnÉm ustam'
).add_command(
    ';_;', None, 'HÃ¼seynin\' 5 dÉqiqÉdir qaynanasÄ±nÄ± gÃ¶rmÉdiyini dÃ¼ÅÃ¼nÃ¼n.'
).add_command(
    'cp', '<cavab>', 'Emoji falan ÉlavÉ edir.'
).add_command(
    'vapor', '<mesaj/cavab>', 'VaporlaÅdÄ±rÄ±n!'
).add_command(
    'str', '<yazÄ±>', 'YazÄ±yÄ± uzadÄ±n.'
).add_command(
    '10iq', None, 'Coshgyn mesaj yazÄ±r....'
).add_command(
    'mizah', None, 'ÃmÃ¼d Usta mizah edÉrsÉ tez edin.'
).add_command(
    'zal', '<cavablama/mesaj>', 'Ãox qarmaÅÄ±q! HÉr Åey Ã§ox qarmaÅÄ±q.'
).add_command(
    'oof', None, 'of dana'
).add_command(
    'skrrt', None, 'sÄ±kÄ±rt'
).add_command(
    'fuk', None, '+18'
).add_command(
    'urek', '<ad>', 'Sevginizi gÃ¶stÉrin.'
).add_command(
    'fp', None, 'Utanmaq.'
).add_command(
    'moon', None, 'Ay animasiyasÄ±.'
).add_command(
    'clock', None, 'HÃ¼seyn qaynanasÄ±nÄ± gÃ¶zlÉyir. (Saat animasiyasÄ±)'
).add_command(
    'hi', None, 'Salam verin.'
).add_command(
    'owo', None, 'OwoooooWoooo'
).add_command(
    'react', None, 'DÄ±tÄ±yÄ±zÄ±rbotun hÉr ÅeyÉ hÉrÉkÉt vermÉsini dÃ¼zÉldin.'
).add_command(
    'slap', '<cavab>', 'TÉsadufi ÅeylÉrlÉ ÅillÉlÉmÉk Ã¼Ã§Ã¼n mesaja cavab verin.'
).add_command(
    'cry', None, 'AÄlamaq mÄ± istiyirsÉn?'
).add_command(
    'shg', None, 'Â¯\_(ã)_/Â¯'
).add_command(
    'run', None, 'QaÃ§!'
).add_command(
    'mock', '<cavab/mesaj>', 'ElÉ vÉ real ÉylÉncÉni tap.'
).add_command(
    'clap', None, 'MÉni, yapraqlar deyil Yuzurbotlar alqÄ±ÅlÄ±yÄ±r!'
).add_command(
    'f', '<mesaj>', 'F'
).add_command(
    'type', '<yazÄ±>', 'Daktilo kimi yazÄ± yazÄ±n.'
).add_command(
    'lfy', '<sorÄu>', 'BuraxÄ±n Google bunu sizin Ã¼Ã§Ã¼n araÅdÄ±rsÄ±n.'
).add_command(
    'scam', '<hÉrÉkÉt> <vaxt>', 'Saxta hÉrÉkÉtlÉr yaradÄ±n.\nMÃ¶vcus hÉrÉkÉtlÉr: (typing, contact, game, location, voice, round, video, photo, document, cancel)'
).add_command(
    'lfy', '<sorÄu>', 'BuraxÄ±n Google bunu sizin Ã¼Ã§Ã¼n araÅdÄ±rsÄ±n.'
).add_command(
    'boÅluq', None, 'BoÅ mesaj.'
).add_command(
    'Ä', '<mesaj>', 'Ä'
).add()
