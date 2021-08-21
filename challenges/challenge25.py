# coding=utf-8

import wave
from io import BytesIO

import requests
from PIL import Image

url = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake{num}.wav"

images = []
for i in range(1, 26):
    resp = requests.get(url.format(num=i))
    with wave.open(BytesIO(resp.content)) as wav:
        content = wav.readframes(wav.getnframes())
    img = Image.frombytes("RGB", (60, 60), content)
    img.show()
    images.append(img)

bigimg = Image.new("RGB", (300, 300))
for h in range(5):
    for w in range(5):
        bigimg.paste(images[h * 5 + w], (w * 60, h * 60))
bigimg.show()

answer = "decent"
print(f"http://butter:fly@www.pythonchallenge.com/pc/hex/{answer}.html")
