import discord
from discord import app_commands
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
from dataHandler import nameFormat
from apiHandler import getData

token = os.getenv("discordbotToken")
dGuildIdOxanoVIP = os.getenv("dGuildIdOxanoVIP")


intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!help'):
        await message.channel.send('These are my commands:')

    if message.content.startswith('!check'):
        print(message.content)
        charlookup = message.content.replace('-'," ")
        username = charlookup.split(' ')[1] #1 because there is "!check" command in front of it.
        server = charlookup.split(' ')[2]
        print(username, server)
        ratingexp = lookup(username, server)
        print(ratingexp)

        await message.channel.send(f"{username}-{server}: {ratingexp}")

def lookup(username, server):
        

    rating = getData(username, server)
    return rating


@tree.command(
    name = "check",
    description = "check pvp exp of player, eg:'oxano-stormscale'",
    guild=discord.Object(id=dGuildIdOxanoVIP))

#Add the guild ids in which the slash command will appear.
#If it should be in all, remove the argument,
#but note that it will take some time (up to an hour)
#to register the command if it's for all guilds.

async def first_command(interaction, player: str):
    playerServer = player
    playerServer = nameFormat(player)
    username = playerServer[0]
    server = playerServer[1]
    ratingexp = lookup(username, server)
    print(ratingexp)

    await interaction.response.send_message(f"{username}-{server}: {ratingexp}")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=dGuildIdOxanoVIP))
    print("Ready!")

client.run(token)