# MFM - UserBot
# format for plugins

import math
import os
import re
import time
import heroku3
import lottie
import requests

import spamwatch as spam_watch
from validators.url import url

from platform import python_version
from telethon import version

from userbot import *
from userbot.Config import Config
from userbot.helpers import *
from userbot.helpers import _format, _icsstools, _icssutils

# =================== Owner - MFMVIP ===================

USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "MFM Userbot"
BOT_USERNAME = Config.TG_BOT_USERNAME
ICSBOT = Config.TG_BOT_USERNAME
ICSB = Config.TG_BOT_USERNAME

# =================== Owner - MFMVIP ===================

# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"

TOSHA_NAME = bot.me.first_name
TOSHA_ID = bot.me.id

# Dev tag
tosh = ( 
    "๐ฉ ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค - ๐ซ๐ฌ๐ฝ๐ฌ๐ณ๐ถ๐ท๐ฌ๐น ๐ช\n"
    "ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท\n"
    "๐โ   ๐ซ๐ฌ๐ฝ ๐ผ๐บ๐ฌ๐น 1 โฌ @MFMVIP เผ\n"
    "ูดโถโโโโโโบแดแดแดสแดโปโโโโโโท"
)

# ุจูุงู 
R = (
    "**๐ฐ**  ๐๐ค๐ช๐ง๐๐ ๐๐ค๐ ๐๐ค   **ุงูุนูุงุจ ุงูุงูููุงููู** ๐ฎ๐ช \n"
    "โโโโโโโโโ๐๐๐ฟโโโโโโโโโ\n\n"
    "  โถ **โชผ**  [ุญุฑุจ ุงููุถุงุก ๐ธ](https://t.me/gamee?game=ATARIAsteroids)   \n"
    "  โท **โชผ**  [ูุนุจุฉ ููุงุจู ุจูุฑุฏ ๐ฅ](https://t.me/awesomebot?game=FlappyBird)   \n"
    "  โธ **โชผ**  [ุงููุท ุงููุดุงูุณ ๐ฑ](https://t.me/gamee?game=CrazyCat)   \n"
    "  โน **โชผ**  [ุตูุฏ ุงูุงุณูุงู ๐](https://t.me/gamee?game=SpikyFish3)   \n"
    "  โบ **โชผ**  [ุณุจุงู ุงูุฏุฑุงุฌุงุช ๐](https://t.me/gamee?game=MotoFX2)   \n"
    "  โป **โชผ**  [ุณุจุงู ุณูุงุฑุงุช ๐](https://t.me/gamee?game=F1Racer)   \n"
    "  โผ **โชผ**  [ุดุทุฑูุฌ โ](https://t.me/T4TTTTBOT?game=chess)   \n"
    "  โฝ **โชผ**  [ูุฑุฉ ุงููุฏู โฝ](https://t.me/gamee?game=FootballStar)   \n"
    "  โพ **โชผ**  [ูุฑุฉ ุงูุณูุฉ ๐](https://t.me/gamee?game=BasketBoyRush)   \n"
    "  โฟ **โชผ**  [ุณูุฉ 2 ๐ฏ](https://t.me/gamee?game=DoozieDunks)   \n"
    "  โซ **โชผ**  [ุถุฑุจ ุงูุงุณูู ๐น](https://t.me/T4TTTTBOT?game=arrow)   \n"
    "  โฌ **โชผ**  [ูุนุจุฉ ุงูุงููุงู ๐ต๐ด](https://t.me/T4TTTTBOT?game=color)   \n"
    "  โญ **โชผ**  [ูููุฌ ูู ๐ฝ](https://t.me/gamee?game=KungFuInc)   \n"
    "  โฎ **โชผ**  [๐ ูุนุจุฉ ุงูุงูุนู ๐](https://t.me/T4TTTTBOT?game=snake)   \n"
    "  โฏ **โชผ**  [๐ ูุนุจุฉ ุงูุตูุงุฑูุฎ ๐](https://t.me/T4TTTTBOT?game=rocket)   \n"
    "  โฐ **โชผ**  [ููุจ ุงุจ ๐งฟ](https://t.me/gamee?game=KeepitUP)   \n"
    "  โฑ **โชผ**  [ุฌูุช ูุงู ๐จ](https://t.me/gamee?game=Getaway)   \n"
    "  โฒ **โชผ**  [ุงูุงูููุงู ๐ฎ](https://t.me/gamee?game=ColorHit)   \n"
    "  โณ **โชผ**  [ูุฏูุน ุงููุฑุงุช๐ฎ](https://t.me/gamee?game=NeonBlaster)   \n\n\n"
    "**๐-** ๐๐ค๐ช๐ง๐๐ ๐ฟ๐๐ **โชผ**  [๐๐๐๐๐ผ๐๐ผ](t.me/MFMVIP)   \n"
    "**๐ฐ** ๐๐ค๐ช๐ง๐๐ ๐๐๐๐ **โชผ**  [๐๐ค๐ ๐๐ค](https://t.me/TOKYO_TEAM/102)  "
)
K = "https://github.com/MFMVIP/MFM_USERBOT"

# Alive Bot 
TOSH = (
       f"**โ โซ ุจูุช ุทูููู ูุนูู ุจูุฌุงุญ ๐คโ**\n"
       f"**   - ุงุตุฏุงุฑ ุงูุชููุซูู :** `{version.__version__}\n`"
       f"**   - ุงุตุฏุงุฑ ุทูููู :** `{icsv}`\n"
       f"**   - ุงูุจูุช ุงููุณุชุฎุฏู :** `{ICSB}`\n"
       f"**   - ุงุตุฏุงุฑ ุงูุจุงูุซูู :** `{python_version()}\n`"
       f"**   - ุงููุณุชุฎุฏู :** {mention}\n"
)

# send 
Send = "**โ โซ ุงุณู ุงูุงุถุงูู : {}**\n**โ โซ ุงูููุช ุงููุณุชุบุฑู : {}ุซุงููู**\n**โ โซ ูููุณุชุฎุฏู :** {}"

# mybot
Mb = "**โ โซ ุงูุจูุช ุงููุณุชุฎุฏู - {}**"

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

# Gdrive
G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET
G_DRIVE_DATA = Config.G_DRIVE_DATA
G_DRIVE_FOLDER_ID = Config.G_DRIVE_FOLDER_ID
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None

ics_users = [bot.uid]
if Config.SUDO_USERS:
    for user in Config.SUDO_USERS:
        ics_users.append(user)


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    check = url(Config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


def check_data_base_heal_th():
    is_database_working = False
    output = "ูุง ุชูุฌุฏ ุงู ูุงุนุฏุฉ ุจูุงูุงุช"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"โ {str(e)}"
        is_database_working = False
    else:
        output = "ูุงุนุฏู ุงูุจูุงูุงุช ุชุนูู ุจูุฌุงุญ"
        is_database_working = True
    return is_database_working, output


async def icsa():
    _, check_sgnirts = check_data_base_heal_th()
    sudo = "Enabled" if Config.SUDO_USERS else "Disabled"
    uptime = await get_readable_time((time.time() - StartTime))
    try:
        useragent = (
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/80.0.3987.149 Mobile Safari/537.36"
        )
        user_id = Heroku.account().id
        headers = {
            "User-Agent": useragent,
            "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
            "Accept": "application/vnd.heroku+json; version=3.account-quotas",
        }
        path = "/accounts/" + user_id + "/actions/get-quota"
        r = requests.get(heroku_api + path, headers=headers)
        result = r.json()
        quota = result["account_quota"]
        quota_used = result["quota_used"]

        # Used
        remaining_quota = quota - quota_used
        math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        # Current
        App = result["apps"]
        try:
            App[0]["quota_used"]
        except IndexError:
            AppQuotaUsed = 0
        else:
            AppQuotaUsed = App[0]["quota_used"] / 60
            math.floor(App[0]["quota_used"] * 100 / quota)
        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)
        dyno = f"{AppHours}h {AppMinutes}m/{hours}h {minutes}m"
    except Exception as e:
        dyno = e
    return f"**โ โซ ูุนูููุงุช ุจูุช ุทูููู***\
                 \n - ูุงุนุฏู ุงูุจูุงูุงุช : {check_sgnirts}\
                  \n - ุณูุฏู : {sudo}\
                  \n - ูุฏุฉ ุงูุชุดุบูู : {uptime}\
                  \n - ูุฏู ุงูุงุณุชุฎุฏุงู : {dyno}\
                  "


async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _icssutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
