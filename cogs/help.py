import discord
from discord.ext import commands
import os
import random
from disputils import BotEmbedPaginator

links_str="""
**-----Youtube-----**
https://youtube.com/AnkushTechCreator
**-----Website-----**
http://ankushtechcreator.com
**-----GitHub------**
https://GitHub.com/ATCtech
**-----Twitter-----**
https://twitter.com/ATC_YT_2014
**----Instagram----**
https://instagram.com/ankush_tech_creator
**-----Fakebook----**
https://facebook.com/ankushtechcreator
**-----Reddit-----**
https://www.reddit.com/u/TECHIE6023
**-----Fiverr-----**
https://fiverr.com/atctech

If you want your own custom discord bot, join this server and DM @IamL or @GEEKY KID
**-----Discord-----**
https://discord.gg/rzJGuWP

__Add Vibhi chan to your server using this link__
https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot
"""

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
  
    
    @commands.command()
    async def help(self,ctx):
        # ABOUT
        abt = discord.Embed(title="Hi I'm Vibhi",description="Official mascot of Weebee Con 2020",color=0xFF0055)
        abt.add_field(name="Prefix (case sensitive)",value="vibhi ",inline=False)
        abt.add_field(name="How to use this help message",value="Add reaction to this message to scroll through the different pages",inline=False)
        abt.add_field(name="Support",value="If you find any bugs or would like to reccomend a feature join this server\nhttps://discord.gg/rzJGuWP",inline=False)
        abt.add_field(name="Vibhi Chan Invite link",value="https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot",inline=True)
        # FUN
        fun = discord.Embed(title="FUN",description="Fun Commmands",color=0xFF0055)
        fun.add_field(name="gif",value="Search for gifs",inline=False)
        fun.add_field(name="meme",value="Show memes",inline=False)
        fun.add_field(name="ask",value="Ask me yes/no questions",inline=False)
        fun.add_field(name="pun",value="Sends puns",inline=False)
        fun.add_field(name="joke",value="Sends jokes",inline=False)
        # ANIME
        anime = discord.Embed(title="ANIMANGA",description="Anime and Manga Commmands",color=0xFF0055)
        anime.add_field(name="anime",value="Anime memes and manga strips",inline=False)
        anime.add_field(name="animegif",value="Random animegif",inline=True)
        # GAMES
        games = discord.Embed(title="GAMES",description="Games commands",color=0xFF0055)
        games.add_field(name="rps",value="Play rock paper scissors",inline=False)
        # UTIL
        util = discord.Embed(title="UTILITIES",description="Useful Commands",color=0xFF0055)
        util.add_field(name="wiki",value="Searches wikipedia",inline=False)
        # MUSIC
        music = discord.Embed(title="MUSIC",description="Music Commmands",color=0xFF0055)
        music.add_field(name="join",value="Joins the connected VC",inline=False)
        music.add_field(name="play",value="Plays a song",inline=False)
        music.add_field(name="pause",value="Pauses the currently playing song",inline=False)
        music.add_field(name="stop",value="Stops playing music",inline=False)
        music.add_field(name="queue",value="Displays the queue",inline=False)
        music.add_field(name="remove",value="Removes a song from the queue",inline=False)
        music.add_field(name="shuffle",value="Shuffles the queue",inline=False)
        music.add_field(name="skip",value="Skips the currently playing song",inline=False)
        # MISC
        misc = discord.Embed(title="MISELLANEOUS",description="Commands that don't fit in any category",color=0xFF0055)
        misc.add_field(name="pfp",value="Shows the profile picture of a user",inline=False)
        misc.add_field(name="say",value="Makes Uraraka say something",inline=False)
        misc.add_field(name="invite",value="Invite link for Uraraka Chan",inline=False)
        misc.add_field(name="stats",value="Stats for Uraraka Chan",inline=False)
        # MODERATION
        mod = discord.Embed(title="MODERATION",description="Mod commands for Admins",color=0xFF0055)
        mod.add_field(name="announce",value="Sends a DM to all members of the server (use with caution)",inline=False)
        mod.add_field(name="dm",value="Sends a DM to the mentioned user",inline=False)
        mod.add_field(name="clear",value="deletes the specified amount of messages from a text channel",inline=False)
        mod.add_field(name="ban/unban",value="bans/unbans the mentioned user",inline=False)
        mod.add_field(name="kick",value="kicks the mentioned user",inline=False)
        # ABOUT
        ln = discord.Embed(title="Developer Social Links",description=links_str,color=0xFF0055)
        
        
        
        embeds = [abt,fun,anime,games,music,util,misc,mod,ln]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()
    

    

def setup(bot):
    bot.add_cog(Help(bot))
    print('---> HELP LOADED')

