import discord
from discord.ext import commands

class hacker1111111111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Owner commands"""

      
    def help_custom(self):
          emoji = '<:anxLeo:1113105487299366912>'
          label = "Owner"
          description = "Only For Owner"
          return emoji, label, description

    @commands.group()
    async def __Owner__(self, ctx: commands.Context):
        """`blacklist`, `blacklist add`, `blacklist remove`, `slist`, `np`, `np add` , `np remove`, `bdg add`, `bdg remove`, `serverlist`, `dm`"""