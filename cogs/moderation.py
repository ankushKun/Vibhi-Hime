import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def warn(self,ctx,u:discord.User,*,reason):
        if ctx.author.id==666578281142812673:
            await ctx.message.delete()
            e=discord.Embed(title="",description=f"{u.mention} has been warned | {reason}",color=0xFF0000)
            await ctx.send(embed=e)
            await u.send(f"You were warned in {ctx.guild.name}\n reason : {reason}")
            


    @commands.command()
    async def announce(self,ctx,*,msg):
        if ctx.message.author.guild_permissions.administrator:
            m = ctx.guild.members
            for u in m:
                print(u)
                try:
                    if not u.bot:
                        await u.send(msg)
                except:
                    await ctx.send("could not to send to {}".format(u.mention))
        else :
            await ctx.send(f"{u.mention} you dont have perms, lol")
        
    @commands.command(aliases=['clear'])
    async def cls(self,ctx,l):
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                await ctx.channel.purge(limit=int(l)+1)
            except:
                await ctx.send("```n.cls <amount>```")
        else :
            await ctx.send(f"{ctx.message.author.mention} you dont have perms, lol")
        
    @commands.command()
    async def dm(self,ctx,u:discord.User,*,msg):
        if ctx.message.author.guild_permissions.administrator:
            try:
                await u.send(msg)
            except Exception as e:
                await ctx.send(f"could not to send to {u.mention}")
                await ctx.send(f"||{e}||")
        else:
            await ctx.send(f"{ctx.message.author.mention} you dont have perms, lol")
            
    @commands.command()
    async def ban(self,ctx,u:discord.User=None,reason=None):
        if ctx.message.author.guild_permissions.ban_members:
            if reason==None:
                reason="For being a jerk!"
            if u==None:
                await ctx.send(f"Who do you want to ban?")
                return
            try:
                await u.send(f'you have been banned from **{ctx.guild}**\nReason : **{reason}**')
                await ctx.guild.ban(u,delete_message_days = 0,reason=reason)
                await ctx.send(f"{u.mention} has been banned")
            except Exception as e:
                await ctx.send(f"```{e}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} you dont have the perms, lol")
        
    @commands.command()
    async def kickout(self,ctx,u:discord.User=None,reason=None):
        if ctx.message.author.guild_permissions.kick_members:
            if reason==None:
                reason="For being a jerk!"
            if u==None:
                await ctx.send(f"Who do you want to kick?")
                return
            try:
                await u.send(f'you have been kicked from **{ctx.guild}**\nReason : **{reason}**')
                await ctx.guild.kick(u,reason=reason)
                await ctx.send(f"{u.mention} has been kicked")
            except Exception as e:
                await ctx.send(f"```{e}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} you dont have the perms, lol")
        
        
    @commands.command()
    async def unban(self,ctx,member=None,reason=None):
        if ctx.message.author.guild_permissions.ban_members:
            if reason==None:
                reason="For being a good kid!"
            if member==None:
                await ctx.send(f"Who do you want to unban?\nType in their ``username#id``")
                return
            try:
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user,reason=reason)
                        await ctx.send(f"{user.mention} has been unbanned")
                        await user.send(f'you have been unbanned from **{ctx.guild}**\nReason : **{reason}**')
            except Exception as e:
                await ctx.send(f"```{e}```")
        else:
            await ctx.send(f"{ctx.message.author.mention} you dont have the perms, lol")
            
def setup(bot):
    bot.add_cog(Moderation(bot))
    print('---> MODERATION LOADED')
