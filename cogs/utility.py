import discord
from discord.ext import commands
import wikipedia
from math import *
from io import StringIO
import sys
from ast import literal_eval
import requests
import random
from bs4 import BeautifulSoup


class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=["im","img","pic"])
    async def image(self,ctx,*,msg):
        async with ctx.typing():
            query = msg
            url=f"https://www.google.co.in/search?q={query.replace(' ','+')}&source=lnms&tbm=isch&safe=active"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            images=[]
            for img in soup.find_all('img'):
                images.append(img.get('src'))

            del images[0]
            url=random.choice(images)


            e=discord.Embed(title="Image Search",description=f"\"{msg}\" - requested by {ctx.author.mention}",color=0xFF0055)
            e.set_image(url=url)
            await ctx.send(embed=e)




    @commands.command()
    async def wiki(self,ctx,*,msg):
        try:
            e=discord.Embed(title=msg,description=wikipedia.summary(msg,sentences=10),color=0xFF0055)
            await ctx.send(embed=e)
        except wikipedia.exceptions.DisambiguationError as e:
            s=''
            for i in e.options:
                s+=i+'\n'
            em=discord.Embed(title='Error',description='Try Something from these\n'+s,color=0xFF0055)
            await ctx.send(embed=em)
        except Exception as e:
            em=discord.Embed(title='Error',description='Could not find what you are looking for',color=0xFF0055)
            em.add_field(name=str(e))
            await ctx.send(embed=em)






def setup(bot):
    bot.add_cog(Utility(bot))
    print('---> UTILITY LOADED')
