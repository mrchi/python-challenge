# coding=utf-8

from io import BytesIO

import requests
from PIL import Image

url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.png"
resp = requests.get(url)

with Image.open(BytesIO(resp.content)) as image:
    print(image.mode, image.size)
    width, height = image.size
    # ring-ring-ring -> green
    green_channel = list(image.getdata(1))

diffs = []
for i in range(0, len(green_channel), 2):
    diff = abs(green_channel[i + 1] - green_channel[i])
    if diff != 42:
        diffs.append(diff)

print("".join(chr(i) for i in diffs))

# whodunnit().split()[0] ?
# who (has) done it -> Guido van Rossum
answer = "guido van rossum".split()[0]
print(f"http://repeat:switch@www.pythonchallenge.com/pc/ring/{answer}.html")
