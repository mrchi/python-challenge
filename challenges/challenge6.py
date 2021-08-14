# coding=utf-8

from zipfile import ZipFile
from io import BytesIO
import re

import requests

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
regex = re.compile(r"Next nothing is (\d+)")


def parse_next_nothing(content):
    result = regex.match(content)
    if result:
        return result.groups()[0]
    else:
        return None


def collect_nothing_num_and_comment(zip: ZipFile, filename: str):
    comments = []
    while True:
        comments.append(zip.getinfo(f"{filename}.txt").comment)

        with zip.open(f"{filename}.txt", "r") as f:
            result = parse_next_nothing(f.read().decode())
            if result:
                filename = result
            else:
                break
    return comments


def main(filename: str):
    resp = requests.get(url)
    with ZipFile(BytesIO(resp.content)) as zip:
        resp = collect_nothing_num_and_comment(zip, filename)
    return b"".join(resp).decode()


if __name__ == "__main__":
    print(main("90052"))
    # hockey
    # oxygen
    print("http://www.pythonchallenge.com/pc/def/oxygen.html")
