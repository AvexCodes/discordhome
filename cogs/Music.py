from discord.ext import commands
import lavalink
import os

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('localhost', 7000, os.getenv('password'), "na", 'music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    @commands.command(name='join')
    async def _join(self, ctx):
        await ctx.send('Cog working, and connected to lavalink server')

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)
        
    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot_connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

def setup(bot):
    bot.add_cog(Music(bot))