import discord
from discord.ext import commands
from random import choice
import os,sys




class Rp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    
    @commands.command()
    async def laugh(self,ctx,*,msg=None):
        i=[]
        with open('./files/roleplay/laugh.txt','r') as f:
            for each in f:
                i.append(each)
        if msg==None:
            msg=''
        em = discord.Embed(title='',description=f'{ctx.author.mention} laughs '+msg[:])
        em.set_image(url=choice(i))
        await ctx.send(embed=em)
        
        
    @commands.command()
    async def kill(self,ctx,*,msg=None):
        i=[]
        with open('./files/roleplay/kill.txt','r') as f:
            for each in f:
                i.append(each)
        if msg==None:
            msg=''
        em = discord.Embed(title='',description=f'{ctx.author.mention} kills '+msg[:])
        em.set_image(url=choice(i))
        await ctx.send(embed=em)
        
    
        
    
    

def setup(bot):
    bot.add_cog(Rp(bot))
    print('---> ROLEPLAY LOADED')

