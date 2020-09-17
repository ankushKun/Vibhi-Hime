import discord
from discord.ext import commands
import os
import aiml
import io
from time import sleep as delay
from random import randint
from random import choice

kernel = aiml.Kernel()
kernel.bootstrap(brainFile = "./chat-with-vibhi/bot_brain.brn")


class Chat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        
        if "vibhi" in msg.channel.name.lower() and not msg.author.bot:
            async with msg.channel.typing():
                x=str(kernel.respond(str(msg.content)))
                x=x.replace("@everyone","@ everyone")
                x=x.replace("@here","@ here")
                if x.startswith("Oh, you are a poet. "):x="huh?, "+x[19:]
                x=x.replace("ALICE","Vibhi")
                delay(randint(1,2))
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

