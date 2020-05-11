from discord.ext import commands
import discord
import os
import requests
import json

#import cogs.converter
import sys
# sys.path.append("..")
from misc import methods as m

class Colours(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ip = os.getenv("bridge")
        self.user = os.getenv("philipstoken")
    
    @commands.command(name="preview", aliases=["pre", 'precol', 'previewcolour'])
    async def _preview(self, ctx, r: int, g: int, b: int):
        hex = m.rgbToHex(r, g, b)
        colName = m.getColNameByRGB(r, g, b)
        embed=discord.Embed(title=f"{colName}", description=f"RGB: {r} {g} {b}\nHex: {hex}")
        embed.set_thumbnail(url=f"{m.getColImage(r, g, b)}")
        await ctx.send(embed=embed)
       

        
def setup(bot):
    bot.add_cog(Colours(bot))
