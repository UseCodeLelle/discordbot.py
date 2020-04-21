import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Yes i am a bot!"))
    print("bot is ready")

bot.run("NzAyMDkyMjk5NTA0NzEzNzM4.Xp7AbQ.-YWjts_H4GbhUrsa0sms1G6Q1kE")