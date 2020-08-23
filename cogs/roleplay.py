import discord
from discord.ext import commands
from random import choice
import os,sys




class Rp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self,msg):
        ms= msg.content.lower()
        ms+=' '
        if 'v!' in ms:
            ms=ms[2:]
            d = os.listdir('./anime-rp-gifs/')
            if ms[:ms.index(' ')] in d:
                ms=ms[:ms.index(' ')]
                d = os.listdir(f'./anime-rp-gifs/{ms}')
                fil=f'./anime-rp-gifs/{ms}/'+choice(d)
                em = discord.Embed(title='',description=f'{msg.author.mention} {ms}s {msg.content[2+len(ms):]}')
                im = discord.File(fil,filename='rp.gif')
                em.set_image(url='attachment://rp.gif')
                await msg.channel.send(file=im,embed=em)
            

        
    
    

def setup(bot):
    bot.add_cog(Rp(bot))
    print('---> ROLEPLAY LOADED')

