import discord
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

from apiHandler import getData

token = os.getenv("discordbotToken")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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
        username = charlookup.split(' ')[1]
        server = charlookup.split(' ')[2]
        ratingexp = lookup(username, server)
        print(ratingexp)

        await message.channel.send(f"{username}-{server} {ratingexp}")

def lookup(username, server):
        

        rating = getData(username, server)
        return rating


client.run(token)