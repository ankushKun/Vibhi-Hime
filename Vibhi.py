import discord
from discord.ext import commands
import os
from decouple import config


print("---> BOT is waking up\n")

bot = commands.Bot(command_prefix=["w!","V!"],case_insensitive=True)
bot.remove_command('help')

def load_cogs():
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
    

bot.run(config('NzU0NjM3MzQ2MTc0OTI2OTY4.X13oyw.NDc1ldMyPyt2S3TQGkV-SvWCnHk'))
