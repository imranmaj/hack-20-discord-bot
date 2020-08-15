import os

from discord.ext import commands
import requests
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = "!"
COMMAND_NAME = "run"
BOUNDS = "```"
bot = commands.Bot(command_prefix=PREFIX)

@bot.command(name=COMMAND_NAME)
async def run(ctx):
    content = ctx.message.content.lstrip(PREFIX + COMMAND_NAME)
    content = content.strip()
    content = content.strip(BOUNDS)

    language = ""
    for i in content:
        if i == "\n":
            break
        language += i
    content = content[len(language)+1::]
    
    r = requests.post("http://localhost:8000", json={"content": content, "language": language})
    
    await ctx.send(r.text)

bot.run(TOKEN)
