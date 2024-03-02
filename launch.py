import os
import requests
import discord
import json
import random
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from littlecup import pool

load_dotenv()
TOKEN = os.getenv('TESTING_TOKEN')
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')
SECRET_BASE_ID = os.getenv('SECRET_BASE_ID')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(
    name="ping", 
    description="pings",
    guilds=[discord.Object(id=DEV_GUILD_ID), discord.Object(id=SECRET_BASE_ID)]
)
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message("pong!")

@tree.command(
    name="server", 
    description="manages a server instance",
    guilds=[discord.Object(id=DEV_GUILD_ID), discord.Object(id=SECRET_BASE_ID)]
)
@app_commands.describe(server_name="Which server?")
@app_commands.rename(server_name="server_name")
@app_commands.choices(server_name=[
    app_commands.Choice(name="LiteVanilla", value="minecraft-vanilla"),
    app_commands.Choice(name="Palworld", value="palworld")
])
@app_commands.describe(action="What would you like to do?")
@app_commands.rename(action="action")
@app_commands.choices(action=[
    app_commands.Choice(name="Start", value="start"),
    app_commands.Choice(name="Stop",value="stop"),
    app_commands.Choice(name="IP",value="ip")
])
async def server(interaction:discord.Interaction, action: app_commands.Choice[str], server_name: app_commands.Choice[str]):
    URL = "https://4llrgrd1vb.execute-api.us-east-1.amazonaws.com"
    endpoint = "/test/" + server_name.value + "/" + action.value
    if action.value in ["start", "stop"]:
        r = requests.post(url=URL + endpoint)
        if r.status_code == 200:
            await interaction.response.send_message("Request to " + action.value + " succeeded!")
        else:
            await interaction.response.send_message("Something went wrong. Contact Vi.")
    
    if action.value in ["ip"]:
        r = requests.get(url=URL + endpoint)
        if r.status_code == 200:
            await interaction.response.send_message("IP Address: " + r.content.decode().strip("\""))
        else:
            await interaction.response.send_message("Something went wrong. Contact Vi.")
    
    
@tree.command(
    name="babyfight", 
    description="Grab a collection of babies to use as a roster",
    guilds=[discord.Object(id=DEV_GUILD_ID), discord.Object(id=SECRET_BASE_ID)]
)
@app_commands.describe(count="How many babies do you want to generate?")
@app_commands.rename(count="count")
async def roster(interaction:discord.Interaction, count: int):
    rand_pokes = ""
    for i in range(count):
        rand_pokes += str(pool[random.randint(0, len(pool))]) + "\n"
    
    await interaction.response.send_message(rand_pokes)



@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=DEV_GUILD_ID))
    await tree.sync(guild=discord.Object(id=SECRET_BASE_ID))
    print(f'We have logged in as {client.user}')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')


client.run(TOKEN)
