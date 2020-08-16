import os
import traceback
import sys
from io import StringIO

from discord.ext import commands

from timeout import timeout
from run_python import run_python
from run_java import run_java
from timer import Timer

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"
COMMAND_NAME = "run"
COMMAND_HELP = """runs code
                    format message: ``\u200B`\u200B{language} code\u200B`\u200B``
                    current languages: python, java"""
BOUNDS = "```"
LANGUAGE_ENDPOINTS = {
    "python": "",
    "java": ""
}

bot = commands.Bot(command_prefix=PREFIX)


@bot.command(name=COMMAND_NAME, help=COMMAND_HELP)
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
        await run(content, run_python, ctx)
    elif language.lower() == "java":
        await run(content, run_java, ctx)
    else:
        await ctx.send(language)

async def run(content, function, ctx):
    result = function(content)
    author = ctx.author.mention
    ends = [0]
    while ends[-1] < len(result):
        end = result.rfind('\n', ends[-1], ends[-1] + 1900) + 1
        if end == 0: end = ends[-1] + 1900
        ends.append(end)
    
    num_messages = len(ends) - 1
    for i in range(num_messages):
        await ctx.send(f'{author} ({i + 1}/{num_messages}):\n' + result[ends[i]:ends[i + 1]])
    
if __name__ == "__main__":
    bot.run(TOKEN)
