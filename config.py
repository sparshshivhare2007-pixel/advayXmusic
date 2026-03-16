# Authored By Certified Coders © 2025

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# ── Core bot config ─────────────────────────────────────────
API_ID = int(getenv("API_ID", 35398511))
API_HASH = getenv("API_HASH", "369b6ef2af46765c4e592168f39bc418")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 8364769546))
OWNER_USERNAME = getenv("OWNER_USERNAME", "oye_nirvi")
BOT_USERNAME = getenv("BOT_USERNAME", "CokeStudioProbot")
BOT_NAME = getenv("BOT_NAME", "˹𝐂ᴏᴋᴇ ✘ 𝙎ᴛᴜᴅɪᴏ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "OYE_NIRVI")

# ── Database & logging ──────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1003320971459))

# ── Limits ──────────────────────────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ───────────────────────────────────────────
API_URL = "https://shrutibots.site"
VIDEO_API_URL = getenv("VIDEO_API_URL")
API_KEY = getenv("API_KEY")
DEEP_API = getenv("DEEP_API")
COOKIE_URL = None
# ── Hosting / deployment ────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ───────────────────────────────────────────
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sparshshivhare2007-pixel/advayXmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

# ── Support links ───────────────────────────────────────────
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/Teamdeatinybots",
)
SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/uff_baby_I",
)

# ── Assistant auto-leave ────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ───────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ──────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv(
    "SPOTIFY_CLIENT_ID",
    "22b6125bfe224587b722d6815002db2b",
)
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET",
    "c9c63c6fbf2f467c8bc68624851e9773",
)

# ── Session strings ─────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ────────────────────────────────────────────
START_VIDS = [
    "https://telegra.ph/file/9b7e1b820c72a14d90be7.mp4",
    "https://telegra.ph/file/72f349b1386d6d9374a38.mp4",
    "https://telegra.ph/file/a4d90b0cb759b67d68644.mp4",
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ",
]

HELP_IMG_URL = "https://files.catbox.moe/yg2vky.jpg"
PING_VID_URL = "https://files.catbox.moe/3ivvgo.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/yhaja5.jpg"
STATS_VID_URL = "https://telegra.ph/file/e2ab6106ace2e95862372.mp4"

TELEGRAM_AUDIO_URL = "https://files.catbox.moe/mlztag.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/tiss2b.jpg"

STREAM_IMG_URL = "https://files.catbox.moe/1d3da7.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/zhymxl.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/veykzq.jpg"

SPOTIFY_ARTIST_IMG_URL = YOUTUBE_IMG_URL
SPOTIFY_ALBUM_IMG_URL = YOUTUBE_IMG_URL
SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ─────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ── Bot Introduction Messages ───────────────────────────────
AYU = ["💞","🦋","🔍","🧪","⚡️","🔥","🎩","🌈","🍷","🥂","🥃","🕊️","🪄","💌","🧨"]

AYUV = [
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫",
    "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ.\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ.",
]

# ── Runtime structures ──────────────────────────────────────
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
autoclean = []
confirmer = {}

# ── Validation ──────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] Invalid SUPPORT_CHANNEL URL")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] Invalid SUPPORT_CHAT URL")
