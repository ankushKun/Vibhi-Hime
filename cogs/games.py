import discord
from discord.ext import commands
import os
import random


class Games(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
  
    #   ROCK PAPER SCISSOR
    @commands.command()
    async def rps(self,ctx,player):
        H=['ROCK','PAPER','SCISSOR']
        bot_=random.choice(H)
        user=player.upper()
        if user=='ROCK' or user=='PAPER' or user=='SCISSOR' or user=="SCISSORS":
            await ctx.send(f'{ctx.message.author.mention} : ``{user}``    vs    {self.bot.user.mention} : ``{bot_}``')
            if user==bot_:
                await ctx.send('lol its a tie')
            elif (user=='ROCK' and bot_=='SCISSOR') or (user=='PAPER' and bot_=='ROCK') or ((user=='SCISSOR' or user=='SCISSORS') and bot_=='PAPER'):
                await ctx.send('you win')
            else:
                await ctx.send('bot wins')
        else:
            await ctx.send('you noob\n``rock``  or  ``paper``  or  ``scissor``?')
    

    

def setup(bot):
    bot.add_cog(Games(bot))
    print('---> GAMES LOADED')
