import discord
from discord.ext import commands
import os
import json


class Message_Events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.data={}
    
    def load_afk(self):
        global data
        with open('files/afk.json','r') as f:
            data = json.loads(f.read())

    def write_afk(self,d={}):
        global data
        with open('files/afk.json','w') as f:
            f.write(json.dumps(d))

    
    @commands.Cog.listener()
    async def on_message(self,msg):
        ms=msg.content
        if not ms.lower().startswith('v!afk'):
            guild_id=str(msg.guild.id)
            user_id=str(msg.author.id)
            tag=guild_id+user_id
            self.load_afk()
            if tag in data:
                e=discord.Embed(title="REMOVED YOUR AFK",description=f"{msg.author.mention} your status was\n{data[tag]}",color=0xFF0055)
                await msg.channel.send(embed=e)
                del data[tag]
                self.write_afk(data)

        for ping in msg.mentions:
            for user in data:
                if user == guild_id+str(ping.id):
                    e=discord.Embed(title="",description=f"{ping.mention} is AFK\n\n{data[user]}",color=0xFF0055)
                    await msg.channel.send(embed=e)

        


    
    @commands.command()
    async def afk(self,ctx,*,status=''):
        global data
        if status=='':status='No status set'
        self.load_afk()
        guild_id=str(ctx.guild.id)
        user=str(ctx.author.id)
        tag=guild_id+user
        data[tag]=status
        self.write_afk(data)
        e=discord.Embed(title="AFK SET",description=f"{ctx.author.mention} is AFK\n{status}",color=0xFF0055)
        await ctx.send(embed=e)

             
        

    

def setup(bot):
    bot.add_cog(Message_Events(bot))
    print('---> MESSAGE EVENTS LOADED')
