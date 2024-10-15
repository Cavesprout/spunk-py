import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests

@tree.command(
    name="server", 
    description="manages a server instance",
    guilds=[discord.Object(id=DEV_GUILD_ID), discord.Object(id=SECRET_BASE_ID)]
)
@app_commands.describe(server_name="Which server?")
@app_commands.rename(server_name="server_name")
@app_commands.choices(server_name=[
    app_commands.Choice(name="LiteVanilla", value="minecraft-vanilla"),
    app_commands.Choice(name="Palworld", value="palworld"),
    app_commands.Choice(name="Pemnis Zome", value="wormpack2")
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