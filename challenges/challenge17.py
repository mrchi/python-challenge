# coding=utf-8

import re
import bz2
from urllib.parse import unquote_to_bytes
from xmlrpc.client import ServerProxy

import requests


# challenge 4
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
regex = re.compile(r"the next busynothing is (\d+)")

busynothing = "12345"
cookie_data = []
while True:
    print(busynothing)
    resp = requests.get(url, params={"busynothing": busynothing})

    cookie = resp.cookies["info"]
    cookie_data.append(cookie)

    result = regex.findall(resp.text)
    if result:
        busynothing = result[0]
    else:
        print(resp.text)
        break

clue = unquote_to_bytes("".join(cookie_data).replace("+", "%20"))
print(clue)


# challenge 8
message = bz2.decompress(clue).decode()
print(message)


# challenge 15
father = "Leopold"


# challenge 13
url = "http://www.pythonchallenge.com/pc/phonebook.php"
with ServerProxy(url) as proxy:
    number = proxy.phone(father)
print(number)


# challenge 17
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
resp = requests.get(url, cookies={"info": "the flowers are on their way"})
print(resp.text)
# oh well, don't you dare to forget the balloons.

answer = "balloons"
print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
