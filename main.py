import discord
from discord.ext import commands
import asyncio
import random

client = commands.Bot(command_prefix = '.')
client.remove_command("help")

client.run('---')
