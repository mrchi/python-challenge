# coding=utf-8

import bz2
import keyword
from io import BytesIO


import requests
from PIL import Image

url = "http://butter:fly@www.pythonchallenge.com/pc/hex/zigzag.gif"
resp = requests.get(url)

with Image.open(BytesIO(resp.content)) as image:
    print(image.n_frames, image.mode, image.size)
    size = image.size
    palette = bytes(image.getpalette()[::3])
    table = bytes.maketrans(bytes(range(256)), palette)

    origin = image.tobytes()
    trans = origin.translate(table)
    print(origin[:20])
    print(trans[:20])

new = Image.new("1", size=size)
new.putdata([i == j for i, j in zip(origin[1:], trans[:-1])])
new.show()

# clue
# - not keyword
# - busy -> bzip

data = bytes(i for i, j in zip(origin[1:], trans[:-1]) if i != j)
result = bz2.decompress(data).decode()

for i in set(result.split()):
    if not keyword.iskeyword(i):
        print(i)

# print and exec is keyword in python2
username = "repeat"
password = "switch"
print(f"http://{username}:{password}@www.pythonchallenge.com/pc/ring/bell.html")
