import os
import asyncio
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
import psycopg2
from telethon.tl.types import InputPhoto
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon.tl.types import User
from userbot import BRAIN_CHECKER, WHITELIST

USERINFO= {}

@register(outgoing=True, from_users=WHITELIST, pattern="^.ulist ?(.*)")
async def klon(event):
    # Bağlantıyı kurma
    conn = psycopg2.connect(
        database="apex", user='postgres', password='SsSsSs1212Ss!', host='20.86.136.250', port='5432'
    )
    # Cursor nesnesi oluşturma
    cursor = conn.cursor()

    # Sorguyu çalıştırma
    komut_SELECT = "SELECT * FROM users;"
    cursor.execute(komut_SELECT)

    # Verileri alıp düzenleme
    liste = cursor.fetchall()
    for i in liste:
        await event.edit(f"AD: {i[0]} | id: {i[1]} | ")

    # Cursor ve bağlantıyı kapatma
    cursor.close()
    conn.close()

@register(outgoing=True, pattern="^.aliv ?(.*)")
async def get_user_id(event):  # event parametresini ekleyin
    # Bağlantıyı kurma
    conn = psycopg2.connect(
        database="apex", user='postgres', password='SsSsSs1212Ss!', host='20.86.136.250', port='5432'
    )
    # Cursor nesnesi oluşturma
    cursor = conn.cursor()
    username = 'username_of_the_user'
    # Kullanıcı ID'sini al
    user = await event.client.get_me()
    first_name = user.first_name
    hesabid = user.id
    
    # Kullanıcı var mı diye kontrol et
    cursor.execute("SELECT * FROM users WHERE uid = %s", (hesabid,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        await event.edit("𝙰 𝙿 Σ 𝚇 ✨ - 𝓤𝓼𝓮𝓻𝓫𝓸𝓽 𝓐𝓴𝓽𝓲𝓿𝓭𝓲𝓻!.")
    else:
        # Kullanıcıyı ekle
        komut_INSERT = "INSERT INTO users (uid, uname) VALUES (%s, %s);"
        cursor.execute(komut_INSERT, (hesabid, first_name))
        await event.edit("𝙰 𝙿 Σ 𝚇 ✨ - 𝓤𝓼𝓮𝓻𝓫𝓸𝓽 𝓐𝓴𝓽𝓲𝓿𝓭𝓲𝓻!..")
        conn.commit()
    
    cursor.close()
    conn.close()
