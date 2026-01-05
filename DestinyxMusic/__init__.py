# Authored By Certified Coders © 2025
from DestinyxMusic.core.bot import MusicBotClient
from DestinyxMusic.core.dir import StorageManager
from DestinyxMusic.core.git import git
from DestinyxMusic.core.userbot import Userbot
from DestinyxMusic.misc import dbb, heroku

from .logging import LOGGER

StorageManager()
git()
dbb()
heroku()

app = MusicBotClient()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
