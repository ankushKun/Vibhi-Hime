import discord
from discord.ext import commands
import os


class Message_Events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
  
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        try:
            ms = msg.content.lower()
            #print(f'->  {msg.guild.name} > {msg.channel} ||  {msg.author} : {ms}')
            
            
        except:
            pass

    

def setup(bot):
    bot.add_cog(Message_Events(bot))
    print('---> MESSAGE EVENTS LOADED')
