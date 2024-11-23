import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

'''
moi = await bot.fetch_user(390751788862668800)
alexandre = await bot.fetch_user(358199167555862528)
dimitri = await bot.fetch_user(210400974848786432)
vivien = await bot.fetch_user(355021748380499968)
hugo = await bot.fetch_user(163315526045532160)
diego = await bot.fetch_user(366502949842714625)
aurelien = await bot.fetch_user(398433514187653121)
'''


@bot.command(pass_context=True)
async def spam(ctx):
    vivien = await bot.fetch_user(355021748380499968)
    await vivien.send("PUTE")

bot.run("")
