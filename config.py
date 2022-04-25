import os
from dotenv.main import load_dotenv

load_dotenv()

# Konfigurasi bot
PREFIX = ">teawaffle_"
BOT_NAME = "TeaWaffle Bot"
BOT_DESC = "Bot server Discord nya TeaWaffle"
BOT_COLOR = 0xFF6A3D
BOT_WATCH = "VTubers"
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_MASTER = os.getenv("BOT_MASTER")

# Discord server ID
GUILD_ID = int(os.getenv("ID_GUILD"))

# Discord Channel ID
WELCOMER_CHANNEL_ID = int(os.getenv("ID_CHANNEL_WELCOMER"))
PERKENALAN_CHANNEL_ID = int(os.getenv("ID_CHANNEL_PERKENALAN"))
BOTLOG_CHANNEL_ID = int(os.getenv("ID_CHANNEL_BOTLOG"))

# Discord Role ID
WVTUBER_ROLE_ID = int(os.getenv("ID_ROLE_WVTUBER"))
SIMPER_ROLE_ID = int(os.getenv("ID_ROLE_SIMPER"))
VERIFIED_ROLE_ID = int(os.getenv("ID_ROLE_VERIFIED"))
UNVERIFIED_ROLE_ID = int(os.getenv("ID_ROLE_UNVERIFIED"))

# Pesan error
ERR_MSG_GENERIC = "⚠ **ERROR!**｜Duh error kak! Ga tau kenapa ini..."
ERR_MSG_PERMISSION = "🚫 **RESTRICTED!**｜Perintah terlarang! Cuma yang berijin yang boleh pakai."