import discord
from discord.ext import commands
from discord.ext.commands import bot

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} est connecté 😀!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#######################################################
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Coding myself"))

client.run('ODAzNTM3MDE0NTYwNzg0Mzk0.GXM_FL.Gs4oIY-eRqfYandv90tWWNdTYVzPX3Ax5TELRI')