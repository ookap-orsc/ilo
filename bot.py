from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

from cogs.acro import CogAcro
from cogs.nimi import CogNimi
from cogs.preferences import CogPreferences
from cogs.lp import CogLp
from cogs.sp import CogSp
from cogs.ss import CogSs
from cogs.preview import CogPreview

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print("* {}".format(guild.name))

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == bot.user:
        if reaction.emoji == "❌":
            await reaction.message.delete()

"""
@bot.command()
async def reload(ctx):
    jasima.routine()
"""

if __name__ == "__main__":
    bot.add_cog(CogAcro(bot))
    bot.add_cog(CogNimi(bot))
    bot.add_cog(CogPreferences(bot))
    bot.add_cog(CogLp(bot))
    bot.add_cog(CogSp(bot))
    bot.add_cog(CogSs(bot))
    bot.add_cog(CogPreview(bot))
    bot.run(TOKEN, reconnect=True)
