from discord.ext import commands

from .python_runner.run_python import run_python
from .java_runner.run_java import run_java


PREFIX = "!"
COMMAND_NAME = "run"
COMMAND_HELP = """runs code
                    format message: ``\u200B`\u200B{language} code\u200B`\u200B``
                    current languages: python, java"""
BOUNDS = "```"
LANGUAGE_FUNCTIONS = {"python": run_python, "java": run_java}

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
    if language.lower() not in LANGUAGE_FUNCTIONS:
        await ctx.send("error: invalid language")
        return
    else:
        await run(content, LANGUAGE_FUNCTIONS[language.lower()], ctx)


async def run(content, function, ctx):
    result = function(content) + "\n"

    counter = 0
    limitedOutput = ""
    for i in result:
        if counter == 30:
            counter+=1
            if i != "":
                limitedOutput+="Max Number of Lines:30\n#Truncated output#\n"
            break;
        if(i == "\n"):
            counter+=1
        limitedOutput+=i
            
    if(counter == 31):
        timeidx = result.rfind("Execution Time")
        limitedOutput += result[timeidx:]

    author = ctx.author.mention
    await ctx.send(f"{author}\n```\n{limitedOutput}```")
