import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from lib.littlecup import pool

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')
SECRET_BASE_ID = os.getenv('SECRET_BASE_ID')

class babyfights(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="babyfight",
        description="Gets a collection of babies to use as a roster!"
    )
    @app_commands.describe(count="How many babies do you want to generate?")
    async def babyfight(self, interaction:discord.Interaction, count: int):
        rand_pokes = ""
        for i in range(count):
            rand_pokes += str(pool[random.randint(0, len(pool))]) + "\n"
        
        await interaction.response.send_message(rand_pokes)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        babyfights(bot),
        guild=discord.Object(id=DEV_GUILD_ID)
    )