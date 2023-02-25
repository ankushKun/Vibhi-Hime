import discord
from discord.ext import commands, tasks
import os
from decouple import config


print("---> BOT is waking up\n")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix=["v!", "V!"], case_insensitive=True, intents=intents
)
bot.remove_command("help")


def unload_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            try:
                bot.unload_extension(f"cogs.{file[:-3]}")
            except Exception as e:
                print(f"COG UNLOAD ERROR : {e}")


def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            try:
                bot.load_extension(f"cogs.{file[:-3]}")
            except Exception as e:
                print(f"COG LOAD ERROR : {e}")


@tasks.loop(seconds=240)
async def presence_change():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="https://Vibhi.me\n\nWebsite made by my senpai <3",
        )
    )
    await discord.utils.sleep_until(60)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Anime with weeblet senpai"
        )
    )
    await discord.utils.sleep_until(120)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="Anime Openings"
        )
    )
    await discord.utils.sleep_until(180)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name="with weeblet~kun <3"
        )
    )
    await discord.utils.sleep_until(240)


@bot.command(aliases=["reload"])
@commands.is_owner()
async def reload_cogs(ctx):
    unload_cogs()
    await ctx.send("> Vibhi unloaded cogs")
    load_cogs()
    await ctx.send("> Vibhi loaded cogs")


@bot.command()
async def invite(ctx):
    emb = discord.Embed(title="INVITE **Vibhi**", color=0xFF0055)
    inv = "[Invite link](https://discord.com/api/oauth2/authorize?client_id=746984468199374908&permissions=8&scope=bot)"
    emb.add_field(name="direct invite ", value=inv, inline=False)
    await ctx.send(embed=emb)


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency, 3) * 1000}ms")


@bot.command()
async def say(ctx):
    if ctx.author.id == 666578281142812673:
        await ctx.send(ctx.message.content[5:])
        await ctx.message.delete()


@bot.event
async def on_ready():
    print(f"---> Logged in as : {bot.user.name} , ID : {bot.user.id}")
    print(f"---> Total Servers : {len(bot.guilds)}\n")
    presence_change.start()
    load_cogs()
    print("\n---> BOT is awake\n")


bot.run(config("BOT_TOKEN"))
