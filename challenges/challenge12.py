# coding=utf-8

from io import BytesIO

import requests
from PIL import Image

url = "http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx"

resp = requests.get(url)
content = resp.content

for i in range(5):
    bytes = resp.content[i::5]
    try:
        Image.open(BytesIO(bytes)).show()
    except:
        # image 3 is not showing
        print(f"Failed on image {i}")

answer = "disproportional"
print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
