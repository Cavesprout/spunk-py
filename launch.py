import os
import requests
import discord
import json
import random
import aiohttp
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from lib.littlecup import pool

load_dotenv()
APPLICATION_ID = os.getenv('APPLICATION_ID')
TOKEN = os.getenv('DISCORD_TOKEN')
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')
SECRET_BASE_ID = os.getenv('SECRET_BASE_ID')
GUILD_IDS = os.getenv('GUILD_IDS')

class SpunkBot(commands.Bot):
    
    def __init__(self):
        super().__init__(
            command_prefix="&",
            intents = discord.Intents.all(),
            application_id = APPLICATION_ID
        )

        self.initial_extensions = [
            "cogs.debug.ping",
            "cogs.babyfights.babyfights",
            "cogs.economy.balance",
            "cogs.serverhosting.server"
        ]

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions:
            print(f"Loaded Extension: {ext}")
            await self.load_extension(ext)
        
        # bot.tree.clear_commands(guilds=[discord.Object(id=DEV_GUILD_ID)])
        await bot.tree.sync(guild=discord.Object(id=DEV_GUILD_ID))

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

bot = SpunkBot()
bot.run(TOKEN)