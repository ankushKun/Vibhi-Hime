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
[Vibhi Chan Invite Link](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)
"""

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
  
    
    @commands.command()
    async def help(self,ctx):
        global help_str
        rolepl=""
        try:
            d = os.listdir('./anime-rp-gifs/')
            d.remove('.git')
            d.remove('README.md')
            for c in d:
                rolepl+="   "+c
            
            h = discord.Embed(title='Vibhi Chan help',description='need help?',color=0xFFBF00)
            h.add_field(name='__ABOUT__',value="Hi I'm Vibhi, Official mascot of Weebee Con 2020\nPrefix : ``v!``")
            h.add_field(name='__SUPPORT__',value="If you find any bugs or would like to reccomend a feature [join this server](https://discord.gg/rzJGuWP)")
            h.add_field(name='__INVITE__',value="[Invite me to your server (click here)](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)")
            h.add_field(name='__ROLEPLAY__',value=rolepl)
            h.add_field(name='__FUN__',value='gif   meme   ask   pun   joke')
            h.add_field(name='__ANIME MANGA__',value='anime   manga')
            h.add_field(name='__GAMES__',value='rps')
            h.add_field(name='__UTILITY__',value='wiki')
            h.add_field(name='__MUSIC__',value='play   pause   stop   skip   queue   join   shuffle   disconnect   remove')
            h.add_field(name='__MISC__',value='afk   pfp   say   invite   stats   servers')
            h.add_field(name='__MODERATION__',value='announce   dm   clear   ban   unban   kick')
            h.add_field(name='__DEVELOPER LINKS__',value=links_str)
            await ctx.author.send(embed=h)
            await ctx.send(embed=h)
        except Exception as e:
            print(e)
        
    @commands.command()
    async def roleplay(self,ctx):
        e=discord.Embed(title="Add roleplay commands to the bot",description="visit this github repo add add your roleplay gif in its respective folder or make one folder if it doesnot exist already\n[Anime-rp-gifs (github repo)](https://github.com/ATCtech/anime-rp-gifs)\n#Open-Sourced",color=0xFFBF00)
        await ctx.send(embed=e)
    
    

def setup(bot):
    bot.add_cog(Help(bot))
    print('---> HELP LOADED')

