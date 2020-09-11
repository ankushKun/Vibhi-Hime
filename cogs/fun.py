import discord
from discord.ext import commands
import random
import praw
from decouple import config
import requests
import json

reddit = praw.Reddit(client_id=config('REDDIT_CLIENT_ID'),client_secret=config('REDDIT_CLIENT_SECRET'),user_agent=config('REDDIT_USER_AGENT').replace('-',' '))

API_KEY = config("TENOR_KEY")
r = requests.get(f"https://api.tenor.com/v1/anonid?&key={API_KEY}")

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
            await ctx.send(random.choice(urls))
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
        e=discord.Embed(title=u_titles[n])
        e.set_image(url=urls[n])
        await ctx.send(embed=e)

    @commands.command()
    async def ask(self,ctx):
        response =['Yes of Course','Oh Yeah','Yep','Without a doubt',
                   'Nopee','Noooooo','Nuo','Na','-_-',
                   'idk','I cant tell now','How should I know','meh','that was a shitty question','']
        await ctx.send(random.choice(response))
        
        
    
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

def setup(bot):
    bot.add_cog(Fun(bot))
    print('---> FUN LOADED')
