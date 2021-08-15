# coding=utf-8

from io import BytesIO

import requests
from PIL import Image

url = "http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg"

resp = requests.get(url)
with Image.open(BytesIO(resp.content)) as im:
    w, h = im.size

    images = [Image.new(im.mode, (w, h)) for _ in range(4)]

    for i in range(w):
        for j in range(h):
            if i % 2 == 0 and j % 2 == 0:
                images[0].putpixel((i, j), im.getpixel((i, j)))
            elif i % 2 != 0 and j % 2 == 0:
                images[1].putpixel((i, j), im.getpixel((i, j)))
            elif i % 2 == 0 and j % 2 != 0:
                images[2].putpixel((i, j), im.getpixel((i, j)))
            elif i % 2 != 0 and j % 2 != 0:
                images[3].putpixel((i, j), im.getpixel((i, j)))

    for image in images:
        image.show()


answer = "evil"
print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
