from PIL import Image
import requests
from io import BytesIO

gif1 = "https://cdn.discordapp.com/avatars/746984468199374908/1472def3c4ffce98ed96764e740af9b4.png?size=256"
gif2 = "https://cdn.discordapp.com/avatars/746984468199374908/1472def3c4ffce98ed96764e740af9b4.png?size=256"

i1 = requests.get(gif1)
i2 = requests.get(gif2)

im1 = Image.open(BytesIO(i1.content))
im2 = Image.open(BytesIO(i2.content))

GIFS = [im1, im2]

frames = []

s = len(GIFS)
d = 250
bg = Image.new(mode="RGBA", size=(d * s, d))

for gif in GIFS:
    f = []
    while True:
        try:
            gif.seek(gif.tell() + 1)
            f.append(gif.copy().resize((d, d)))
        except:
            frames.append(f)
            break


frames_imgs = []
s = len(frames)
f_no = 0
while True:
    i = 0
    brk = False
    bg = Image.new(mode="RGBA", size=(d * s, d))
    for x in range(0, s):
        try:
            bg.paste(frames[i][f_no], (d * x, 0))
            i += 1
            frames_imgs.append(bg)
        except Exception as e:
            print(e, i)
            brk = True
    f_no += 1
    if brk:
        break

print(frames_imgs)
frames_imgs[0].save(
    "ok.gif", save_all=True, append_images=frames_imgs[:-1], loop=0, quality=1
)
