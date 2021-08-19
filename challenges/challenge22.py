# coding=utf-8

from io import BytesIO

import requests
from PIL import Image, ImageDraw


url = "http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif"
resp = requests.get(url)


def joystick(image):
    for w in range(98, 103):
        for h in range(98, 103):
            if image.getpixel((w, h)) == 8:
                return w - 100, h - 100


patterns = []
with Image.open(BytesIO(resp.content)) as image:
    for i in range(image.n_frames):
        image.seek(i)
        move = joystick(image)
        if move == (0, 0):
            patterns.append([(100, 100)])
        else:
            w, h = patterns[-1][-1]
            patterns[-1].append((w + move[0], h + move[1]))

for pattern in patterns:
    im = Image.new(image.mode, image.size, color="white")
    drawer = ImageDraw.Draw(im)
    drawer.line(pattern, fill="red")
    im.show()

answer = "bonus"
print(f"http://www.pythonchallenge.com/pc/hex/{answer}.html")
