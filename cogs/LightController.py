from discord.ext import commands
import discord
import os
import requests
import json

import sys
# sys.path.append("..")
from misc import methods as m
from misc import jsonHandler as jso
from misc.converter import Converter, GamutB


class LightController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ip = os.getenv("bridge")
        self.user = os.getenv("philipstoken")
    
    @commands.command(name="turnoff", aliases=["off", "loff"])
    async def _test(self, ctx, lid: int):
        """
            Turns a light off.

            Params:
                ! lid: integer (light id)

            ! = Required, ? = Optional
        """
        self.data = jso.read_json("controller.json")

        if self.data['allowDiscordChange'] == True:
            m.turnOff(self.ip, self.user, lid)

            embed=discord.Embed(title=f"Light {lid} Turned Off!", url="https://auto.avex.dev", description=f"Succesfully turned light {lid} off!")
            embed.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/59937b8f2994cae8c280ca6c/1504903605561-PYMALOQSSWJRGYEKD8QK/ke17ZwdGBToddI8pDm48kGDpvalPb1SqHoCn1hwN0Y57gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QHyNOqBUUEtDDsRWrJLTmQPoRzxSr1hzN-vPBHt7YyLLXgctAyUJRqJUUGWVDK_ZzIgvsybGcZEPqUYiXY8im/Yonomi+-+Philips+Hue+A19+Smart+Color+Bulb.jpg")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Error: 1 (Permission Denied)", url="https://auto.avex.dev/errors?id=1", description="Sorry, but any remote change, via discord or auto.avex.dev has been disabled! Stay tuned for a change in #status\n\nClick [here](https://avex.dev/errors/1) to view error", color=0xff0000)
            await ctx.send(embed=embed)


    @commands.command(name="turnon", aliases=["on", "lon"])
    async def _on(self, ctx, lid: int):
        """
           Turns a light on. 

           Params:
               ! lid: integer (light id)

           ! = Required, ? = Optional
        """
        self.data = jso.read_json("controller.json")

        if self.data['allowDiscordChange'] == True:
            m.turnOn(self.ip, self.user, lid)

            embed=discord.Embed(title=f"Light {lid} Turned On!", url="https://auto.avex.dev", description=f"Succesfully turned light {lid} on!", color=0x80ff00)
            embed.set_thumbnail(url="https://www.assets.signify.com/is/image/PhilipsLighting/80cc70d6f53343cc8baea9b9009d764d?&wid=110&hei=110&$jpglarge$")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Error: 1 (Permission Denied)", url="https://auto.avex.dev/errors?id=1", description="Sorry, but any remote change, via discord or auto.avex.dev has been disabled! Stay tuned for a change in #status\n\nClick [here](https://avex.dev/errors/1) to view error", color=0xff0000)
            await ctx.send(embed=embed)

    @commands.command(name="changecolour", aliases=["rgb"])
    async def _rgb(self, ctx, lid: int, r: int, g: int, b: int):
        """
            Changes light colour
            
            Params:
                ! lid: integer (light id)
                ! r: integer (0 - 255)
                ! g: integer (0 - 255)
                ! b: integer (0 - 255)

            ! = Required, ? = Optional
        """
        self.data = jso.read_json("controller.json")
        conv = Converter(GamutB)

        if self.data['allowDiscordChange'] == True:
            m.changeCol(lid, conv.rgb_to_xy(r, g, b), 254, 254, self.ip, self.user)
            hex = m.rgbToHex(r, g, b)
            colName = m.getColNameByRGB(r, g, b)
            embed=discord.Embed(title=f"{colName}", description=f"Updated light {lid} to {colName} ({r} {g} {b})")
            embed.set_thumbnail(url=f"{m.getColImage(r, g, b)}")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Error: 1 (Permission Denied)", url="https://auto.avex.dev/errors?id=1", description="Sorry, but any remote change, via discord or auto.avex.dev has been disabled! Stay tuned for a change in #status\n\nClick [here](https://avex.dev/errors/1) to view error", color=0xff0000)
            await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(LightController(bot))
