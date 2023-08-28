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

@client.event
async def on_message(message):
    if message.content.startswith('$embed'):
        embedVar = discord.Embed(title='Hello', description='Desc', color=0x00ff00)
        embedVar.add_field(name='Field1', value='hi', inline=False)
        embedVar.add_field(name='Field2', value='hi2', inline=False)
        await message.channel.send(embed=embedVar)

# @client.event
# async def on_message(message):
#     if message.content.startswith('$invite'):

client.run('ODAzNTM3MDE0NTYwNzg0Mzk0.GXM_FL.Gs4oIY-eRqfYandv90tWWNdTYVzPX3Ax5TELRI')