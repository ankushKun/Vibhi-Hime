import discord
from discord.ext import commands
from random import choice
import requests
import json
#import urllib
from os import chdir, getcwd, mkdir
import os.path
from os import path
from decouple import config
import pyrebase

firebase = pyrebase.initialize_app(json.loads(config("FIREBASE")))
db=firebase.database()

class Rp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def get_prefix(self,uid):
        pfxs=db.child("PREFIX").child(uid).get().val()
        if pfxs==None:pfxs=[]
        return pfxs
            
    @commands.Cog.listener()
    async def on_message(self,msg):
        user=str(msg.author.id)
        prefixes = self.get_prefix(user)
        newmsg=msg.content
        for pfix in prefixes:
            if msg.content.startswith(pfix):
                newmsg = msg.content.replace(pfix,'v!').replace('v! ','v!')
                
        ms= newmsg.lower()
        ms+=' '
        if 'v!' in ms:
            ms=ms[2:]
            
            rpname=ms[:ms.index(' ')]
            rps=db.child("RP").child("GIF").get().val()
            
            action='s'
            rp=rpname
            if rpname=='sad': rp,action='is sad',' '
            elif rpname=='sleepy': rp,action='is sleepy',' '
            elif rpname=='money': rp,action='dreams about money',' '
            elif rpname=='scared': rp,action='is scared',' '
            elif rpname=='happy': rp,action='is happy',' '
            elif rpname=='delighted': rp,action='is delighted',' '
            elif rpname=='angry': rp,action='is angry',' '
            elif rpname=='lewd': rp,action='is being lewd',' '
            elif rpname=='cute': rp,action='is cute',' '
            elif rpname=='nervous': rp,action='is nervous',' '
            elif rpname.endswith('s') or rpname.endswith('h'):action='es'
            elif rpname.endswith('y'):
                action='ies'
                rp=rpname[:-1]
            
            if rpname in rps:
                gif = choice(rps[rpname][:-1])
                em = discord.Embed(title='',description=f'{msg.author.mention} {rp}{action}{ms[ms.index(" "):]}',color=0xFF0055)
                em.set_image(url=gif)
                await msg.channel.send(embed=em)

    @commands.command()
    async def updaterp(self,ctx,amt=5):
        if ctx.author.id == 666578281142812673:
            API_KEY = config("TENOR_KEY")
            r = requests.get(f"https://api.tenor.com/v1/anonid?&key={API_KEY}")
            rp = db.child("RP").child("CMD").get().val()
            await ctx.send('> updating all RP gifs ...')
            
            
            if r.status_code == 200:
                with open("anon_id.txt", "a+") as f:
                    if f.read() == "":
                        r = requests.get(f"https://api.tenor.com/v1/anonid?&key={API_KEY}")
                        anon_id = json.loads(r.content)["anon_id"]
                        f.write(anon_id)
                    else:
                        anon_id = f.read()
                        mkdir("media")
            else:
                await ctx.send("Failed Connection, Please try again")
                return

            #chdir(getcwd() + "\\media")
            for rp_c in rp:
                limit = amt
                search_term = rp_c
                filetype = "gif"

                if filetype ==  "h":
                    print("Currently supported filetypes:")
                    print("-gif")
                    print("-mp4")
                    print("-webm")
                    
                    filetype = input("Filetype: ")
                search="anime "+search_term
                r = requests.get(f"https://api.tenor.com/v1/search?q={search}&key={API_KEY}&limit={limit}&anon_id={anon_id}")

                if r.status_code == 200:
                    tenorjson = json.loads(r.content)
                    l=""
                    for i in range(len(tenorjson["results"])):
                        url = tenorjson["results"][i]["media"][0][filetype]["url"]
                        l+=url+"\n"
                    l=l.split("\n")
                    db.child("RP").child("GIF").child(search_term.replace(" ","-")).set(l)
                    


                else:
                    tenorjson = None
                    await ctx.send("Failed connection Please Try Again")
                    continue
                
                #await ctx.send(f"``{search_term} updated``")
                continue
                
                if input("Would you like to download any more files[Y or N]: ").upper() == "Y":
                    continue
                else:
                    #print("Thank you for using TenorDownloader.py")
                    break    
            await ctx.send('OwO new gifs')         
        else :
            print(f"{ctx.author.name}({ctx.author.id}) tried to use updategif command")
            
            
            
    @commands.command(aliases=['rp'])
    async def roleplay(self,ctx):
        rolepl=""
        for each in db.child("RP").child("GIF").get().val():
            rolepl+="\n"+each
        e=discord.Embed(title="Roleplay commands",description=f"{rolepl}",color=0xFF0055)
        await ctx.send(embed=e)
    
    @commands.command()
    async def addrp(self,ctx,*,cmd):
        if ctx.author.id == 666578281142812673:
            cmd=cmd.replace(" ","-")
            rp_cmd=db.child("RP").child("CMD").get().val()
            rp_cmd.append(cmd)
            db.child("RP").child("CMD").set(rp_cmd)
            await ctx.send(f"> {cmd} was added")
        else :
            print(f"{ctx.author.name}({ctx.author.id}) tried to use addrp command")
    @commands.command()
    async def remrp(self,ctx,*,cmd):
        if ctx.author.id == 666578281142812673:
            cmd=cmd.replace(" ","-")
            rp_cmd=db.child("RP").child("CMD").get().val()
            del rp_cmd[rp_cmd.index(cmd)]
            db.child("RP").child("CMD").set(rp_cmd)
            db.child("RP").child("GIF").child(cmd).remove()
            await ctx.send(f'> {cmd} was removed')
        else:
            print(f"{ctx.author.name}({ctx.author.id}) tried to use remrp command")

def setup(bot):
    bot.add_cog(Rp(bot))
    print('---> ROLEPLAY LOADED')
