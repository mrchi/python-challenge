# coding=utf-8

import re
import requests


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
regex = re.compile(r"and the next nothing is (\d+)")


def get_next_nothing(nothing: int):
    while True:
        print(nothing)
        resp = requests.get(url, params={"nothing": nothing})
        result = regex.findall(resp.text)
        if result:
            nothing = result[0]
        else:
            return resp.text


if __name__ == "__main__":
    # resp = get_next_nothing(12345)
    resp = get_next_nothing(16044 // 2)
    print(resp)
    print(f"http://www.pythonchallenge.com/pc/def/{resp}")
