import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='')

@bot.command(name='run')
async def run(ctx):
    await ctx.send('received')

bot.run(TOKEN)