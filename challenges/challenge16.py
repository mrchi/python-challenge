# coding=utf-8

from io import BytesIO

import requests
from PIL import Image

url = "http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif"
resp = requests.get(url)

with Image.open(BytesIO(resp.content)) as image:
    reformed_image = Image.new(image.mode, image.size)
    reformed_image.palette = image.palette

    for h in range(image.size[1]):
        before_flag_pixels = []
        after_flag_pixels = []
        flag_found = False
        for w in range(image.size[0]):
            if flag_found:
                after_flag_pixels.append(image.getpixel((w, h)))
            else:
                before_flag_pixels.append(image.getpixel((w, h)))

            if before_flag_pixels[-5:] == [195, 195, 195, 195, 195]:
                flag_found = True

        i = 0
        for pixel in after_flag_pixels + before_flag_pixels:
            reformed_image.putpixel((i, h), pixel)
            i += 1

    reformed_image.show()

answer = "romance"
print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
