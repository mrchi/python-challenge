# coding=utf-8

import bz2

username = (
    b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!"
    b"\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
)
password = (
    b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<"
    b"]\xc9\x14\xe1BBP\x91\xf08"
)

username = bz2.decompress(username).decode()
password = bz2.decompress(password).decode()
print(f"http://{username}:{password}@www.pythonchallenge.com/pc/return/good.html")
