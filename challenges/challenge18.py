# coding=utf-8

import gzip
import difflib
import binascii
from io import BytesIO

import requests
from PIL import Image


clue = "brightness"
print(f"http://www.pythonchallenge.com/pc/return/{clue}.html")

url = "http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz"
resp = requests.get(url)

file = gzip.decompress(resp.content).decode()

left = []
right = []
for line in file.split("\n"):
    left.append(line[:53])
    right.append(line[56:])
result = difflib.Differ().compare(left, right)

added = []
deleted = []
other = []
for i in result:
    data = i[2:].split()
    if i.startswith("+"):
        added.extend(data)
    elif i.startswith("-"):
        deleted.extend(data)
    else:
        other.extend(data)

for collection in [added, deleted, other]:
    bytes = binascii.unhexlify("".join(collection))
    Image.open(BytesIO(bytes)).show()

username = "butter"
password = "fly"
url = f"http://{username}:{password}@www.pythonchallenge.com/pc/hex/bin.html"
print(url)
