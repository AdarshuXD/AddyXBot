from AddyX.core.bot import AddyXBot
from AddyX.core.dir import dirr
from AddyX.core.git import git
from AddyX.core.userbot import Userbot
from AddyX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AddyXBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
