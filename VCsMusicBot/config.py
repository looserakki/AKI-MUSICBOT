from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQByDT-L7ejg492_vi8T1yKGQgegl2i1I5opOvSxczk2XmQTr_-Mj44An4sxvofP-vVeIVLWRxU_muSaiI0ZxtfXQZQHfteSVduN6_t_jucxIujCcIQtJGTA5tuWEgig71sJ-nTUWlcahGSvr11yEcuG1q1CWUZKrhmFBihPcydCA0-qHPlg0TFKTkBo0gepgjkcIuHJIgRs-LfqfbuWXsD6Wnqt3zpyp1iR2_17bwgqTuzSkPQNjmAZemTHHyblXG9BHyXRpc_04eg25MkzzpO11Klvt3zuNVXzwD0msrY9hZ2LQwDMreHifkUVBSgdHIrYK7MNpEgedz-5h2mn6dy5X9XNvAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1888191908:AAG5SmEUIh8vuYsxIQyakGI1eaqnmY5q4V4")
BOT_NAME = getenv("BOT_NAME", "ERA-MUSIC")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "PATRICIA_UPDATES")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/62d9980a2bdbbd05cd11e.png")
admins = {}
API_ID = int(getenv("API_ID", "3898418"))
API_HASH = getenv("API_HASH", "5a82313211da04d63297bd4de436228c")
BOT_USERNAME = getenv("BOT_USERNAME", "ERAGANGMUSICBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ERA_ASSISTANT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "PATRICIA_SUPPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "ERA MUSIC")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/LushaiMusic/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
