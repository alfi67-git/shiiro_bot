import discord
import Shiiro.main as main
from discord.ext import command
from discord.ext.commands import bot

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Coding myself"))