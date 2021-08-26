# coding=utf-8

import csv
from io import StringIO


import requests
from PIL import Image

url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.csv"
resp = requests.get(url)

data = []
reader = csv.reader(StringIO(resp.text))
for line in reader:
    for i in line:
        if i:
            data.append(i.strip())
print(data[:20])
print(len(data))

# 7367 = 53 * 139

image = Image.new(mode="F", size=(53, 139))
image.putdata([float(i) for i in data], scale=256)
image = image.transpose(Image.ROTATE_270)
image = image.transpose(Image.FLIP_LEFT_RIGHT)
image.show()

result = []
for x, y, z in zip(data[::3], data[1::3], data[2::3]):
    value = int(str(x[5]) + str(y[5]) + str(z[6]))
    result.append(value)
print(bytes(result))

answer = "grandpa"
print(f"http://repeat:switch@www.pythonchallenge.com/pc/ring/{answer}.html")
