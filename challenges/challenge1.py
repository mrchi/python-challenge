# coding=utf-8

import string

mapper = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + "ab")

data = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
    "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
)
print(data.translate(mapper))

print(f"http://www.pythonchallenge.com/pc/def/{'map'.translate(mapper)}.html")
