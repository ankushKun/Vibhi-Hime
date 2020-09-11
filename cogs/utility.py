import discord
from discord.ext import commands
import wikipedia
from math import *
from io import StringIO
import sys
from ast import literal_eval
import requests
import random

class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=["im","img","pic"])
    async def image(self,ctx,*,msg):
        async with ctx.typing():
            query = msg

            r = requests.get("https://api.qwant.com/api/search/images",
                params={'count': 50,'q': query,'t': 'images','safesearch': 1,'uiv': 4},
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                })

            response = r.json().get('data').get('result').get('items')
            urls = [r.get('media') for r in response]
            url = random.choice(urls)
            e=discord.Embed(title="Image Search",description=f"\"{query}\" - requested by {ctx.author.mention}",color=0xFF0055)
            e.set_image(url=url)
            await ctx.send(embed=e)




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
