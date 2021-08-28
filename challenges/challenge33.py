# coding=utf-8

import math
from io import BytesIO

import requests
from PIL import Image

url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer2.png"
resp = requests.get(url)

with Image.open(BytesIO(resp.content)) as image:
    print(image.mode, image.size)
    image.show()
    data = image.getdata()

# remove ligit pixel
# remained numbers count are square numbers
for limit in sorted(list(set(data)), reverse=True):
    ashes = [i == limit for i in data if i <= limit]
    squre_root = int(math.sqrt(len(ashes)))
    if squre_root ** 2 == len(ashes) and squre_root > 0:
        image = Image.new("1", (squre_root, squre_root))
        image.putdata(ashes)
        image.show()

answer = "gremlins"

print(f"http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/{answer}.html")
