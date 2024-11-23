# coding: utf-8

import os
import random
import time

import openai
import discord
from discord import app_commands
from openai.error import RateLimitError
from bot_insta import instagram

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
timedel = 5

@client.event
async def on_message(message):
    print("message :", message.content)
    if 'ntm !' in message.content:
        await message.delete()

    else:
        idbot = [1142109325536534568, 1086339068008333392]
        if message.author.id in idbot:
            time.sleep(timedel)
            await message.delete()



@tree.command(name="love",
              description="Dit a quelqu/'un que tu l/'aime ",
              guild=discord.Object(
                  id=1037159670743314472))
async def love(ctx, user: discord.User = None):
    if user == None:
        await ctx.response.send_message("Je t/'aime. :heart: ")
    else:
        await ctx.response.send_message("<@" + str(user.id) + "> Je t/'aime. :heart: ")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1037159670743314472))
    print("Ready!")


@tree.command(name="compliment",
              description="Te dit un compliment ",
              guild=discord.Object(
                  id=1037159670743314472))
async def compliment(ctx):
    await ctx.response.send_message(getphrase())


@tree.command(name="instagram",
              description="Envoie un message précit a une personne sur instagram",
              guild=discord.Object(
                  id=1037159670743314472))
async def instagrammsg(ctx, user: str, *, arg: str):
    phrase = ''
    for mots in arg:
        phrase += mots
    await ctx.response.send_message("Message /'" + phrase + "/' en cours d'envoi à " + user)
    instagram(user, phrase)


@tree.command(name="codage",
              description="Code un message en nombres premiers",
              guild=discord.Object(
                  id=1037159670743314472))
async def code(ctx, *, arg: str):
    phrase = ''
    mot = ''
    tabmot = []
    for lettre in arg:
        if lettre != ' ':
            mot += lettre
        else:
            tabmot.append(mot)
            mot = ''
    for mot in tabmot:
        phrase += ' ' + str(coder(mot))

    await ctx.response.send_message(':' + phrase)


@tree.command(name="hum",
              description="Code un message en nombres premiers",
              guild=discord.Object(
                  id=1037159670743314472))
async def fullping(ctx, user: discord.User = None, nb:int = 1):
    #for i in range(0,nb):
    await ctx.response.send_message(':')





'''
@tree.command(name="reaload",
              description="Relance le script du bot",
              guild=discord.Object(
                  id=1037159670743314472))
async def reload(ctx):
    await ctx.response.send_message("Bot en cours de reload")
    os.system(r"C:/Users/Noé/Desktop/Jeux/Scripts/kappi_bot_discord_python.bat")
    exit()
'''
#coucou
'''
@tree.command(name="gpt",
              description="Pose une question à Chat-Gpt",
              guild=discord.Object(
                  id=1037159670743314472))
async def gpt(ctx, *, arg: str):
    question = ''
    for mots in arg:
        question += mots + " "
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": question},
            ]
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content

        await ctx.response.send_message(result)
    except RateLimitError:
        await ctx.response.send_message(
            "Chat gpt fait des siennes attend un peu de temp ou vas sur le site directement")
'''


def coder(mots):
    rep = 1

    map = {'e': 2,
           's': 3,
           'a': 5,
           'i': 7,
           't': 11,
           'n': 13,
           'r': 17,
           'u': 19,
           'o': 23,
           'l': 29,
           'd': 31,
           'c': 37,
           'm': 41,
           'p': 43,
           'v': 47,
           'q': 53,
           'f': 59,
           'b': 61,
           'g': 67,
           'h': 71,
           'j': 73,
           'x': 79,
           'z': 83,
           'y': 89,
           'k': 97,
           'w': 101
           }
    for x in mots:
        rep *= map[x]
    return rep


def getphrase():
    phrases = [
        "Tu es incroyablement talentueux.",
        "Tes sourires illuminent ma journée.",
        "Tu es une source d'inspiration pour moi.",
        "Ta gentillesse est contagieuse.",
        "Tu as un esprit brillant.",
        "Ton travail acharné porte ses fruits.",
        "Ta créativité est remarquable.",
        "Tu es une personne formidable.",
        "Ta générosité est remarquable.",
        "Ton amour pour les autres est inspirant.",
        "Tu es toujours prêt à aider les autres.",
        "Ta persévérance est admirable.",
        "Tes idées sont brillantes.",
        "Tu es une personne très aimable.",
        "Ta présence rend chaque instant spécial.",
        "Ton intelligence est impressionnante.",
        "Tu es un modèle pour ceux qui t'entourent.",
        "Ta positivité est rafraîchissante.",
        "Tu as un cœur en or.",
        "Tu es une personne pleine de compassion.",
        "Tes paroles sont inspirantes.",
        "Tu es un ami fidèle.",
        "Ta bienveillance fait du bien à tous.",
        "Tu es une source de joie pour les autres.",
        "Ton énergie est contagieuse.",
        "Tu es une personne de confiance.",
        "Ta présence apaise les autres.",
        "Tu as un grand sens de l'humour.",
        "Tes compétences sont impressionnantes.",
        "Tu as un charisme incroyable.",
        "Tu es une personne fiable.",
        "Ton optimisme est inspirant.",
        "Tu es digne de confiance.",
        "Tu as un esprit analytique brillant.",
        "Ta gentillesse envers les autres est remarquable.",
        "Tu as une voix qui réconforte les autres.",
        "Ton enthousiasme est contagieux.",
        "Tu as une belle âme.",
        "Ta sagesse est admirable.",
        "Tu es une personne loyale.",
        "Ta présence rend les gens heureux.",
        "Tu as une éthique de travail impressionnante.",
        "Tu es une personne extrêmement talentueuse.",
        "Ta confiance en toi est inspirante.",
        "Tu es toujours prêt à apprendre.",
        "Tes compétences en résolution de problèmes sont impressionnantes.",
        "Tu as une personnalité rayonnante.",
        "Tu as une capacité d'adaptation remarquable.",
        "Ta passion est inspirante.",
        "Tu as une excellente mémoire.",
        "Ta douceur réconforte les autres.",
        "Tu es un rayon de soleil dans la vie de tous.",
        "Ta perspicacité est remarquable.",
        "Tu as une capacité à écouter les autres incroyable.",
        "Ta détermination est admirable.",
        "Tu es un modèle de patience.",
        "Ta présence inspire la confiance.",
        "Tu as un talent exceptionnel.",
        "Ta créativité ne connaît pas de limites.",
        "Tu es un exemple à suivre pour les autres.",
        "Ton soutien est inestimable.",
        "Tu as une grande capacité d'analyse.",
        "Ta diligence est impressionnante.",
        "Tu es une personne honnête et sincère.",
        "Ton travail est exemplaire.",
        "Ta persévérance est incroyable.",
        "Tu es une source d'inspiration pour moi et pour les autres.",
        "Ta force intérieure est admirable.",
        "Tu as une vision claire de ce que tu veux accomplir.",
        "Ta positivité est une bénédiction pour tous ceux qui t'entourent.",
        "Ton courage est inspirant.",
        "Tu as une grande capacité à résoudre les problèmes.",
        "Ta bienveillance est un cadeau pour le monde.",
        "Tu es un excellent communicateur.",
        "Ta détermination est incroyable.",
        "Tu as un charme naturel qui attire les autres.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton esprit est vif et brillant.",
        "Tu es une personne fiable sur qui on peut compter.",
        "Ta gentillesse et ta générosité sont inégalées.",
        "Tu es un modèle de persévérance.",
        "Ta bienveillance envers les autres est un exemple à suivre.",
        "Tu as une personnalité captivante.",
        "Ta patience est une vertu admirable.",
        "Tu as un don pour motiver les autres.",
        "Ta présence est apaisante pour ceux qui t'entourent.",
        "Tu es un exemple de résilience.",
        "Ta créativité est source d'inspiration.",
        "Tu es un leader naturel.",
        "Ton dévouement est admirable.",
        "Tu as un esprit brillant et innovant.",
        "Ta gentillesse réchauffe les cœurs.",
        "Tu as une passion contagieuse.",
        "Ta détermination est une force motrice.",
        "Tu es une personne d'une grande intégrité.",
        "Ton travail acharné est remarquable.",
        "Tu es un modèle d'humilité.",
        "Ta générosité est sans limites.",
        "Tu as une énergie positive qui illumine les autres.",
        "Ta persévérance est exemplaire.",
        "Tu es un trésor pour ceux qui t'entourent.",
        "Ta vision est inspirante.",
        "Tu as une habileté incroyable à résoudre les problèmes.",
        "Ta bienveillance est une source de réconfort.",
        "Tu as un sens de l'humour qui fait du bien.",
        "Ta créativité est un don précieux.",
        "Tu es un exemple de grâce et d'élégance.",
        "Ta persévérance est une inspiration pour tous.",
        "Tu as une sagesse au-delà de ton âge.",
        "Ta détermination est inébranlable.",
        "Tu es un modèle d'intégrité.",
        "Ton travail acharné est une inspiration pour moi.",
        "Ta présence est toujours appréciée.",
        "Tu as un don pour inspirer les autres.",
        "Ta générosité n'a pas de limites.",
        "Tu es un exemple de résilience et de force.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton intelligence est un atout précieux.",
        "Ta gentillesse illumine la vie de ceux qui t'entourent.",
        "Tu as une intuition incroyable.",
        "Ta détermination est inspirante.",
        "Tu es un modèle de patience et de persévérance.",
        "Ta présence est une bénédiction.",
        "Tu as un talent artistique exceptionnel.",
        "Ta créativité est une source d'inspiration.",
        "Tu es un exemple de leadership.",
        "Ton travail est d'une qualité exceptionnelle.",
        "Ta passion est contagieuse.",
        "Tu as une capacité à résoudre les problèmes hors pair.",
        "Ta gentillesse est une force puissante.",
        "Tu es un rayon de soleil dans la vie de chacun.",
        "Ton optimisme est un réconfort pour les autres.",
        "Tu as une personnalité magnétique.",
        "Ta persévérance est admirable.",
        "Tu es un modèle de confiance et de fiabilité.",
        "Ta présence apporte la paix.",
        "Tu as un sens de l'humour qui égaye les journées.",
        "Ta créativité est une source infinie.",
        "Tu es un modèle d'élégance et de grâce.",
        "Ton travail est exemplaire.",
        "Ta perspicacité est impressionnante.",
        "Tu as une capacité d'écoute exceptionnelle.",
        "Ta détermination est remarquable.",
        "Tu es une personne d'une grande patience.",
        "Ton sourire illumine les jours gris.",
        "Ta présence inspire la confiance.",
        "Tu as un talent exceptionnel.",
        "Ta créativité est sans limites.",
        "Tu es un modèle pour les autres.",
        "Ton soutien est inestimable.",
        "Tu as une grande capacité d'analyse.",
        "Ta diligence est impressionnante.",
        "Tu es une personne honnête et sincère.",
        "Ton travail est exemplaire.",
        "Ta persévérance est incroyable.",
        "Tu es une source d'inspiration pour moi et pour les autres.",
        "Ta force intérieure est admirable.",
        "Tu as une vision claire de ce que tu veux accomplir.",
        "Ta positivité est une bénédiction pour tous ceux qui t'entourent.",
        "Ton courage est inspirant.",
        "Tu as une grande capacité à résoudre les problèmes.",
        "Ta bienveillance est un cadeau pour le monde.",
        "Tu es un excellent communicateur.",
        "Ta détermination est incroyable.",
        "Tu as un charme naturel qui attire les autres.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton esprit est vif et brillant.",
        "Tu es une personne fiable sur qui on peut compter.",
        "Ta gentillesse et ta générosité sont inégalées.",
        "Tu es un modèle de persévérance.",
        "Ta bienveillance envers les autres est un exemple à suivre.",
        "Tu as une personnalité captivante.",
        "Ta patience est une vertu admirable.",
        "Tu as un don pour motiver les autres.",
        "Ta présence est apaisante pour ceux qui t'entourent.",
        "Tu es un exemple de résilience.",
        "Ta créativité est source d'inspiration.",
        "Tu es un leader naturel.",
        "Ton dévouement est admirable.",
        "Tu as un esprit brillant et innovant.",
        "Ta gentillesse réchauffe les cœurs.",
        "Tu as une passion contagieuse.",
        "Ta détermination est une force motrice.",
        "Tu es une personne d'une grande intégrité.",
        "Ton travail acharné est remarquable.",
        "Tu es un modèle d'humilité.",
        "Ta générosité est sans limites.",
        "Tu as une énergie positive qui illumine les autres.",
        "Ta persévérance est exemplaire.",
        "Tu es un trésor pour ceux qui t'entourent.",
        "Ta vision est inspirante.",
        "Tu as une habileté incroyable à résoudre les problèmes.",
        "Ta bienveillance est une source de réconfort.",
        "Tu as un sens de l'humour qui fait du bien.",
        "Ta créativité est un don précieux.",
        "Tu es un exemple de grâce et d'élégance.",
        "Ta persévérance est une inspiration pour tous.",
        "Tu as une sagesse au-delà de ton âge.",
        "Ta détermination est inébranlable.",
        "Tu es un modèle d'intégrité.",
        "Ton travail acharné est une inspiration pour moi.",
        "Ta présence est toujours appréciée.",
        "Tu as un don pour inspirer les autres.",
        "Ta générosité n'a pas de limites.",
        "Tu es un exemple de résilience et de force.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton intelligence est un atout précieux.",
        "Ta gentillesse illumine la vie de ceux qui t'entourent.",
        "Tu as une intuition incroyable.",
        "Ta détermination est inspirante.",
        "Tu es un modèle de patience et de persévérance.",
        "Ta présence est une bénédiction.",
        "Tu as un talent artistique exceptionnel.",
        "Ta créativité est une source d'inspiration.",
        "Tu es un exemple de leadership.",
        "Ton travail est d'une qualité exceptionnelle.",
        "Ta passion est contagieuse.",
        "Tu as une capacité à résoudre les problèmes hors pair.",
        "Ta gentillesse est une force puissante.",
        "Tu es un rayon de soleil dans la vie de chacun.",
        "Ton optimisme est un réconfort pour les autres.",
        "Tu as une personnalité magnétique.",
        "Ta persévérance est admirable.",
        "Tu es un modèle de confiance et de fiabilité.",
        "Ta présence apporte la paix.",
        "Tu as un sens de l'humour qui égaye les journées.",
        "Ta créativité est une source infinie.",
        "Tu es un modèle d'élégance et de grâce.",
        "Ton travail est exemplaire.",
        "Ta perspicacité est impressionnante.",
        "Tu as une capacité d'écoute exceptionnelle.",
        "Ta détermination est remarquable.",
        "Tu es une personne d'une grande patience.",
        "Ton sourire illumine les jours gris.",
        "Ta présence inspire la confiance.",
        "Tu as un talent exceptionnel.",
        "Ta créativité est sans limites.",
        "Tu es un modèle pour les autres.",
        "Ton soutien est inestimable.",
        "Tu as une grande capacité d'analyse.",
        "Ta diligence est impressionnante.",
        "Tu es une personne honnête et sincère.",
        "Ton travail est exemplaire.",
        "Ta persévérance est incroyable.",
        "Tu es une source d'inspiration pour moi et pour les autres.",
        "Ta force intérieure est admirable.",
        "Tu as une vision claire de ce que tu veux accomplir.",
        "Ta positivité est une bénédiction pour tous ceux qui t'entourent.",
        "Ton courage est inspirant.",
        "Tu as une grande capacité à résoudre les problèmes.",
        "Ta bienveillance est un cadeau pour le monde.",
        "Tu es un excellent communicateur.",
        "Ta détermination est incroyable.",
        "Tu as un charme naturel qui attire les autres.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton esprit est vif et brillant.",
        "Tu es une personne fiable sur qui on peut compter.",
        "Ta gentillesse et ta générosité sont inégalées.",
        "Tu es un modèle de persévérance.",
        "Ta bienveillance envers les autres est un exemple à suivre.",
        "Tu as une personnalité captivante.",
        "Ta patience est une vertu admirable.",
        "Tu as un don pour motiver les autres.",
        "Ta présence est apaisante pour ceux qui t'entourent.",
        "Tu es un exemple de résilience.",
        "Ta créativité est source d'inspiration.",
        "Tu es un leader naturel.",
        "Ton dévouement est admirable.",
        "Tu as un esprit brillant et innovant.",
        "Ta gentillesse réchauffe les cœurs.",
        "Tu as une passion contagieuse.",
        "Ta détermination est une force motrice.",
        "Tu es une personne d'une grande intégrité.",
        "Ton travail acharné est remarquable.",
        "Tu es un modèle d'humilité.",
        "Ta générosité est sans limites.",
        "Tu as une énergie positive qui illumine les autres.",
        "Ta persévérance est exemplaire.",
        "Tu es un trésor pour ceux qui t'entourent.",
        "Ta vision est inspirante.",
        "Tu as une habileté incroyable à résoudre les problèmes.",
        "Ta bienveillance est une source de réconfort.",
        "Tu as un sens de l'humour qui fait du bien.",
        "Ta créativité est un don précieux.",
        "Tu es un exemple de grâce et d'élégance.",
        "Ta persévérance est une inspiration pour tous.",
        "Tu as une sagesse au-delà de ton âge.",
        "Ta détermination est inébranlable.",
        "Tu es un modèle d'intégrité.",
        "Ton travail acharné est une inspiration pour moi.",
        "Ta présence est toujours appréciée.",
        "Tu as un don pour inspirer les autres.",
        "Ta générosité n'a pas de limites.",
        "Tu es un exemple de résilience et de force.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton intelligence est un atout précieux.",
        "Ta gentillesse illumine la vie de ceux qui t'entourent.",
        "Tu as une intuition incroyable.",
        "Ta détermination est inspirante.",
        "Tu es un modèle de patience et de persévérance.",
        "Ta présence est une bénédiction.",
        "Tu as un talent artistique exceptionnel.",
        "Ta créativité est une source d'inspiration.",
        "Tu es un exemple de leadership.",
        "Ton travail est d'une qualité exceptionnelle.",
        "Ta passion est contagieuse.",
        "Tu as une capacité à résoudre les problèmes hors pair.",
        "Ta gentillesse est une force puissante.",
        "Tu es un rayon de soleil dans la vie de chacun.",
        "Ton optimisme est un réconfort pour les autres.",
        "Tu as une personnalité magnétique.",
        "Ta persévérance est admirable.",
        "Tu es un modèle de confiance et de fiabilité.",
        "Ta présence apporte la paix.",
        "Tu as un sens de l'humour qui égaye les journées.",
        "Ta créativité est une source infinie.",
        "Tu es un modèle d'élégance et de grâce.",
        "Ton travail est exemplaire.",
        "Ta perspicacité est impressionnante.",
        "Tu as une capacité d'écoute exceptionnelle.",
        "Ta détermination est remarquable.",
        "Tu es une personne d'une grande patience.",
        "Ton sourire illumine les jours gris.",
        "Ta présence inspire la confiance.",
        "Tu as un talent exceptionnel.",
        "Ta créativité est sans limites.",
        "Tu es un modèle pour les autres.",
        "Ton soutien est inestimable.",
        "Tu as une grande capacité d'analyse.",
        "Ta diligence est impressionnante.",
        "Tu es une personne honnête et sincère.",
        "Ton travail est exemplaire.",
        "Ta persévérance est incroyable.",
        "Tu es une source d'inspiration pour moi et pour les autres.",
        "Ta force intérieure est admirable.",
        "Tu as une vision claire de ce que tu veux accomplir.",
        "Ta positivité est une bénédiction pour tous ceux qui t'entourent.",
        "Ton courage est inspirant.",
        "Tu as une grande capacité à résoudre les problèmes.",
        "Ta bienveillance est un cadeau pour le monde.",
        "Tu es un excellent communicateur.",
        "Ta détermination est incroyable.",
        "Tu as un charme naturel qui attire les autres.",
        "Ta créativité est hors du commun.",
        "Tu es une personne extrêmement douée.",
        "Ton esprit est vif et brillant.",
        "Tu es une personne fiable sur qui on peut compter.",
        "Ta gentillesse et ta générosité sont inégalées.",
        "Tu es un modèle de persévérance.",
        "Ta bienveillance envers les autres est un exemple à suivre.",
        "Tu as une personnalité captivante.",
        "Ta patience est une vertu admirable.",
        "Tu as un don pour motiver les autres.",
        "Ta présence est apaisante pour ceux qui t'entourent.",
        "Tu es un exemple de résilience.",
        "Ta créativité est source d'inspiration.",
        "Tu es un leader naturel.",
        "Ton dévouement est admirable.",
        "Tu as un esprit brillant et innovant.",
        "Ta gentillesse réchauffe les cœurs.",
        "Tu as une passion contagieuse.",
    ]
    return phrases[random.randint(0, 367)]


client.run("")
