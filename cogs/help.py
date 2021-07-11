import discord
from discord.ext import commands
import os
import random
from disputils import BotEmbedPaginator
import pyrebase
import json
from decouple import config

links_str = """
[Youtube](https://www.youtube.com/channel/UCq4FMXXgsbsZmw5A-Mr7zSA) , [GitHub](https://GitHub.com/ankushKun) , [Twitter](https://twitter.com/__AnkushSingh__) , [Instagram](https://instagram.com/__weebletkun__) , [Reddit](https://www.reddit.com/u/TECHIE6023) , [Fiverr](https://fiverr.com/atctech)
[Vibhi Chan Invite Link](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)
"""


firebase = pyrebase.initialize_app(json.loads(config("FIREBASE")))
db = firebase.database()


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        global help_str
        rolepl = ""
        try:
            rolepl = ""
            for each in db.child("RP").child("CMD").get().val():
                rolepl += ", " + each

            h = discord.Embed(
                title="Vibhi Chan help", description="need help?", color=0xFF0055
            )
            h.add_field(
                name="__ABOUT__",
                value="Hi I'm Vibhi Chan\nPrefix : `v!`\nFor custom prefix use `v!prefix`\nDeveloped by : `weeblet~kun#1193`",
            )
            h.add_field(
                name="__CHAT WITH VIBHI__",
                value="Setup a channel to chat with the bot using **v!setupchat**",
            )
            h.add_field(
                name="__INVITE__",
                value="[Invite me to your server (click here)](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)",
            )
            h.add_field(name="__ROLEPLAY__", value=(rolepl[2:1990] + "..."))
            h.add_field(name="__FUN__", value="gif, meme, ask, pun, joke, reddit, boom")
            h.add_field(
                name="__ANIME MANGA__", value="anime(WIP), animegif, anilist, mal"
            )
            h.add_field(name="__GAMES__", value="rps, toss, roll")
            h.add_field(name="__UTILITY__", value="wiki, img, splitimg")
            h.add_field(
                name="__MUSIC__",
                value="play, pause, resume, stop, skip, queue, join, disconnect, remove",
            )
            h.add_field(name="__MISC__", value="pfp, invite, stats, prefix")
            # h.add_field(name='__MODERATION__',value='announce, dm, clear, ban, unban, kickout')
            h.add_field(name="__DEVELOPER LINKS__", value=links_str)
            # await ctx.author.send(embed=h)
            await ctx.send(embed=h)
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(Help(bot))
    print("---> HELP LOADED")
