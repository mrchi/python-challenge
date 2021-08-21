# coding=utf-8

from io import BytesIO
from zipfile import ZipFile

import requests
from PIL import Image

url = "http://butter:fly@www.pythonchallenge.com/pc/hex/maze.png"
resp = requests.get(url)

start_coord = (639, 0)
end_coords = (1, 640)
visited = {}
queue = [start_coord]

with Image.open(BytesIO(resp.content)) as image:
    while queue:
        w, h = queue.pop()
        if (w, h) == end_coords:
            break
        for coord in [(w - 1, h), (w + 1, h), (w, h - 1), (w, h + 1)]:
            if not (0 <= coord[0] < image.size[0]):
                continue
            if not (0 <= coord[1] < image.size[1]):
                continue
            if coord in visited:
                continue
            if image.getpixel(coord) in [(255, 255, 255, 255), (127, 127, 127, 255)]:
                continue
            queue.insert(0, coord)
            visited[coord] = (w, h)

    coord = end_coords
    path = [image.getpixel(coord)[0]]
    while coord != start_coord:
        parent = visited.get(coord)
        path.append(image.getpixel(parent)[0])
        coord = parent

with ZipFile(BytesIO(bytes(path[-2::-2]))) as zip:
    print(zip.filelist)
    with zip.open("maze.jpg") as f:
        with Image.open(f) as img:
            img.show()

answer = "lake"
print(f"http://butter:fly@www.pythonchallenge.com/pc/hex/{answer}.html")
