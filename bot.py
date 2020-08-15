import os

from discord.ext import commands
import requests


TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = "!"
COMMAND_NAME = "run"
BOUNDS = "```"

bot = commands.Bot(command_prefix=PREFIX)

@bot.command(name=COMMAND_NAME)
async def run(ctx):
    # remove !run
    content = ctx.message.content.lstrip(PREFIX + COMMAND_NAME)
    # remove leading and trailing whitespace
    content = content.strip()
    # remove ````
    content = content.strip(BOUNDS)

    # extract language
    language = ""
    for i in content:
        if i == "\n":
            break
        language += i
    content = content[len(language)+1::]
    
    # send to server
    r = requests.post("http://localhost:8000", json={"content": content, "language": language})
    
    # send eval output to discord
    await ctx.send(r.text)

if __name__ == "__main__":
    bot.run(TOKEN)
