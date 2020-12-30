import discord
from discord.ext import commands
import os
import praw
import random
from decouple import config
from bs4 import BeautifulSoup
import requests

reddit = praw.Reddit(client_id=config('REDDIT_CLIENT_ID'),client_secret=config('REDDIT_CLIENT_SECRET'),user_agent=config('REDDIT_USER_AGENT').replace('-',' '))

class Anime(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def anime(self,ctx):
        irl = reddit.subreddit('anime_irl')
        mem = reddit.subreddit('animememes')
        posts_irl = irl.new(limit=50)
        posts_mem = mem.new(limit=50)
        urls,u_titles = [],[]

        for m in posts_irl:
            urls.append(m.url)
            u_titles.append(m.title)

        for n in posts_mem:
            urls.append(n.url)
            u_titles.append(n.title)

        n=random.randint(0,len(urls))
        e=discord.Embed(title=u_titles[n],color=0xFF0055)
        e.set_image(url=urls[n])
        await ctx.send(embed=e)

    @commands.command()
    async def animegif(self,ctx):
        sr = reddit.subreddit('animegifs')
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
    async def anilist(self,ctx,*,uname=""):
        if uname=="":
            await ctx.send(f"{ctx.author.mention} you need to give a username `v!anilist <username>`")
            return
        URL = f"https://anilist.co/user/{uname}"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        stats = soup.findAll('div', attrs = {'class':'stat'})
        desc = ""
        for s in stats:
            label = s.find("div",attrs = {'class':'label'})
            value = s.find("div",attrs = {'class':'value'})
            desc+=f"**{label.text} : {value.text}**\n"
        if len(desc)==0:
            desc="Can't find that user, make sure you have given the correct display name."
        else:
            desc+=f"[Full Profile]({URL})"
        emb = discord.Embed(title=f"Anilist Stats for {uname}",description=desc,color=0xFF0055)
        await ctx.send(embed=emb)
        
    @commands.command()
    async def MAL(self,ctx,*,uname=""):
        if uname=="":
            await ctx.send(f"{ctx.author.mention} you need to give a username `v!MAL <username>`")
            return
        url = f"https://myanimelist.net/profile/{uname}"

        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content,"html5lib")

        total = soup.find_all("span",{"class":"di-ib fl-r"})
        score = soup.find_all("span",{"class":"score-label"})
        
        if len(total) == 0:
            dsc="Can't find that user, make sure you have given the correct username."
        else:
            dsc = f"""
**Total Anime : {total[0].text}
Episodes Watched : {total[2].text}
Mean Score : {score[0].text}
Manga Read : {total[3].text}
Chapters Read : {total[5].text}
Mean Score : {score[2].text}**
"""
            dsc += f"[Full Profile]({url})"
            
        emb = discord.Embed(title=f"MAL Stats for {uname}",description=dsc,color=0xFF0055)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Anime(bot))
    print('---> ANIME LOADED')
