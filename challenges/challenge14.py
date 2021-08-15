# coding=utf-8

from io import BytesIO

import requests
from PIL import Image

url = "http://huge:file@www.pythonchallenge.com/pc/return/wire.png"
resp = requests.get(url)

with Image.open(BytesIO(resp.content)) as image:
    mode = image.mode
    pixels = [image.getpixel((i, 0)) for i in range(image.size[0])]

resized_image = Image.new(mode, (100, 100))

coord = [-1, 0]
pixel_index = 0
steps = [100, 99, 99, 98]
while steps[-1] >= 0:
    # right
    for _ in range(steps[0]):
        coord[0] += 1
        resized_image.putpixel(coord, pixels[pixel_index])
        pixel_index += 1

    # down
    for _ in range(steps[1]):
        coord[1] += 1
        resized_image.putpixel(coord, pixels[pixel_index])
        pixel_index += 1

    # left
    for _ in range(steps[2]):
        coord[0] -= 1
        resized_image.putpixel(coord, pixels[pixel_index])
        pixel_index += 1

    # up
    for _ in range(steps[3]):
        coord[1] -= 1
        resized_image.putpixel(coord, pixels[pixel_index])
        pixel_index += 1

    for i in range(4):
        steps[i] -= 2

resized_image.show()

answer = "cat"
answer = "uzi"

print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
