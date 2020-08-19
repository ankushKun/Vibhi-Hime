import discord
from discord.ext import commands
import os
from decouple import config


print("---> BOT is waking up\n")

bot = commands.Bot(command_prefix=["v!","V!","<@745167619253993543> "],case_insensitive=True)
bot.remove_command('help')

def load_cogs():
    if os.path.isdir('./anime-rp-gifs'):
        os.system('cd anime-rp-gifs')
        os.system('git pull https://github.com/ATCtech/anime-rp-gifs.git')
        os.system('cd ..')
    else:
        os.system('git clone https://github.com/ATCtech/anime-rp-gifs.git')
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
    print(f'---> Logged in as : {bot.user.name} , ID : {bot.user.id}')
    print(f'---> Total Servers : {len(bot.guilds)}\n')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Anime"))
    load_cogs()
    print('\n---> BOT is awake\n')
    
    
bot.run(config('BOT_TOKEN'))
