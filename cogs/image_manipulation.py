import discord
from discord.ext import commands
from PIL import Image, ImageSequence
from io import BytesIO
import requests
import os


class IMGM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def splitimg(self, ctx):
        print("cmd run")
        if len(ctx.message.attachments) > 0:
            size = 1000, 500  # 2:1 ratio
            url = requests.get(ctx.message.attachments[0].url)
            im = Image.open(BytesIO(url.content))
            if str(ctx.message.attachments[0].filename).endswith(".gif"):
                left, right = [], []

                for fn in range(0, im.n_frames):
                    im.seek(fn)
                    a = im.copy().resize(size)
                    b = a
                    l = a.crop((0, 0, 500, 500))
                    r = b.crop((500, 0, 1000, 500))
                    left.append(l)
                    right.append(r)

                left[0].save(
                    f"images/generated/{ctx.author.id}_left.gif",
                    save_all=True,
                    append_images=left,
                )
                right[0].save(
                    f"images/generated/{ctx.author.id}_right.gif",
                    save_all=True,
                    append_images=right,
                )

                # upload on discord
                file = [
                    discord.File(
                        f"images/generated/{ctx.author.id}_left.gif", filename="pic.gif"
                    ),
                    discord.File(
                        f"images/generated/{ctx.author.id}_right.gif",
                        filename="pic.gif",
                    ),
                ]
                await ctx.send("left", file=file[0])
                await ctx.send("right", file=file[1])
                # CLEAR SPACE
                os.system(f"rm -rf images/generated/{ctx.author.id}_left.gif")
                os.system(f"rm -rf images/generated/{ctx.author.id}_right.gif")
            else:
                a = im.copy().resize(size)
                b = a
                l = a.crop((0, 0, 500, 500))
                r = b.crop((500, 0, 1000, 500))
                l.save(f"images/generated/{ctx.author.id}_left.png")
                r.save(f"images/generated/{ctx.author.id}_right.png")

                # upload on discord
                file = [
                    discord.File(
                        f"images/generated/{ctx.author.id}_left.png", filename="pic.png"
                    ),
                    discord.File(
                        f"images/generated/{ctx.author.id}_right.png",
                        filename="pic.png",
                    ),
                ]
                await ctx.send("left", file=file[0])
                await ctx.send("right", file=file[1])
                # CLEAR SPACE
                os.system(f"rm -rf images/generated/{ctx.author.id}_left.png")
                os.system(f"rm -rf images/generated/{ctx.author.id}_right.png")
        else:
            await ctx.send("you need to upload an image too :<")


def setup(bot):
    bot.add_cog(IMGM(bot))
    print("---> IMAGE MANIP LOADED")
