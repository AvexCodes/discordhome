from dotenv import load_dotenv
load_dotenv()

import os

import discord
from discord.ext import commands

from misc import jsonHandler as jso


client = commands.Bot(command_prefix="-", case_insensitive=True)

@client.event
async def on_ready():
    print(f"[Client] {client.user} connected to discord!")

@client.command(name="shutdown")
async def _shutdown(ctx):
    """
        Shut downs bot
    """
    id = 686846374737739797
    if str(ctx.author.id) != str(id):
        await ctx.send("You are not the bot owner!")
    else:
        print(f"[Client] {client.user} logged out!")
        await ctx.send(':wave: Bye Bye!')
        await ctx.bot.logout()


@client.command(name="togglechange", aliases=["tcg"])
async def _changetoggle(ctx, type: bool):
    """
        Allow/Disallow Light Controller
    """
    id = 686846374737739797
    if str(ctx.author.id) != str(id):
        await ctx.send("You are not the bot owner!")
    else:
        data = { "allowDiscordChange": type }
        jso.writeJson("controller.json", data)

client.load_extension('cogs.LightController')
client.load_extension('cogs.Colours')
client.run(os.getenv("discordToken"))
