from telethon.tl import functions, types
from userbot.events import register
import os


old_first_name = None
old_last_name = None
old_profile_photo = None

@register(outgoing=True, pattern="^.klon ?(.*)")
async def clone(event):
    global old_first_name, old_last_name, old_profile_photo
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    replied_user = await get_user(event)
    if not replied_user:
        await event.edit("User tapılmadı.User seçdiyindən əminsən?.")
        return
  
    me = await event.client.get_me()
    old_first_name = me.first_name
    old_last_name = me.last_name
    old_profile_photo = await event.client.download_profile_photo(me.username)
    
    first_name = replied_user.first_name if replied_user.first_name else ""
    last_name = replied_user.last_name if replied_user.last_name else ""
    
    await event.client(functions.account.UpdateProfileRequest(
        first_name=first_name,
        last_name=last_name,
    ))

 
    profile_pic = await event.client.download_profile_photo(reply_message.sender_id)
    if profile_pic:
  
        uploaded_photo = await event.client.upload_file(profile_pic)
  
        await event.client(functions.photos.UploadProfilePhotoRequest(file=uploaded_photo))
    else:
        await event.edit("Userin profil şəkli tapılmadı.")

    await event.delete()
    await event.respond("Ahaha, səni klonladım.", reply_to=reply_message)

@register(outgoing=True, pattern="^.revert$")
async def revert(event):
    global old_first_name, old_last_name, old_profile_photo
    if event.fwd_from:
        return
    if not (old_first_name or old_last_name or old_profile_photo):
        await event.edit("köhnə profil məlumatları, tapılmadı.")
        return
    
  
    await event.client(functions.account.UpdateProfileRequest(
        first_name=old_first_name,
        last_name=old_last_name,
    ))
    
 
    if old_profile_photo:
        uploaded_photo = await event.client.upload_file(old_profile_photo)
        await event.client(functions.photos.UploadProfilePhotoRequest(file=uploaded_photo))
    
    await event.edit("artıq öz profilindəsən. ⚡")

async def get_user(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id is not None:
            return await event.client.get_entity(reply_message.sender_id)
    elif event.pattern_match.group(1):
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if isinstance(user, int) or user.startswith("@"):
            return await event.client.get_entity(user)
