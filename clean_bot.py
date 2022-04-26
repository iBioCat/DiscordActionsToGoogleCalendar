import discord
from discord.ext import commands
import asyncio
import datetime

TOKEN = 'NDE4MDcwMDE4NDA5MTAzMzcw.DxSzqg.t1O3IkIrFnYRERv2xPlTLsioLyk'
client = discord.ext.commands.Bot(command_prefix = '>')
empty_array = []
@client.event
async def on_ready():
    await client.change_presence(game = discord.Game(name='Cleanning'))

@client.event
async def on_message(message):
    if message.content.startswith('!плей'):
        await client.delete_message(message)
    if message.content.startswith('!скип'):
        await client.delete_message(message)
    if str(message.author) == 'JuniperBot#6999':
        await asyncio.sleep(15, result=None, loop=None)
        if message.reactions == []:
            await client.delete_message(message)





    


client.run(TOKEN)
