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



class Rp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def get_prefix(self,id):
        try:
            with open('files/prefixes.json','r')as f:
                l= json.loads(f.read())
                if id in l:
                    return l[id]
                else: return []
        except:
            pass
            
    @commands.Cog.listener()
    async def on_message(self,msg):
        user=str(msg.author.id)
        prefixes = self.get_prefix(user)
        for pfix in prefixes:
            if msg.content.startswith(pfix):
                msg.content = msg.content.replace(pfix,'v!').replace('v! ','v!')
                #await self.bot.process_commands(msg)
        ms= msg.content.lower()
        ms+=' '
        if 'v!' in ms:
            ms=ms[2:]
            d = os.listdir('./files/rp/')
            filename=ms[:ms.index(' ')]+".txt"
            if filename in d:
                with open(f'./files/rp/{filename}','r') as f:
                    urls=f.read().split('\n')
                gif=choice(urls[:-1])
                em = discord.Embed(title='',description=f'{msg.author.mention} {ms[:ms.index(" ")]}s{ms[ms.index(" "):]}',color=0xFF0055)
                em.set_image(url=gif)
                await msg.channel.send(embed=em)
           

    @commands.command()
    async def updaterp(self,ctx,amt=5):
        if ctx.author.id == 666578281142812673:
            
            API_KEY = config("TENOR_KEY")

            r = requests.get(f"https://api.tenor.com/v1/anonid?&key={API_KEY}")
            
            with open('files/rp_cmd.txt','r') as f:
                rp=f.read().split('\n')
            await ctx.send('updating all ...')
            
            
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
                        
                    if not path.isdir('files'): os.system('mkdir files')
                    if not path.isdir('files/rp'): os.system('mkdir files/rp')
                    with open(f'./files/rp/{search_term.replace(" ","-")}.txt','w') as f:f.write(l)


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
        try:
            d = os.listdir('./files/rp')
            for c in d:
                rolepl+="\n"+c.replace('.txt','')
        except:
            pass
        e=discord.Embed(title="Roleplay commands",description=f"{rolepl}",color=0xFF0055)
        await ctx.send(embed=e)
    
    @commands.command()
    async def addrp(self,ctx,*,cmd):
        if ctx.author.id == 666578281142812673:
            with open('files/rp_cmd.txt','a') as f:
                f.write("\n"+cmd)
                await ctx.send(f'> added {cmd}')
        else :
            print(f"{ctx.author.name}({ctx.author.id}) tried to use addrp command")
    @commands.command()
    async def remrp(self,ctx,*,cmd):
        if ctx.author.id == 666578281142812673:
            os.system(f'rm files/rp/{cmd}.txt')
            with open('files/rp_cmd.txt','r+') as f:
                edited = f.read().replace(cmd,"")
                f.write(edited)
            await ctx.send(f'> removed {cmd}')
        else:
            print(f"{ctx.author.name}({ctx.author.id}) tried to use remrp command")

def setup(bot):
    bot.add_cog(Rp(bot))
    print('---> ROLEPLAY LOADED')

