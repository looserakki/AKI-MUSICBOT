from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCt3YwFqx71ynNNHviUmQ2BeriDRLvH8Qvt6cXe8dtrfb-rD_8-5l1GXy0zZNdZ3wEjH_OxSKaxTCo8N3y0gSCiZPhHxIr8PEhBxbkXlB-LoMe1ruJCPdZc45BsRwSPKya0ojNNt_PGsI5-ETLKh_L6DIeXnKpp1Fh1mCBnKjfTZ7SCONfR9DLWSMk0AnmPJ7EARDEqstBjwCjFrs_6vrOEATC_6n16xqVVH8KIZZMEY4xwvfcqppX5jEiuSo6H1bdgyIxmC1J-LvRV-cUHtene0GKFTyeBkyedsdzmP23w6eIPiWyYyus0ETV1Q6_8x1D_0dZdvj0jSQS0RCkON1Jnb4g4gQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1795262909:AAFiiZwypJJhXpzO9TlPTHnv0lTyKdp_tV0")
BOT_NAME = getenv("BOT_NAME", "AKKI-MUSIC")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "PATRICIA_UPDATES")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/62d9980a2bdbbd05cd11e.png")
admins = {}
API_ID = int(getenv("API_ID", "6285038"))
API_HASH = getenv("API_HASH", "cea8174655dfd00fb51f91f8493e55ee")
BOT_USERNAME = getenv("BOT_USERNAME", "AKKIMUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AKKI_ASSISTANT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GREATPEAPOLE")
PROJECT_NAME = getenv("PROJECT_NAME", "AKKI-MUSIC")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/LushaiMusic/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570 936481432").split()))
