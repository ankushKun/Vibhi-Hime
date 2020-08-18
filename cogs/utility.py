import discord
from discord.ext import commands
import wikipedia
from math import *
from io import StringIO
import sys
from ast import literal_eval


class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def wiki(self,ctx,*,msg):
        try:
            e=discord.Embed(title=msg,description=wikipedia.summary(msg,sentences=10))
            await ctx.send(embed=e)
        except wikipedia.exceptions.DisambiguationError as e:
            s=''
            for i in e.options:
                s+=i+'\n'
            em=discord.Embed(title='Error',description='Try Something from these\n'+s)
            await ctx.send(embed=em)
        except Exception as e:
            em=discord.Embed(title='Error',description='Could not find what you are looking for')
            em.add_field(name=str(e))
            await ctx.send(embed=em)
        
        

    

def setup(bot):
    bot.add_cog(Utility(bot))
    print('---> UTILITY LOADED')
