import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import boto3

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')
SECRET_BASE_ID = os.getenv('SECRET_BASE_ID')

class balance(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="start",
        description="Open an account!",
    )

    @app_commands.command(
        name="balance",
        description="Checks your current balance!",
    )
    async def balance(
        self,
        interaction: discord.Interaction
    ) -> None:
        response = "You have not opened an account yet!"
        

        await interaction.response.send_message(
            response
        )
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        balance(bot)
    )