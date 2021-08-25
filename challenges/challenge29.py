# coding=utf-8

import bz2

import requests

url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html"
resp = requests.get(url)
lines = resp.text.split("\n")

space_counts_data = bytes(len(line) for line in lines[12:])
print(space_counts_data)

result = bz2.decompress(space_counts_data).decode()
print(result)

answer = "yankeedoodle"
print(f"http://repeat:switch@www.pythonchallenge.com/pc/ring/{answer}.html")
