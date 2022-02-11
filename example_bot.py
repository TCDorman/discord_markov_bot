import os
import discord
from markov import *


client = discord.Client

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content is not (' '):
        await message.channel.send(markov_bot())
        

client.run(os.environ.get('DISCORD_TOKEN'))