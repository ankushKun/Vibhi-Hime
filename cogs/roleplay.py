import discord
from discord.ext import commands
from random import choice
import requests
import json
#import urllib
from os import chdir, getcwd, mkdir
import os.path
from os import path



class Rp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self,msg):
        ms= msg.content.lower()
        ms+=' '
        if 'v!' in ms:
            ms=ms[2:]
            d = os.listdir('./files/rp/')
            filename=ms[:ms.index(' ')]+".txt"
            if filename in d:
                with open(f'./files/rp/{filename}','r') as f:
                    urls=f.read().split('\n')
                gif=choice(urls)
                print(ms)
                em = discord.Embed(title='',description=f'{msg.author.mention} {ms[:ms.index(" ")]}s{ms[ms.index(" "):]}',color=0xFF0055)
                em.set_image(url=gif)
                await msg.channel.send(embed=em)
            """
            if ms[:ms.index(' ')] in d:
                ms=ms[:ms.index(' ')]
                d = os.listdir(f'./anime-rp-gifs/{ms}')
                fil=f'./anime-rp-gifs/{ms}/'+choice(d)
                
                im = discord.File(fil,filename='rp.gif')
                em.set_image(url='attachment://rp.gif')
                )"""

    @commands.command()
    async def updategif(self,ctx,amt=25):
        await ctx.send('updating ...')
        API_KEY = "M9YAESOTVOLX"

        r = requests.get(f"https://api.tenor.com/v1/anonid?&key={API_KEY}")

        rp = ['laugh','smile','cry','sad','run','punch','kill','kick','lick','poke','pat','hug','shoot','stare','die','chase']

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
            print("Failed Connection, Please try again")
            exit()

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
                with open(f'./files/rp/{search_term}.txt','w') as f:f.write(l)


            else:
                tenorjson = None
                print("Failed connection Please Try Again")
                continue
            
            await ctx.send(f"> {search_term} done")
            continue
            
            if input("Would you like to download any more files[Y or N]: ").upper() == "Y":
                continue
            else:
                #print("Thank you for using TenorDownloader.py")
                break    
        await ctx.send('OwO new gifs')         

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
    
    

def setup(bot):
    bot.add_cog(Rp(bot))
    print('---> ROLEPLAY LOADED')

