import discord
from discord import message
from discord.ext import commands
import os
import random
from PIL import Image, ImageSequence
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
    
    @commands.command(aliases=['bn', 'bnr'])
    async def banner(self, ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        req = await self.client.http.request(discord.http.Route("GET", "/users/{uid}", uid=mem.id))
        banner_id = req["banner"]
        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{mem.id}/{banner_id}?size=1024"
        response = requests.get(banner_url)
        img = Image.open(BytesIO(response.content))
        if img.is_animated == True:
            emb = discord.Embed(color=0x2e69f2)
            framess = [frame.copy() for frame in ImageSequence.Iterator(img)]
            framess[0].save('banner.gif',
                            save_all=True, append_images=framess[1:],
                            optimize=False, duration=100, loop=0)
            file = discord.File("banner.gif")
            emb.set_image(url="attachment://banner.gif")
            #emb.set_footer(
                #text=f"Kanna Chan",
                #icon_url=kana.avatar_url,
            #)
            await ctx.send(embed=emb, file=file)
        else:
            emb = discord.Embed(color=0xFF0055)
            img.save("banner.png")
            file = discord.File("banner.png")
            emb.set_image(url="attachment://banner.png")
            #emb.set_footer(
                #text=f"Kanna Chan",
                #icon_url=kana.avatar_url,
            #)
            await ctx.send(embed=emb, file=file)
    
    @commands.command(aliases=["av", "avatar"])
    async def pfp(self, ctx):
        members = ctx.message.mentions
        if members == []:
            members = [ctx.author]
        if len(members) == 1:
            emb = discord.Embed(title="", description=f"", color=0xFF0055)
            emb.set_image(url=members[0].avatar_url)
            await ctx.send(embed=emb)
            return

        animated = []
        for m in members:
            animated.append(m.is_avatar_animated())

        imgs = []
        for mem in members:
            url = requests.get(mem.avatar_url)
            im = Image.open(BytesIO(url.content))
            imgs.append(im)

        s = len(imgs)
        # print(animated)
        all_animated = all(animated)
        all_not_animated = not any(animated)
        # print(all_animated, all_not_animated)
        if all_animated:  ############ ANIMATED ############
            frames = []

            s = len(imgs)
            print("S", s)
            d = 250
            bg = Image.new(mode="RGBA", size=(d * s, d))

            for gif in imgs:
                f = []
                while True:
                    try:
                        gif.seek(gif.tell() + 1)
                        f.append(gif.copy().resize((d, d)))
                    except Exception as e:
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
            # print(frames_imgs)
            if frames_imgs == []:
                frames_imgs = imgs

            # print(frames_imgs)
            frames_imgs[0].save(
                f"images/generated/{ctx.author.id}.gif",
                save_all=True,
                append_images=frames_imgs[:],
                loop=0,
                quality=1,
            )
            file = discord.File(
                f"images/generated/{ctx.author.id}.gif", filename="pic.gif"
            )
            emb = discord.Embed(title="", description=f"", color=0xFF0055)
            emb.set_image(url="attachment://pic.gif")
        else:
            s = len(imgs)
            bg = Image.new(mode="RGBA", size=(500 * s, 500))
            i = 0
            for x in range(0, s):
                try:
                    bg.paste(imgs[i].resize((500, 500)), (500 * x, 0))
                    i += 1
                except Exception as e:
                    print(e, i)
                    pass
            bg.save(f"images/generated/{ctx.author.id}.png", quality=10)
            file = discord.File(
                f"images/generated/{ctx.author.id}.png", filename="pic.jpg"
            )
            emb = discord.Embed(title="", description=f"", color=0xFF0055)
            emb.set_image(url="attachment://pic.jpg")

        await ctx.send(file=file, embed=emb)
        # await ctx.send(file=file)
        os.system(f"rm -rf images/generated/{ctx.author.id}.gif")
        os.system(f"rm -rf images/generated/{ctx.author.id}.png")

    @commands.command()
    async def patgif(self, ctx):
        avatar = ctx.author.avatar_url
        if len(ctx.message.mentions) > 0:
            avatar = ctx.message.mentions[0].avatar_url

        i1 = requests.get(avatar)
        im1 = Image.open(BytesIO(i1.content)).resize((500, 500)).convert("RGBA")

        pat_gif = Image.open("images/pat.gif")
        pat_frames = []

        d = 500
        y_pos = [100, 110, 120, 130, 140, 130, 120, 110, 100]

        while True:
            try:
                pat_gif.seek(pat_gif.tell() + 1)
                f = pat_gif.copy().resize((d, d)).convert("RGBA")
                pat_frames.append(f)
            except:
                break

        print(len(pat_frames))

        final_frames = []

        p = 0
        for y in y_pos:
            blank = Image.new("RGBA", (500, 500))
            blank.paste(im1.resize((400, 500 - y)), (100, y))  # pastes avatar
            blank.paste(pat_frames[p], (0, 0), pat_frames[p])
            final_frames.append(blank)
            p += 1

        final_frames[0].save(
            f"images/generated/{ctx.author.id}.gif",
            type="GIF",
            save_all=True,
            append_images=final_frames[:],
            loop=0,
            quality=1,
            duration=pat_gif.info["duration"],
            format="GIF",
        )
        file = discord.File(f"images/generated/{ctx.author.id}.gif", filename="pic.gif")
        await ctx.send(file=file)
        os.system(f"rm -rf images/generated/{ctx.author.id}.gif")

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
