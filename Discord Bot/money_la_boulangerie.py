import os
import discord

bot = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True


def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    channel = bot.get_channel()
    await channel.send(file=discord.File(newest("")))

bot.run("")
