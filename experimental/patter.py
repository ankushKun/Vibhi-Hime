from PIL import Image
import requests
from io import BytesIO

avatar = "https://cdn.discordapp.com/avatars/666578281142812673/a_1b06d5740908c76eee92fe99a33d2e80.gif?size=1024"

i1 = requests.get(avatar)
im1 = Image.open(BytesIO(i1.content)).resize((500, 500)).convert("RGBA")


pat_gif = Image.open("images/pat.gif")
pat_frames = []

d = 500
y_pos = [100, 110, 120, 130, 140, 130, 120, 110, 100]

while True:
    try:
        pat_gif.seek(pat_gif.tell() + 1)
        f = pat_gif.copy().resize((d, d)).convert("RGBA")
        pat_frames.append(f)
    except:
        break

print(len(pat_frames))

final_frames = []

p = 0
for y in y_pos:
    blank = Image.new("RGBA", (500, 500))
    blank.paste(im1.resize((400, 500 - y)), (100, y))  # pastes avatar
    blank.paste(pat_frames[p], (0, 0), pat_frames[p])
    final_frames.append(blank)
    p += 1

final_frames[0].save(
    "ok.gif",
    type="GIF",
    save_all=True,
    append_images=final_frames[:],
    loop=0,
    quality=1,
    duration=pat_gif.info["duration"],
    format="GIF",
)
