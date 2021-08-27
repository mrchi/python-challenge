# coding=utf-8

from io import BytesIO


import requests
from PIL import Image

# Search image in Google, it's hin ta & hin yai rock in Koh Samui, Thailand
# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/grandpa.html

url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/mandelbrot.gif"
left = 0.34
top = 0.57
width = 0.036
height = 0.027
iterations = 128

resp = requests.get(url)
with Image.open(BytesIO(resp.content)) as image:
    w, h = image.size
    mode = image.mode
    palette = image.palette
    image_data = image.getdata()
    image.show()
    image2 = image.copy()

# Mandelbrot set
data = []
for y in range(h - 1, -1, -1):
    for x in range(w):
        c = complex(left + x / w * width, top + y / h * height)
        z = complex(0, 0)
        for i in range(iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                break
        data.append(i)

image2.putdata(data)
image.show()

diff = [p1 - p2 for p1, p2 in zip(image_data, data) if p1 != p2]
print(len(diff), diff[:10])
# len(diff) = 1679 = 23 * 73

diff_image = Image.new("1", (23, 73))
diff_image.putdata([i > 0 for i in diff])
diff_image.resize((230, 730)).show()
# The image is Arecibo Message

answer = "arecibo"
print(f"http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/{answer}.html")
