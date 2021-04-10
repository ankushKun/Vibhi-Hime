import discord
from discord.ext import commands
import os
from decouple import config
from discord.ext.tasks import loop
from asyncio import sleep


print("---> BOT is waking up\n")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=["v!", "V!"], case_insensitive=True, intents=intents)
bot.remove_command("help")


def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")


@loop(seconds=240)
async def presence_change():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Anime")
    )
    await sleep(60)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="Pokemon")
    )
    await sleep(60)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="Anime Openings"
        )
    )
    await sleep(60)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.streaming, name="Anime")
    )
    await sleep(60)


@bot.event
async def on_ready():
    print(f"---> Logged in as : {bot.user.name} , ID : {bot.user.id}")
    print(f"---> Total Servers : {len(bot.guilds)}\n")
    # presence_change.start()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name="with weeblet~kun"
        )
    )
    load_cogs()
    print("\n---> BOT is awake\n")


bot.run(config("BOT_TOKEN"))
