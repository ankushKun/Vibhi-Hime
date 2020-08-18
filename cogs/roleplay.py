import discord
from discord.ext import commands
from random import choice
import os,sys




class Rp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    
    @commands.command()
    async def laugh(self,ctx):
        i=[]
        with open('./files/roleplay/laugh.txt','r') as f:
            for each in f:
                i.append(each)
        em = discord.Embed(title='',description=f'{ctx.author.mention} laughs')
        em.set_image(url=choice(i))
        await ctx.send(embed=em)
        
        
    @commands.command()
    async def kill(self,ctx):
        i=[]
        with open('./files/roleplay/kill.txt','r') as f:
            for each in f:
                i.append(each)
        em = discord.Embed(title='',description=f'{ctx.author.mention} kills')
        em.set_image(url=choice(i))
        await ctx.send(embed=em)
        
    
        
    
    

def setup(bot):
    bot.add_cog(Rp(bot))
    print('---> ROLEPLAY LOADED')

