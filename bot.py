import os
import traceback
import sys
from io import StringIO

from discord.ext import commands


from timeout import timeout
from run_python import run_python
from timer import Timer

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"
COMMAND_NAME = "run"
BOUNDS = "```"
LANGUAGE_ENDPOINTS = {
    "python": "",
    "java": ""
}

bot = commands.Bot(command_prefix=PREFIX)


@bot.command(name=COMMAND_NAME)
async def run(ctx):
    # remove !run
    content = ctx.message.content.lstrip(PREFIX + COMMAND_NAME)
    # remove leading and trailing whitespace
    content = content.strip()
    # remove ```
    content = content.strip(BOUNDS)

    # extract language
    language = ""
    for i in content:
        if i == "\n":
            break
        language += i
    content = content[len(language) + 1 :]

    # check if endpoint exists
    if language.lower() not in LANGUAGE_ENDPOINTS:
        await ctx.send("error: invalid language")
        return

    if language.lower() == "python":
        t = Timer()
        with t:
            result = run_python(content)
        await ctx.send(result)
        await ctx.send(t.duration)
    else:
        await ctx.send(content)

if __name__ == "__main__":
    bot.run(TOKEN)
