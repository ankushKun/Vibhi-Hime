import discord
from discord.ext import commands
import os
import json
import pyrebase
from decouple import config

firebase = pyrebase.initialize_app(json.loads(config("FIREBASE")))
db=firebase.database()


class Message_Events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    
    def afk_exists(self,uid):
        try:
            return uid in db.child("AFK").get().val()
        except Exception as e:
            pass
        
    
    def remove_afk(self,uid):
        if self.afk_exists(uid):
            db.child("AFK").child(uid).remove()
            
        

    def set_afk(self,uid,data):
        db.child("AFK").child(uid).set(data)
        
    def get_info(self,uid):
        if self.afk_exists(uid):
            d=db.child("AFK").child(uid).get().val()
            return d
        else: return [-1,"error"]

    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author.bot:return
        ms=msg.content
        if not ms.lower().startswith('v!afk'):
            guild_id=str(msg.guild.id)
            user_id=str(msg.author.id)
            tag=guild_id+user_id
            if self.afk_exists(tag):
                data=self.get_info(tag)
                self.remove_afk(tag)
                no_more_afk=f"welcome back {msg.author.mention}.\n__{data[1]}__.\nYou were pinged __{data[0]}__ times."
                await msg.channel.send(no_more_afk)
                # remove afk here
        for ping in msg.mentions:
            guild_id=str(msg.guild.id)
            user_id=str(ping.id)
            tag=guild_id+user_id
            if self.afk_exists(tag):
                data=self.get_info(tag)
                data[0]+=1
                self.set_afk(tag,data)
                msg_afk=f"**{ping.display_name}** is AFK\n\n{data[1]}"
                await msg.channel.send(msg_afk)
        user=str(msg.author.id)
        prefixes = self.get_prefix(user)
        for pfix in prefixes:
            print(msg.content)
            if msg.content.startswith(pfix):
                msg.content = msg.content.replace(pfix,'v!').replace('v! ','v!')
                await self.bot.process_commands(msg)
                

    def get_prefix(self,uid):
        pfxs=db.child("PREFIX").child(uid).get().val()
        if pfxs==None:pfxs=[]
        return list(pfxs)

    def add_prefix(self,uid,pf):
        pfxs=db.child("PREFIX").child(uid).get().val()
        if pfxs==None:pfxs=[]
        pfxs.append(pf)
        db.child("PREFIX").child(uid).set(pfxs)
        

    def remove_prefix(self,uid,pf):
        pfxs=db.child("PREFIX").child(uid).get().val()
        if pfxs==None:pfxs=[]
        else:del pfxs[pfxs.index(pf)]
        db.child("PREFIX").child(uid).set(pfxs)


    
    @commands.command()
    async def prefix(self,ctx,do='',prfx=''):
        user=str(ctx.author.id)
        
        if do=='add' and prfx!='':
            self.add_prefix(user,prfx)
            await ctx.send(f"> added custom prefix - {prfx}")
        elif do=='remove' and prfx!='':
            self.remove_prefix(user,prfx)
            await ctx.send(f"> removed custom prefix - {prfx}")
        else:
            e=discord.Embed(title="CUSTOM PREFIX",description=f"add : add a custom prefix\nremove : remove a custom prefix",color=0xFF0055)
            ypfx = ""
            all_pfx=self.get_prefix(str(ctx.author.id))
            if all_pfx==[]: ypfx = "<no prefix set>"
            for each in all_pfx:
                ypfx+=each+"\n"
            e.add_field(name="your prefixes",value=ypfx)
            await ctx.send(embed=e)




    
    @commands.command()
    async def afk(self,ctx,*,status=' '):
        guild_id=str(ctx.guild.id)
        user=str(ctx.author.id)
        tag=guild_id+user
        data=[0,status]
        self.set_afk(tag,data)
        #e=discord.Embed(title="AFK SET",description=f"{ctx.author.mention} is AFK\n{status}",color=0xFF0055)
        #await ctx.send(embed=e)
        msg=f"{ctx.author.mention} is AFK\n{status}"
        await ctx.send(msg)

             
        

    

def setup(bot):
    bot.add_cog(Message_Events(bot))
    print('---> MESSAGE EVENTS LOADED')
