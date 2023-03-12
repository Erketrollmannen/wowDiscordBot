import discord
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

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
        print(charlookup)
        username = charlookup.split(' ')[1]
        server = charlookup.split(' ')[2]

        print("username: "+username, "\n" "server: "+server)


def lookup(username, server):
    

client.run(token)