import discord
from discord.ext import commands
import os
from disputils import BotEmbedPaginator
import random 



class Misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    	
    @commands.command()
    async def pfp(self,ctx, mn:discord.User=None):
        if mn==None:
            mn=ctx.author
        p_emb = discord.Embed(title=" ", description="{}".format(mn.mention),color=0xFF0055)
        p_emb.set_image(url=mn.avatar_url)
        await ctx.send(embed=p_emb)
  
    @commands.command()
    async def say(self,ctx):
        print(ctx.message.content)
        if "everyone" in ctx.message.content or "here" in ctx.message.content:
            await ctx.send(random.choice(["bruh, I'm not gonna ping everyone","You bad human, dont ping everyone!","no","I'm not your waifu anymore"]))
        else:
            await ctx.send(ctx.message.content[5:])
            await ctx.message.delete()
    
    @commands.command()
    async def invite(self,ctx):
        emb=discord.Embed(title='INVITE **Vibhi**',color=0xFF0055)
        inv='[Invite link](https://discord.com/api/oauth2/authorize?client_id=745167619253993543&permissions=536472918&scope=bot)'
        emb.add_field(name="direct invite ",value=inv,inline=False)
        await ctx.send(embed=emb)

    @commands.command()
    async def stats(self,ctx):
        emb = discord.Embed(title="**Vibhi STATS**",color=0xFF0055)
        emb.add_field(name="Total Servers",value=str(len(self.bot.guilds)),inline=False)
        emb.add_field(name="Latency(ms)",value=str(round(self.bot.latency,1)),inline=False)
        emb.add_field(name=f"{ctx.guild} members",value=f'{ctx.guild.member_count}',inline=False)
        await ctx.send(embed=emb)
        
        
    @commands.command()
    async def servers(self,ctx):
        server_per_page=5
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
        
    @commands.command()
    async def updategif(self,ctx):
        try:
            os.system('git clone https://github.com/ATCtech/anime-rp-gifs.git')
            os.system('cd anime-rp-gifs')
            os.system('git pull https://github.com/ATCtech/anime-rp-gifs.git')
            os.system('cd ..')

            await ctx.send('OwO new Gifs')
        except Exception as e:
            await ctx.send(f'```ERROR\n{e}```')
        
    
    

def setup(bot):
    bot.add_cog(Misc(bot))
    print('---> MISC LOADED')

