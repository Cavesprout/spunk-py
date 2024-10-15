import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')
SECRET_BASE_ID = os.getenv('SECRET_BASE_ID')

class ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Pings the server!"
    )
    async def ping(
        self,
        interaction: discord.Interaction
    ) -> None:
        await interaction.response.send_message(
            "Pong! :3c"
        )
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ping(bot)
    )