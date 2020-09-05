import requests
import json
import urllib
from os import chdir, getcwd, mkdir
import os.path
from os import path

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
    limit = 50
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
    
    print(f"> {search_term} done")
    continue
    
    if input("Would you like to download any more files[Y or N]: ").upper() == "Y":
        continue
    else:
         #print("Thank you for using TenorDownloader.py")
         break
        
