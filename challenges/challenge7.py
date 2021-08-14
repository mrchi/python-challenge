# coding=utf-8

from io import BytesIO

import requests
from PIL import Image

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
resp = requests.get(url)

with Image.open(BytesIO(resp.content)) as image:
    greyscale = image.convert("L")

w, h = greyscale.size
y = greyscale.size[1] // 2

pixels = []
for x in range(0, w, 7):
    pixel = greyscale.getpixel((x, y))
    pixels.append(pixel)

print("".join(chr(i) for i in pixels))

data = [105, 110, 116, 101, 103, 114, 105, 116, 121]
answer = "".join(chr(i) for i in data)
print(f"http://www.pythonchallenge.com/pc/def/{answer}.html")
