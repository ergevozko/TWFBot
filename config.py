import os
from dotenv import load_dotenv

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
GUILD_ID = os.getenv("ID_GUILD")

# Discord Channel ID
WELCOMER_CHANNEL_ID = os.getenv("ID_CHANNEL_WELCOMER")
PERKENALAN_CHANNEL_ID = os.getenv("ID_CHANNEL_PERKENALAN")
BOTLOG_CHANNEL_ID = os.getenv("ID_CHANNEL_BOTLOG")

# Discord Role ID
WVTUBER_ROLE_ID = os.getenv("ID_ROLE_WVTUBER")
SIMPER_ROLE_ID = os.getenv("ID_ROLE_SIMPER")
VERIFIED_ROLE_ID = os.getenv("ID_ROLE_VERIFIED")
UNVERIFIED_ROLE_ID = os.getenv("ID_ROLE_UNVERIFIED")

# Pesan error
ERR_MSG_GENERIC = "⚠ **ERROR!**｜Duh error kak! Ga tau kenapa ini..."
ERR_MSG_PERMISSION = "🚫 **RESTRICTED!**｜Perintah terlarang! Cuma yang berijin yang boleh pakai."

# Respon bot untuk perintah Interaksi "iloveyou"
BOT_RESP_LOVE = ["Hee? Ada-ada aja kamu kak", "Ah masa? Bercanda pasti nih!!"]
# Respon bot untuk perintah Interaksi "8ball"
BOT_RESP_BAL8 = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As i see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply haze, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Do not count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
