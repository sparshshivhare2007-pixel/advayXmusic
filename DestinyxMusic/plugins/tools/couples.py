# Authored By Certified Coders © 2025
import os
import random
from datetime import datetime, timedelta
from pathlib import Path

from PIL import Image, ImageDraw, UnidentifiedImageError
from pyrogram import errors, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from DestinyxMusic import app
from DestinyxMusic.core.dir import COUPLE_DIR
from DestinyxMusic.mongo.couples_db import get_couple, save_couple

# Path settings
ASSETS = Path("DestinyxMusic/assets")
FALLBACK = ASSETS / "upic.png"
OUT_DIR = Path(COUPLE_DIR)

# Folder check: Agar directory nahi hai to bana dega
if not OUT_DIR.exists():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

def today() -> str:
    return datetime.now().strftime("%d/%m/%Y")

def tomorrow() -> str:
    return (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")

def circular(path: str | Path) -> Image.Image:
    try:
        img = Image.open(path).convert("RGBA").resize((486, 486))
    except (FileNotFoundError, UnidentifiedImageError, Exception):
        # Agar user ki photo na mile to fallback use karega
        if FALLBACK.exists():
            img = Image.open(FALLBACK).convert("RGBA").resize((486, 486))
        else:
            # Agar fallback bhi na ho to empty transparent image
            img = Image.new("RGBA", (486, 486), (255, 255, 255, 0))
            
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + img.size, fill=255)
    img.putalpha(mask)
    return img

async def safe_get_user(uid: int):
    try:
        return await app.get_users(uid)
    except Exception:
        return None

async def safe_photo(uid: int, name: str) -> Path:
    try:
        chat = await app.get_chat(uid)
        if chat.photo and chat.photo.big_file_id:
            path = await app.download_media(chat.photo.big_file_id, file_name=OUT_DIR / name)
            return Path(path) if path else FALLBACK
    except Exception:
        pass
    return FALLBACK

async def generate_image(chat_id: int, uid1: int, uid2: int, date: str) -> str:
    # YAHAN PATH UPDATE KIYA HAI: destiny/couple.png
    bg_path = ASSETS / "destiny/couple.png"
    
    if not bg_path.exists():
        raise FileNotFoundError(f"Background image nahi mili: {bg_path}")

    base = Image.open(bg_path).convert("RGBA")
    p1 = await safe_photo(uid1, f"pfp1_{chat_id}.png")
    p2 = await safe_photo(uid2, f"pfp2_{chat_id}.png")

    a1 = circular(p1)
    a2 = circular(p2)
    
    # Paste circles on background (Coordinates same rakhe hain)
    base.paste(a1, (410, 500), a1)
    base.paste(a2, (1395, 500), a2)

    out_path = OUT_DIR / f"couple_{chat_id}_{date.replace('/','-')}.png"
    base.save(out_path)

    # Temporary photos delete karna
    for pf in (p1, p2):
        try:
            if pf != FALLBACK and pf.exists():
                os.remove(pf)
        except Exception:
            pass

    return str(out_path)

@app.on_message(filters.command("couple"))
async def couples_handler(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.**")

    wait = await message.reply("🦋")
    cid = message.chat.id
    date = today()

    try:
        record = await get_couple(cid, date)
        if record:
            uid1, uid2, img_path = record["user1"], record["user2"], record["img"]
            user1 = await safe_get_user(uid1)
            user2 = await safe_get_user(uid2)

            if not (user1 and user2) or not img_path or not Path(img_path).exists():
                record = None

        if not record:
            # Members list nikalna
            members = []
            async for m in app.get_chat_members(cid, limit=250):
                if not m.user.is_bot and not m.user.is_deleted:
                    members.append(m.user.id)
            
            if len(members) < 2:
                return await wait.edit("**ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.**")

            tries = 0
            while tries < 10:
                uid1, uid2 = random.sample(members, 2)
                user1 = await safe_get_user(uid1)
                user2 = await safe_get_user(uid2)
                if user1 and user2:
                    break
                tries += 1
            else:
                return await wait.edit("**ᴄᴏᴜʟᴅ ɴᴏᴛ ꜰɪɴᴅ ᴠᴀʟɪᴅ ᴍᴇᴍʙᴇʀꜱ.**")

            img_path = await generate_image(cid, uid1, uid2, date)
            await save_couple(cid, date, {"user1": uid1, "user2": uid2}, img_path)

        caption = (
            "💌 **ᴄᴏᴜᴘʟᴇ ᴏꜰ ᴛʜᴇ ᴅᴀʏ!** 💗\n\n"
            "╔═══✿═══❀═══✿═══╗\n"
            f"💌 **ᴛᴏᴅᴀʏ'ꜱ ᴄᴏᴜᴘʟᴇ:**\n⤷ {user1.mention} 💞 {user2.mention}\n"
            "╚═══✿═══❀═══✿═══╝\n\n"
            f"📅 **ɴᴇxᴛ ꜱᴇʟᴇᴄᴛɪᴏɴ:** `{tomorrow()}`\n\n"
            "💗 **ᴛᴀɢ ʏᴏᴜʀ ᴄʀᴜꜱʜ — ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ɴᴇxᴛ!** 😉"
        )

        await message.reply_photo(img_path, caption=caption)
        await wait.delete()

    except Exception as e:
        await wait.edit(f"**Error:** `{e}`")
