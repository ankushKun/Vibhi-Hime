import discord
from discord.ext import commands
import os
import random
from disputils import BotEmbedPaginator

links_str="""
[Youtube](https://youtube.com/AnkushTechCreator)
[Website](http://ankushtechcreator.com)
[GitHub](https://GitHub.com/ATCtech)
[Twitter](https://twitter.com/ATC_YT_2014)
[Instagram](https://instagram.com/ankush_tech_creator)
[Fakebook](https://facebook.com/ankushtechcreator)
[Reddit](https://www.reddit.com/u/TECHIE6023)
[Fiverr](https://fiverr.com/atctech)

[Discord](https://discord.gg/rzJGuWP)

[Vibhi Chan Invite Link](https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot)
"""

help_str="""
**__ABOUT__**
Hi I'm Vibhi, Official mascot of Weebee Con 2020
Prefix(case sensitive) : ``vibhi``

__**SUPPORT**__
If you find any bugs or would like to reccomend a feature [join this server](https://discord.gg/rzJGuWP)

__**INVITE**__
[Invite me to your server](https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot)

__**ROLEPLAY**__
  laugh
  kill
  (more to be added)
__**FUN**__
  gif
  meme
  ask
  pun
  joke
__**ANIME MANGA**__
  anime
  animegif
__**GAMES**__
  rps (rock paper scissor)
__**UTILITY**__
  wiki
__**MUSIC**__
  play
  pause
  stop
  skip
  queue
  join
  shuffle
  remove
__**MISELLANEOUS**__
  pfp
  say
  invite
  stats
  servers
__**MODERATION**__
  announce
  dm
  clear
  ban
  unban
  kick
"""
class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
  
    
    @commands.command()
    async def help(self,ctx):
        
        await ctx.send('I have DMed help to you')
        h = discord.Embed(title='Vibhi Chan help',description=help_str,color=0xFF0055)
        await ctx.author.send(embed=h)
        h = discord.Embed(title='Developer Links',description=links_str,color=0xFF0055)
        await ctx.author.send(embed=h)
        

    

def setup(bot):
    bot.add_cog(Help(bot))
    print('---> HELP LOADED')

