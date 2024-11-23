import asyncio
import random
import time

import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="$", intents=intents)

intents.guilds = True
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@bot.event
async def on_ready():
    print(f"{bot.user.name} est co")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=1037159670743314472))
        print(f"Command sincro {len(synced)}")
    except Exception as e:
        print(e)


def is_owner(id):
    if id == 355021748380499968:
        return True
    if id == 390751788862668800:
        return True
    else:
        return False


@bot.tree.command(guild=discord.Object(id=1037159670743314472), name="hello", description="Hello")
async def hello_slash(interaction: discord.Interaction):
    await interaction.response.send_message('Hello !')


@bot.tree.command(guild=discord.Object(id=1037159670743314472), name="random",
                  description="Donne une chiffre entre 1 et 100")
async def hello_slash(interaction: discord.Interaction):
    r: int = random.randint(1, 100)
    await interaction.response.send_message(r)


@bot.tree.command(guild=discord.Object(id=1037159670743314472), name="op", description="Est-tu op ?")
async def hello_slash(interaction: discord.Interaction):
    await interaction.response.send_message(is_owner(interaction.user.id))


@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ne répondez pas à vos propres messages
        return

    if "bonjour" in message.content.lower():
        await message.channel.send("Bonjour !")

    oui = False
    if "mere" in message.content.lower():
        oui = True
    if "vivien" in message.content.lower():
        if oui == True:
            await message.channel.send("ntm !")

    await bot.process_commands(message)  # Nécessaire pour que les commandes fonctionnent


@bot.tree.command(guild=discord.Object(id=1037159670743314472), name='clear',
                  description='Clear all user messages in the channel')
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx):
    channel = ctx.channel
    await channel.purge(limit=None)


@bot.tree.command(guild=discord.Object(id=1037159670743314472), name='calc', description='Pose un calcul mental')
async def math_question(ctx):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    question = f'Calculez : {num1} {operator} {num2}'
    answer = eval(f'{num1} {operator} {num2}')
    channel = ctx.channel

    await ctx.response.send_message(question)

    def check(m):
        return m.channel == ctx.channel

    try:
        channel = ctx.channel
        user_response = await bot.wait_for('message', check=check, timeout=15)
        if user_response.content.strip() == str(answer):
            await channel.send('Correct !')
        else:
            await channel.send(f'Incorrect. La réponse était {answer}.')
    except asyncio.TimeoutError:
        channel = ctx.channel
        await channel.send(f'Temps écoulé. La réponse était {answer}.')


def generate_question():
    operand1 = random.randint(1, 20)
    operand2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    question = f"Question: {operand1} {operator} {operand2} = ?"
    if operator == '+':
        answer = operand1 + operand2
    elif operator == '-':
        answer = operand1 - operand2
    elif operator == '*':
        answer = operand1 * operand2
    else:
        answer = operand1 // operand2  # Use floor division for simplicity
    return question, answer


@bot.tree.command(guild=discord.Object(
    id=1037159670743314472),
    name='calculegame',
    description='Jeu de calcul mental')
async def game(ctx):
    num_questions = 5
    correct_answers = 0
    start_time = time.time()
    channel = ctx.channel
    await channel.send("Bienvenue dans le jeu de calcul mental !")
    await channel.send("Tapez la réponse à chaque question. Commencez !\n")

    for _ in range(num_questions):
        question, correct_answer = generate_question()
        await channel.send(question)

        def check(msg):
            return msg.channel == ctx.channel

        try:
            user_message = await bot.wait_for('message', check=check, timeout=20)
            user_answer = int(user_message.content)
        except (ValueError, asyncio.TimeoutError):
            await channel.send("Veuillez entrer un nombre valide.")
            continue

        if user_answer == correct_answer:
            await channel.send("Correct !\n")
            correct_answers += 1
        else:
            await channel.send(f"Incorrect. La réponse correcte était : {correct_answer}\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

    await channel.send("Jeu terminé ! Voici vos résultats :")
    await channel.send(f"Questions correctes : {correct_answers}/{num_questions}")
    await channel.send(f"Temps écoulé : {elapsed_time:.2f} secondes")

    with open("r.txt", "a") as file:
        file.write(f"{ctx.user.id} {correct_answers} {elapsed_time}\n")


@bot.tree.command(guild=discord.Object(id=1037159670743314472), name='top', description='Classement')
async def top(ctx):
    try:
        channel = ctx.channel
        with open("r.txt", "r") as file:
            lines = file.readlines()
            user_data = {}  # Dictionnaire pour stocker les données des utilisateurs

            for line in lines:
                user_id, correct_answers, elapsed_time = line.split()
                user_id = int(user_id)
                correct_answers = int(correct_answers)
                elapsed_time = float(elapsed_time)

                if user_id in user_data:
                    # Mettre à jour les données si le score actuel est meilleur
                    if correct_answers > user_data[user_id]['correct_answers']:
                        user_data[user_id]['correct_answers'] = correct_answers
                        user_data[user_id]['elapsed_time'] = elapsed_time
                else:
                    # Ajouter de nouvelles données si l'utilisateur n'est pas dans le dictionnaire
                    user_data[user_id] = {
                        'correct_answers': correct_answers,
                        'elapsed_time': elapsed_time
                    }

            if user_data:
                sorted_users = sorted(user_data.items(), key=lambda x: x[1]['correct_answers'], reverse=True)

                await channel.send("Meilleurs résultats :")
                for user_id, data in sorted_users:
                    member = await bot.fetch_user(user_id)
                    correct_answers = data['correct_answers']
                    elapsed_time = data['elapsed_time']

                    if correct_answers > 0:
                        best_score = elapsed_time / correct_answers
                        await channel.send(f"{member.display_name} - Meilleur score : {best_score:.2f}")
                    else:
                        await channel.send(f"{member.display_name} - Aucune question correcte enregistrée.")
            else:
                await channel.send("Aucun résultat enregistré pour le moment.")
    except FileNotFoundError:
        await channel.send("Aucun résultat enregistré pour le moment.")


@bot.command()
async def choix(ctx):
    message = await ctx.send("Choisissez une option:")
    await message.add_reaction('1️⃣')  # :one:
    await message.add_reaction('2️⃣')  # :two:
    await message.add_reaction('3️⃣')  # :three:

    def check(reaction, user):
        return user == ctx.author and reaction.message == message and str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣']

    try:
        reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

        if str(reaction.emoji) == '1️⃣':
            await ctx.send("Vous avez choisi :one:")
        elif str(reaction.emoji) == '2️⃣':
            await ctx.send("Vous avez choisi :two:")
        elif str(reaction.emoji) == '3️⃣':
            await ctx.send("Vous avez choisi :three:")
    except asyncio.TimeoutError:
        await ctx.send("Vous n'avez pas fait de choix à temps.")


bot.run("")
