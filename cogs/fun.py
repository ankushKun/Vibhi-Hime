import discord
from discord.ext import commands
import random
import praw
from prawcore import NotFound
from decouple import config
import requests
import json
from PIL import Image,ImageDraw,ImageFont
import requests
from io import BytesIO
import os

reddit = praw.Reddit(client_id=config('REDDIT_CLIENT_ID'),client_secret=config('REDDIT_CLIENT_SECRET'),user_agent=config('REDDIT_USER_AGENT').replace('-',' '))

API_KEY = config("TENOR_KEY")
r = requests.get(f"https://api.tenor.com/v1/anonid?&key={API_KEY}")

deletable_messages=[]

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def gif(self,ctx):
        q=ctx.message.content[5:]
        # set the apikey and limit
        apikey = config("TENOR_KEY")  # test value
        lmt = 10

        # our test search
        search_term = q

        # get the top 8 GIFs for the search term
        r = requests.get(
            f"https://api.tenor.com/v1/search?q={search_term}&key={apikey}&limit={str(lmt)}&contentfilter=medium&media_filter=minimal")

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            tenorjson = json.loads(r.content)
            urls=[]
            for i in range(len(tenorjson["results"])):
                url = tenorjson["results"][i]["media"][0]["tinygif"]["url"]

                urls.append(url)
            if urls==[]:
                await ctx.send(f"can't find any gifs related to {search_term}")
                return
            gif_msg = await ctx.send(random.choice(urls))
            #await gif_msg.add_reaction('🗑️')
            deletable_messages.append(gif_msg.id)
        else:
            tenorjson = None


    @commands.command()
    async def meme(self,ctx):
        sr = reddit.subreddit('memes')
        posts = sr.new(limit=100)
        urls,u_titles = [],[]

        for m in posts:
            urls.append(m.url)
            u_titles.append(m.title)

        n=random.randint(0,len(urls))
        e=discord.Embed(title=u_titles[n],color=0xFF0055)
        e.set_image(url=urls[n])
        await ctx.send(embed=e)

    @commands.command()
    async def reddit(self,ctx,*,sr):
        def sub_exists(sub):
            exists = True
            try:
                reddit.subreddits.search_by_name(sub, exact=True)
            except NotFound:
                exists = False
            return exists
        async with ctx.typing():
            if sub_exists(sr):
                sr = reddit.subreddit(sr)
                if not sr.over18:
                    posts = sr.new(limit=100)
                    urls,u_titles = [],[]

                    for m in posts:
                        urls.append(m.url)
                        u_titles.append(m.title)

                    n=random.randint(0,len(urls))
                    e=discord.Embed(title=u_titles[n],color=0xFF0055)
                    e.set_image(url=urls[n])
                    post = await ctx.send(embed=e)
                    #await post.add_reaction('🗑️')
                    deletable_messages.append(post.id)
                    return
                else:
                    await ctx.send("Use that in an NSFW channel >_<")
            else:
                await ctx.send("That subreddit doesnot exist :(")
                return


    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction):
        if reaction.message_id in deletable_messages and reaction.emoji.name == '🗑️' and not reaction.member.bot:
            await self.bot.http.delete_message(reaction.channel_id, reaction.message_id)
            deletable_messages.remove(reaction.message_id)


    @commands.command()
    async def pun(self,ctx):
        pun = requests.get('https://sv443.net/jokeapi/v2/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt')
        if pun.status_code == 200:
            e = discord.Embed(title=str(pun.content.decode('utf-8')),color=0xFF0055)
            await ctx.send(embed=e)
        else:
            await ctx.send(f'```Error : {pun.status_code}```')

    @commands.command()
    async def joke(self,ctx):
        jk = requests.get('https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt')
        if jk.status_code == 200:
            e = discord.Embed(title=str(jk.content.decode('utf-8')),color=0xFF0055)
            await ctx.send(embed=e)
        else:
            await ctx.send(f'```Error : {jk.status_code}```')


    @commands.command()
    async def nuke(self,ctx,*,msg=''):
        e=discord.Embed(title="",description=f'{ctx.author.mention} NUKES {msg}',color=0xFF0055)
        e.set_image(url="https://i.pinimg.com/originals/47/12/89/471289cde2490c80f60d5e85bcdfb6da.gif")
        await ctx.send(embed=e)

    @commands.command()
    async def ship(self,ctx, m1:discord.User=None, m2:discord.User=None):
        def center_text(img, font, text):
            strip_width, strip_height = 2560, 1261
            draw = ImageDraw.Draw(img)
            text_width, text_height = draw.textsize(text, font)
            position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
            draw.text(position, text, (255, 255, 255), font=font)
            return img
        if m1==None:
            m1=ctx.author
            m2=ctx.author
        elif m2==None:
            m2=m1
            m1=ctx.author
        perc = random.randint(0,101)
        u1r = requests.get(m1.avatar_url)
        u1img = Image.open(BytesIO(u1r.content)).resize((1000,1000))
        u2r = requests.get(m2.avatar_url)
        u2img = Image.open(BytesIO(u2r.content)).resize((1000,1000))
        bg = Image.open('images/bg.png')
        y=130
        x=130
        bg.paste(u1img,(x,y))
        bg.paste(u2img,(x+1280,y))
        fnt = ImageFont.truetype("files/font.ttf", 80)
        bg = center_text(bg,fnt,f"{perc}%")
        bg.save(f'images/generated/{ctx.author.id}.png',quality=40)
        file = discord.File(f"images/generated/{ctx.author.id}.png",filename='pic.jpg')
        emb=discord.Embed(title="",description=f"{m1.mention} x {m2.mention}",color=0xFF0055)
        emb.set_image(url="attachment://pic.jpg")
        await ctx.send(file=file, embed=emb)
        os.system(f"rm -rf images/generated/{ctx.author.id}.png")


def setup(bot):
    bot.add_cog(Fun(bot))
    print('---> FUN LOADED')
