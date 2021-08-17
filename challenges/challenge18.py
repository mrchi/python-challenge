# coding=utf-8

import gzip
import difflib

import requests

clue = "brightness"
print(f"http://www.pythonchallenge.com/pc/return/{clue}.html")

url = "http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz"
resp = requests.get(url)

file = gzip.decompress(resp.content).decode()
