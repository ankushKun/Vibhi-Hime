from PIL import Image, ImageSequence
from io import BytesIO
import requests
import os


size = 1000, 500  # 2:1 ratio

url = requests.get(
    "https://cdn.discordapp.com/avatars/821387163144945734/a_e6a9d2565c8fd8823611c55bf27d6edb.gif?size=1024"
)
im = Image.open(BytesIO(url.content))
frames = ImageSequence.Iterator(im)

left, right = [], []


for fn in range(0, im.n_frames):
    im.seek(fn)
    a = im.copy().resize(size)
    b = a
    l = a.crop((0, 0, 500, 500))
    r = b.crop((500, 0, 1000, 500))
    left.append(l)
    right.append(r)

left[0].save("left.gif", save_all=True, append_images=left)
right[0].save("right.gif", save_all=True, append_images=right)
