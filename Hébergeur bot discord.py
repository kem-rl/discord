from discord.ext.commands import command , cooldown
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready.')
bot.run("Your_Token_Bot") # Remplace this with your token bot discord
