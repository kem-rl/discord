from discord.ext.commands import command , cooldown
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "m!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    await  bot.change_presence(activity=discord.Streaming(name="Par kem.rl - Main.py", url="https://www.twitch.tv/kemrl_"))


bot.run("Your_Token_Bot") # Remplace this with token bot discord
