import os
import sys
import discord
from discord.ext import commands

sys.path.insert(0, os.path.dirname(__file__))


def send_message():
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


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])

    # Executer le script selfbot.py
    send_message()

    return [response.encode()]
