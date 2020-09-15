import discord
from discord.ext import commands
import os
import aiml
import io

kernel = aiml.Kernel()
kernel.bootstrap(brainFile = "./chat-with-vibhi/bot_brain.brn")


class Chat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if "vibhi" in msg.channel.name.lower() and not msg.author.bot:
            x=kernel.respond(str(msg.content))
            if x.startswith("Oh, you are a poet. "):x="huh?, "+x[19:]
            if "ALICE" in x:x.replace("ALICE","Vibhi")
            await msg.channel.send(x)
            
    @commands.command(aliases=["setupchat","setupvibhi","vibhisetup","chat"])
    async def setuptalk(self,ctx):
        if ctx.message.author.guild_permissions.manage_channels:
            channel = await ctx.guild.create_text_channel('talk-with-vibhi')
            await channel.send("Hello, you can talk with me here.\n:)")
            await ctx.send(f'{channel.mention} created')
        else:
            await ctx.send(f'You dont have Manage Channels permission :(\nAsk an admin yo use this command')
        

    

def setup(bot):
    bot.add_cog(Chat(bot))
    print('---> CHAT LOADED')

