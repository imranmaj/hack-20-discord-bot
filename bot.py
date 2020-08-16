import os
import traceback
import sys
from io import StringIO

from discord.ext import commands
import requests
from io import StringIO
import sys, traceback


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

    # send to server
    # r = requests.post(
    #     LANGUAGE_ENDPOINTS[language], json={"content": content}
    # )

    # send eval output to discord
    # await ctx.send(r.text)
    if language.lower() == "python":
        output = StringIO()
        
        sys.stdout = output
        sys.stderr = output
        try: 
            exec(content)
        except SyntaxError as err:
            error_class = err.__class__.__name__
            detail = err.args[0]
            line_number = err.lineno
            await ctx.send(f"{error_class} at line {line_number}")
        except Exception as err:
            error_class = err.__class__.__name__
            # detail = err.args[0]
            # cl, exc, tb = sys.exc_info()
            # line_number = traceback.extract_tb(tb)[-1][1]
            await ctx.send(f"{error_class} at line {line_number}")
        else:
            await ctx.send(output.getvalue())
    else:
        await ctx.send(content)


if __name__ == "__main__":
    bot.run(TOKEN)
