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
Prefix : ``v!``

__**SUPPORT**__
If you find any bugs or would like to reccomend a feature [join this server](https://discord.gg/rzJGuWP)

__**INVITE**__
[Invite me to your server](https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot)

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
__**ROLEPLAY**__
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
                rolepl+=c+'\n'
            help_str+=rolepl
            #print(rolepl)
            h = discord.Embed(title='Vibhi Chan help',description=help_str,color=0xFF0055)
            await ctx.author.send(embed=h)
            h = discord.Embed(title='Developer Links',description=links_str,color=0xFF0055)
            await ctx.author.send(embed=h)
            await ctx.send('I have DMed help to you')
        except Exception as e:
            print(e)
        
        # ABOUT
        abt = discord.Embed(title="Hi I'm Vibhi",description="Official mascot of Weebee con 2020",color=0x00FF00)
        abt.add_field(name="Prefix",value="v! ",inline=True)
        abt.add_field(name="How to use this help message",value="Add reaction to this message to scroll through the different pages",inline=True)
        abt.add_field(name="Support",value="If you find any bugs or would like to reccomend a feature join this server\nhttps://discord.gg/rzJGuWP",inline=True)
        abt.add_field(name="Vibhi Chan Invite link",value="[Invite](https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot)",inline=True)
        # FUN
        fun = discord.Embed(title="FUN",description="Fun Commmands",color=0x00FF00)
        fun.add_field(name="gif",value="Search for gifs",inline=True)
        fun.add_field(name="meme",value="Show memes",inline=True)
        fun.add_field(name="ask",value="Ask me yes/no questions",inline=True)
        fun.add_field(name="pun",value="Sends puns",inline=True)
        fun.add_field(name="joke",value="Sends jokes",inline=True)
        # ANIME
        anime = discord.Embed(title="ANIMANGA",description="Anime and Manga Commmands",color=0x00FF00)
        anime.add_field(name="anime",value="Anime memes and manga strips",inline=True)
        anime.add_field(name="animegif",value="Random animegif",inline=True)
        # GAMES
        games = discord.Embed(title="GAMES",description="Games commands",color=0x00FF00)
        games.add_field(name="rps",value="Play rock paper scissors",inline=True)
        # UTIL
        util = discord.Embed(title="UTILITIES",description="Useful Commands",color=0x00FF00)
        util.add_field(name="wiki",value="Searches wikipedia",inline=True)
        # MUSIC
        music = discord.Embed(title="MUSIC",description="Music Commmands",color=0x00FF00)
        music.add_field(name="join",value="Joins the connected VC",inline=True)
        music.add_field(name="play",value="Plays a song",inline=True)
        music.add_field(name="pause",value="Pauses the currently playing song",inline=True)
        music.add_field(name="stop",value="Stops playing music",inline=True)
        music.add_field(name="queue",value="Displays the queue",inline=True)
        music.add_field(name="remove",value="Removes a song from the queue",inline=True)
        music.add_field(name="shuffle",value="Shuffles the queue",inline=True)
        music.add_field(name="skip",value="Skips the currently playing song",inline=True)
        # MISC
        misc = discord.Embed(title="MISELLANEOUS",description="Commands that don't fit in any category",color=0x00FF00)
        misc.add_field(name="pfp",value="Shows the profile picture of a user",inline=True)
        misc.add_field(name="say",value="Makes Vibhi say something",inline=True)
        misc.add_field(name="invite",value="Invite link for Vibhi Chan",inline=True)
        misc.add_field(name="stats",value="Stats for Vibhi Chan",inline=True)
        # MODERATION
        mod = discord.Embed(title="MODERATION",description="Mod commands for Admins",color=0x00FF00)
        mod.add_field(name="announce",value="Sends a DM to all members of the server (use with caution)",inline=True)
        mod.add_field(name="dm",value="Sends a DM to the mentioned user",inline=True)
        mod.add_field(name="clear",value="deletes the specified amount of messages from a text channel",inline=True)
        mod.add_field(name="ban/unban",value="bans/unbans the mentioned user",inline=True)
        mod.add_field(name="kick",value="kicks the mentioned user",inline=True)
        # ABOUT
        ln = discord.Embed(title="Developer Social Links",description=links_str,color=0x00FF00)
        # RP
        rp = discord.Embed(title="ROLEPLAY",description=rolepl,color=0x00FF00)
        
        
        embeds = [abt,fun,rp,anime,games,music,util,misc,mod,ln]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()
        

    

def setup(bot):
    bot.add_cog(Help(bot))
    print('---> HELP LOADED')

