import os

from discord.ext import commands
import requests
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = "!"
COMMAND_NAME = "run"

bot = commands.Bot(command_prefix=PREFIX)

@bot.command(name=COMMAND_NAME)
async def run(ctx):
    content = ctx.message.content.lstrip(PREFIX + COMMAND_NAME)
    r = requests.post("http://localhost:8000", json={"content": content})
    await ctx.send(r.text)

bot.run(TOKEN)