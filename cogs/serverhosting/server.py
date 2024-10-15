import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')
SECRET_BASE_ID = os.getenv('SECRET_BASE_ID')

class server(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="server",
        description="Start, Stop, or Get the IP of a Server Instance!",
    )
    @app_commands.describe(server_name="Which server?")
    @app_commands.choices(server_name=[
        app_commands.Choice(name="LiteVanilla", value="minecraft-vanilla"),
        app_commands.Choice(name="Palworld", value="palworld"),
        app_commands.Choice(name="Pemnis Zome", value="wormpack2")
    ])
    @app_commands.describe(action="What would you like to do?")
    @app_commands.choices(action=[
        app_commands.Choice(name="Start", value="start"),
        app_commands.Choice(name="Stop",value="stop"),
        app_commands.Choice(name="IP",value="ip")
    ])
    async def server(self, interaction:discord.Interaction, action: app_commands.Choice[str], server_name: app_commands.Choice[str]):
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
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        server(bot),
        guild=discord.Object(id=DEV_GUILD_ID)
    )