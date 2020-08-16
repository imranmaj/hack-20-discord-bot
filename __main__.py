import os
from . import bot
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)