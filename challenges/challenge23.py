# coding=utf-8

import this
import string

message = "va gur snpr bs jung?"

# see this module of Python
table = str.maketrans(
    string.ascii_lowercase, string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
)
clue = message.translate(table)
print(clue)

answer = "ambiguity"
print(f"http://butter:fly@www.pythonchallenge.com/pc/hex/{answer}.html")
