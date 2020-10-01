import discord
from discord.ext import commands
import os
import random
from time import sleep as delay



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

    # COIN TOSS
    @commands.command()
    async def toss(self,ctx,side=''):
        side=side.lower()
        possibilities=['heads','tails']
        head=['h','heads','head']
        tail=['t','tails','tail']
        await ctx.send('tossing coin . . .')
        delay(0.5)
        tossed=random.choice(possibilities)
        await ctx.send(f'Its **{tossed}**')

        if side!='':
            if side in head :side='heads'
            elif side in tail :side='tails'

            if side==tossed: await ctx.send('You won')
            else: await ctx.send('You lost')

    # ROLL DIE
    @commands.command()
    async def roll(self,ctx):
        await ctx.send("rolling dice . . .")
        delay(0.5)
        await ctx.send(f"rolled a **{random.choice(range(1,7))}**")

    # TIC TAC TOE
    @commands.command(aliases = ["ttt"])
    async def tictactoe(self,ctx):
        pass





def setup(bot):
    bot.add_cog(Games(bot))
    print('---> GAMES LOADED')
