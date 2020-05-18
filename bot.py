import os

import discord
from discord.ext import commands

from misc import jsonHandler as jso

from misc import inject

inject.injectVariables()


dev = jso.read_json("mode.json")
dev = dev['dev']

if dev == True:
    prefix = os.getenv("devPrefix")
    token = os.getenv("devToken")
else:
    prefix = "-"
    token = os.getenv("discordToken")

client = commands.Bot(command_prefix=prefix, case_insensitive=True)
@client.event
async def on_ready():
    print(f"[Client] {client.user} connected to discord!")
    client.load_extension('cogs.LightController')
    client.load_extension('cogs.Colours')
    client.load_extension('cogs.Fun')
    client.load_extension('cogs.Music')

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

@client.command(name="reload")
async def _reload(ctx, cog: str):
    """
        Reloads a cog
    """
    id = 686846374737739797
    if str(ctx.author.id) != str(id):
        await ctx.send("You are not the bot owner!")
    else:
        await ctx.send("Attempting to reload cog " + cog)
        try:
            client.unload_extension(f"cogs.{cog}")
            client.load_extension(f"cogs.{cog}")
            await ctx.send(f"Reloaded cog {cog}")
        except Exception as e:
            await ctx.send(f"Error whilst loading cog: ```{e}```")

@client.command(name="load")
async def _reload(ctx, cog: str):
    """
        Loads a cog
    """
    id = 686846374737739797
    if str(ctx.author.id) != str(id):
        await ctx.send("You are not the bot owner!")
    else:
        await ctx.send("Attempting to load cog " + cog)
        try:
            client.load_extension(f"cogs.{cog}")
            await ctx.send(f"Loaded cog {cog}")
        except Exception as e:
            await ctx.send(f"Error whilst loading cog: ```{e}```")



client.run(str(token))
