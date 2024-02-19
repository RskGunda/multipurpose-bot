import discord
from discord.ext import commands

class hacker1111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Nsfw commands"""
  
    def help_custom(self):
		      emoji = '<:anxLeo:1113105487299366912>'
		      label = "Media"
		      description = "Show You Media Commands"
		      return emoji, label, description

    @commands.group()
    async def __Nsfw__(self, ctx: commands.Context):
        """`nsfw` , `nsfw 4k` , `nsfw pussy` , `nsfw boobs` , `nsfw lewd` , `nsfw lesbian` , `nsfw blowjob` , `nsfw cum` , `nsfw gasm` , `nsfw hentai`"""