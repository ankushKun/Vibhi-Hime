import discord
from discord.ext import commands
import wikipedia
from math import *
from io import StringIO
import sys
from ast import literal_eval
import requests
import random
from bs4 import BeautifulSoup
from disputils import BotEmbedPaginator


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(aliases=["im", "img", "pic"])
    async def image(self, ctx, *, msg):
        async with ctx.typing():
            query = msg
            url = f"https://www.google.co.in/search?q={query.replace(' ','+')}&source=lnms&tbm=isch&safe=active"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            images = []
            for img in soup.find_all("img"):
                images.append(img.get("src"))

            del images[0]
            url = random.choice(images)

            e = discord.Embed(
                title="Image Search",
                description=f'"{msg}" - requested by {ctx.author.mention}',
                color=0xFF0055,
            )
            e.set_image(url=url)
            await ctx.send(embed=e)

    @commands.command()
    async def wiki(self, ctx, *, msg):
        try:
            e = discord.Embed(
                title=msg,
                description=wikipedia.summary(msg, sentences=10),
                color=0xFF0055,
            )
            await ctx.send(embed=e)
        except wikipedia.exceptions.DisambiguationError as e:
            s = ""
            for i in e.options:
                s += i + "\n"
            em = discord.Embed(
                title="Error",
                description="Try Something from these\n" + s,
                color=0xFF0055,
            )
            await ctx.send(embed=em)
        except Exception as e:
            em = discord.Embed(
                title="Error",
                description="Could not find what you are looking for",
                color=0xFF0055,
            )
            em.add_field(name=str(e))
            await ctx.send(embed=em)

    @commands.command()
    async def stats(self, ctx):
        emb = discord.Embed(title="**Vibhi STATS**", color=0xFF0055)
        mc = 0
        for s in self.bot.guilds:
            mc += s.member_count
        emb.add_field(
            name="Total Servers", value=str(len(self.bot.guilds)), inline=False
        )
        emb.add_field(name="Total Members", value=str(mc), inline=False)
        emb.add_field(
            name="Latency(s)",
            value=str(round(self.bot.latency, 3) * 1000),
            inline=False,
        )
        emb.add_field(
            name=f"{ctx.guild} members", value=f"{ctx.guild.member_count}", inline=False
        )
        await ctx.send(embed=emb)

    @commands.is_owner()
    @commands.command()
    async def servers(self, ctx):
        server_per_page = 20
        svr = self.bot.guilds
        mem_count = 0
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
                    mem_count += svr[j].member_count
                except:
                    break
                j += 1
            embeds.append(emb)

        front = discord.Embed(
            title=f"**Vibhi Server Stats**",
            description=f"Total Servers : **{len(svr)}**\nTotal members : **{mem_count}**\n\ndisplaying 20 servers per page",
            color=0xFF0055,
        )
        embeds = [front] + embeds
        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


def setup(bot):
    bot.add_cog(Utility(bot))
    print("---> UTILITY LOADED")
