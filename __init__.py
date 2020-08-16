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

    counter_new_line = 0
    counter_chars = 0
    limitedOutput = ""
    timeidx = result.rfind("Execution Time")
    for i in result[:timeidx]:
        if counter_new_line == 30:
            counter_new_line+=1
            if i != "":
                limitedOutput+="Max Number of Lines Reached\n#Truncated output#\n"
            break
        if counter_chars == 1000:
            counter_chars+=1
            if i != "":
                limitedOutput+="\nMax Number of Characters Reached\n#Truncated output#\n"
            break
        if(i == "\n"):
            counter_new_line+=1
        limitedOutput+=i
        counter_chars+=1
            
    limitedOutput += result[timeidx:]

    author = ctx.author.mention
    await ctx.send(f"{author}\n```\n{limitedOutput}```")
