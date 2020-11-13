import discord
from discord.ext import commands
import os
from disputils import BotEmbedPaginator
import random
from PIL import Image
import requests
from io import BytesIO


class Misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(aliases=["av","avatar"])
    async def pfp(self,ctx, m1:discord.User=None, m2:discord.User=None):
        if m2==None:
            if m1==None:
                m1=ctx.author
            p_emb = discord.Embed(title=" ", description="{}".format(m1.mention),color=0xFF0055)
            p_emb.set_image(url=m1.avatar_url)
            #await ctx.send(embed=p_emb)
            await ctx.send(m1.avatar_url)
        else: # TRYING TO SHOW TWO AVATARS TOGETHER
            u1r = requests.get(m1.avatar_url)
            u1img = Image.open(BytesIO(u1r.content)).resize((1240,1240))
            u2r = requests.get(m2.avatar_url)
            u2img = Image.open(BytesIO(u2r.content)).resize((1240,1240))
            bg = Image.open('images/bg.png')
            y=10
            x=20
            bg.paste(u1img,(x,y))
            bg.paste(u2img,(x+1280,y))
            bg.save(f'images/generated/{ctx.author.id}.png',quality=40)
            file = discord.File(f"images/generated/{ctx.author.id}.png",filename='pic.jpg')
            emb=discord.Embed(title="",description=f"{m1.mention} x {m2.mention}",color=0xFF0055)
            emb.set_image(url="attachment://pic.jpg")
            #await ctx.send(file=file, embed=emb)
            await ctx.send(file=file)
            os.system(f"rm -rf images/generated/{ctx.author.id}.png")

    @commands.command()
    async def say(self,ctx):
        print(ctx.message.content)
        if "everyone" in ctx.message.content or "here" in ctx.message.content:
            await ctx.send(random.choice(["bruh, I'm not gonna ping everyone","You bad human, dont ping everyone!","no","I'm not your waifu anymore"]))
        else:
            #await ctx.send(ctx.message.content[5:])
            #await ctx.message.delete()
            pass

    @commands.command()
    async def invite(self,ctx):
        emb=discord.Embed(title='INVITE **Vibhi**',color=0xFF0055)
        inv='[Invite link](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)'
        emb.add_field(name="direct invite ",value=inv,inline=False)
        await ctx.send(embed=emb)

    @commands.command()
    async def stats(self,ctx):
        emb = discord.Embed(title="**Vibhi STATS**",color=0xFF0055)
        emb.add_field(name="Total Servers",value=str(len(self.bot.guilds)),inline=False)
        emb.add_field(name="Latency(s)",value=str(round(self.bot.latency,3)),inline=False)
        emb.add_field(name=f"{ctx.guild} members",value=f'{ctx.guild.member_count}',inline=False)
        await ctx.send(embed=emb)


    @commands.command()
    async def servers(self,ctx):
        server_per_page=10
        svr = self.bot.guilds
        embeds=[]
        for i in range(0,len(svr),server_per_page):
            emb = discord.Embed(title=f"**Vibhi SERVERS [{len(svr)}]**",color=0xFF0055)
            j=i
            while j<i+server_per_page:
                try:
                    emb.add_field(name=svr[j],value=f'members : {svr[j].member_count}',inline=False)
                except:
                    break
                j+=1
            embeds.append(emb)

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()









def setup(bot):
    bot.add_cog(Misc(bot))
    print('---> MISC LOADED')
