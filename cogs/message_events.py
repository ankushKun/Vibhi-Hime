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
        if msg.author.bot:return
        ms=msg.content
        if not ms.lower().startswith('v!afk'):
            guild_id=str(msg.guild.id)
            user_id=str(msg.author.id)
            tag=guild_id+user_id
            self.load_afk()
            if tag in data:
                #e=discord.Embed(title="REMOVED YOUR AFK",description=f"{msg.author.mention} your status was\n\n{data[tag]}",color=0xFF0055)
                #await msg.channel.send(embed=e)
                no_more_afk=f"welcome back {msg.author.mention}.\n__{data[tag][1]}__.\nYou were pinged __{data[tag][0]}__ times."
                await msg.channel.send(no_more_afk)
                del data[tag]
                self.write_afk(data)
                return

        for ping in msg.mentions:
            guild_id=str(msg.guild.id)
            for user in data:
                if user == guild_id+str(ping.id):
                    #e=discord.Embed(title="",description=f"{ping.mention} is AFK\n\n{data[user]}",color=0xFF0055)
                    #await msg.channel.send(embed=e)
                    data[user][0]+=1
                    self.write_afk(data)
                    msg_afk=f"**{ping.display_name}** is AFK\n\n{data[user][1]}"
                    await msg.channel.send(msg_afk)
        user=str(msg.author.id)
        prefixes = self.get_prefix(user)
        for pfix in prefixes:
            if msg.content.startswith(pfix):
                msg.content = msg.content.replace(pfix,'v!').replace('v! ','v!')
                await self.bot.process_commands(msg)

    def get_prefix(self,id):
        try:
            with open('files/prefixes.json','r')as f:
                l= json.loads(f.read())
                if id in l:
                    return l[id]
                else: return []
        except:
            pass

    def add_prefix(self,id,pf):
        with open('files/prefixes.json','r')as f:
            l = json.loads(f.read())
        if not id in l:
            l[id]=[]
        l[id].append(pf)
        with open('files/prefixes.json','w')as f:
            f.write(json.dumps(l))

    def remove_prefix(self,id,pf):
        with open('files/prefixes.json','r')as f:
            l = json.loads(f.read())
        del l[id][l[id].index(pf)]
        with open('files/prefixes.json','w')as f:
            f.write(json.dumps(l))


    
    @commands.command()
    async def prefix(self,ctx,do='',prfx=''):
        user=str(ctx.author.id)
        if do=='':
            e=discord.Embed(title="CUSTOM PREFIX",description=f"add : add a custom prefix\nremove : remove a custom prefix",color=0xFF0055)
            ypfx = ""
            all_pfx=self.get_prefix(str(ctx.author.id))
            if all_pfx==[]: ypfx = "<no prefix set>"
            for each in all_pfx:
                ypfx+=each+"\n"
            e.add_field(name="your prefixes",value=ypfx)
            await ctx.send(embed=e)
        elif do=='add' and prfx!='':
            self.add_prefix(user,prfx)
        elif do=='remove' and prfx!='':
            self.remove_prefix(user,prfx)




    
    @commands.command()
    async def afk(self,ctx,*,status=''):
        global data
        if status=='':status='No status set'
        self.load_afk()
        guild_id=str(ctx.guild.id)
        user=str(ctx.author.id)
        tag=guild_id+user
        data[tag]=[0,status]
        self.write_afk(data)
        #e=discord.Embed(title="AFK SET",description=f"{ctx.author.mention} is AFK\n{status}",color=0xFF0055)
        #await ctx.send(embed=e)
        msg=f"{ctx.author.mention} is AFK\n{status}"
        await ctx.send(msg)

             
        

    

def setup(bot):
    bot.add_cog(Message_Events(bot))
    print('---> MESSAGE EVENTS LOADED')
