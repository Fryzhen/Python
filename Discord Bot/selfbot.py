#!/usr/bin/env python3

import discord
from discord.ext import commands

TOKEN = ""

CHANNEL_ID = 1250416125594963970

MESSAGE = '$p'

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(MESSAGE)
    await client.close()


client.run(TOKEN, bot=False)
