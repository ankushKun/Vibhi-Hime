import discord
from discord.ext import commands
import os
from disputils import BotEmbedPaginator
import random
from PIL import Image
import requests
from io import BytesIO
from math import *


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """ #matrix
    @commands.command(aliases=["av","avatar"])
    async def pfp(self,ctx):
        members=ctx.message.mentions
        if members==[]:members=[ctx.author]
        imgs=[]
        
        for mem in members:
            url = requests.get(mem.avatar_url)
            im = Image.open(BytesIO(url.content)).resize((500,500))
            imgs.append(im)
        s = ceil(len(members)/2)
        if len(members)==2:s+=2
        print(s)
        i=0
        bg = Image.new(mode = "RGBA", size = (500*s, 500*s))
        for y in range(0,s):
            for x in range(0,s):
                try:
                    bg.paste(imgs[i],(500*x,500*y))
                    i+=1
                except Exception as e:
                    print(e,i)
                    pass
        print(x,y)
        imageBox = bg.getbbox()
        bg=bg.crop(imageBox)
        bg.save(f'images/generated/{ctx.author.id}.png',quality=10)
        file = discord.File(f"images/generated/{ctx.author.id}.png",filename='pic.jpg')
        emb=discord.Embed(title="",description=f"",color=0xFF0055)
        emb.set_image(url="attachment://pic.jpg")
        await ctx.send(file=file, embed=emb)
        #await ctx.send(file=file)
        os.system(f"rm -rf images/generated/{ctx.author.id}.png")
    """

    @commands.command(aliases=["av", "avatar"])
    async def pfp(self, ctx):
        members = ctx.message.mentions
        if members == []:
            members = [ctx.author]
        imgs = []
        for mem in members:
            url = requests.get(mem.avatar_url)
            im = Image.open(BytesIO(url.content))
            imgs.append(im)

        frames = []

        s = len(imgs)
        d = 250
        bg = Image.new(mode="RGBA", size=(d * s, d))

        for gif in imgs:
            f = []
            while True:
                try:
                    gif.seek(gif.tell() + 1)
                    f.append(gif.copy().resize((d, d)))
                except:
                    frames.append(f)
                    break

        frames_imgs = []
        s = len(frames)
        f_no = 0
        while True:
            i = 0
            brk = False
            bg = Image.new(mode="RGBA", size=(d * s, d))
            for x in range(0, s):
                try:
                    bg.paste(frames[i][f_no], (d * x, 0))
                    i += 1
                    frames_imgs.append(bg)
                except Exception as e:
                    print(e, i)
                    brk = True
            f_no += 1
            if brk:
                break

        if frames_imgs == []:
            frames_imgs = imgs

        # print(frames_imgs)
        frames_imgs[0].save(
            f"images/generated/{ctx.author.id}.gif",
            save_all=True,
            append_images=frames_imgs,
            loop=0,
            quality=1,
        )

        file = discord.File(f"images/generated/{ctx.author.id}.gif", filename="pic.gif")
        emb = discord.Embed(title="", description=f"", color=0xFF0055)
        emb.set_image(url="attachment://pic.gif")
        await ctx.send(file=file, embed=emb)
        # await ctx.send(file=file)
        os.system(f"rm -rf images/generated/{ctx.author.id}.gif")

    @commands.command()
    async def say(self, ctx):
        if ctx.author.id == 666578281142812673:
            await ctx.send(ctx.message.content[5:])
            await ctx.message.delete()

    @commands.command()
    async def invite(self, ctx):
        emb = discord.Embed(title="INVITE **Vibhi**", color=0xFF0055)
        inv = "[Invite link](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)"
        emb.add_field(name="direct invite ", value=inv, inline=False)
        await ctx.send(embed=emb)

    @commands.command()
    async def stats(self, ctx):
        emb = discord.Embed(title="**Vibhi STATS**", color=0xFF0055)
        emb.add_field(
            name="Total Servers", value=str(len(self.bot.guilds)), inline=False
        )
        emb.add_field(
            name="Latency(s)", value=str(round(self.bot.latency, 3)), inline=False
        )
        emb.add_field(
            name=f"{ctx.guild} members", value=f"{ctx.guild.member_count}", inline=False
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def servers(self, ctx):
        server_per_page = 10
        svr = self.bot.guilds
        embeds = []
        for i in range(0, len(svr), server_per_page):
            emb = discord.Embed(title=f"**Vibhi SERVERS [{len(svr)}]**", color=0xFF0055)
            j = i
            while j < i + server_per_page:
                try:
                    emb.add_field(
                        name=svr[j],
                        value=f"members : {svr[j].member_count}",
                        inline=False,
                    )
                except:
                    break
                j += 1
            embeds.append(emb)

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

    # @commands.command()
    async def pfpall(self, ctx):
        mem = ctx.guild.members
        members = []
        for mbr in mem:
            if mbr.bot == False:
                members.append(mbr)
        print(members)
        # return
        l = len(members)
        msg = await ctx.send(f"In progress ({l})")
        s = ceil(len(members) / 4)
        if len(members) == 2:
            s += 2
        print(s)
        i = 0
        bg = Image.new(mode="RGBA", size=(100 * s, 100 * s))
        for y in range(0, s):
            for x in range(0, s):
                try:
                    url = requests.get(members[i].avatar_url)
                    im = Image.open(BytesIO(url.content)).resize((100, 100))
                    bg.paste(im, (100 * x, 100 * y))
                    if i % 10 == 0:
                        print(i)  # await msg.edit(content=f"In progress `({i}/{l})`")
                    i += 1
                except Exception as e:
                    print(e, i)
                    break
        print(x, y)
        imageBox = bg.getbbox()
        bg = bg.crop(imageBox)
        bg.save(f"images/generated/{ctx.author.id}.png", quality=5)
        file = discord.File(f"images/generated/{ctx.author.id}.png", filename="pic.jpg")
        await ctx.send(file=file)
        # await ctx.send(file=file)
        os.system(f"rm -rf images/generated/{ctx.author.id}.png")


def setup(bot):
    bot.add_cog(Misc(bot))
    print("---> MISC LOADED")
