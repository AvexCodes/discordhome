from discord.ext import commands
import discord
import os
import requests
import json

#import cogs.converter
import sys
# sys.path.append("..")
from misc import methods as m
from misc.ksoft import KSoft as ks
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ip = os.getenv("bridge")
        self.user = os.getenv("philipstoken")
    
    @commands.command(name="meme")
    async def _meme(self, ctx):
        """
        Returns a random meme
        """
        data = ks.meme()
        embed=discord.Embed(description=f"👍 {data['upvotes']} 👎 {data['downvotes']}", color=0x0080ff)
        embed.set_author(name=data['title'])
        embed.set_footer(text="Sourced via KSoft")
        embed.set_image(url=data['image_url'])
        await ctx.send(embed=embed)
        

    @commands.command(name="wikihow")
    async def _wikihow(self, ctx):
        """
        Returns a random WikiHow
        """
        data = ks.wikihow()
        emb=discord.Embed(color=0x0080ff)
        emb.set_author(name=data['title'])
        emb.set_footer(text="Sourced via KSoft")
        emb.set_image(url=data['url'])
        await ctx.send(embed=emb)
    
    @commands.command(name="aww", aliases=["cute"])
    async def _aww(self, ctx):
        """
        Returns a cute image
        """
        data = ks.aww()
        embed=discord.Embed(description=f"👍 {data['upvotes']} 👎 {data['downvotes']}", color=0x0080ff)
        embed.set_author(name=data['title'])
        embed.set_footer(text="Sourced via KSoft")
        embed.set_image(url=data['image_url'])
        await ctx.send(embed=embed)

    @commands.command(name="currency", aliases=["convert"])
    async def _currency(self, ctx, frm: str, to: str, amount: str):
        """
            Convert currency.

            List of currency code symbols can be found here: https://www.xe.com/iso4217.php
        """
        data = ks.convert(to, frm, amount)

        if data == "invalid":
            await ctx.send("Invalid currency!")

        embed=discord.Embed(description=f"${amount} {frm.upper()} -> ${data['pretty']}")
        embed.set_author(name=f"{frm.upper()} -> {to.upper()}")
        embed.set_footer(text="Sourced via KSoft")
        await ctx.send(embed=embed)
        

        
def setup(bot):
    bot.add_cog(Fun(bot))
