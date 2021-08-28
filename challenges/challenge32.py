# coding=utf-8

from nonogram_cracker import solve

# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/warmup.txt
warmup_horizontal = """
2 1 2
1 3 1
5

7
9
3

2 3 2
2 3 2
2 3 2
"""

warmup_vertical = """
2 1 3
1 2 3
3

8
9
8

3
1 2 3
2 1 3
"""


def read_numbers(lines: str):
    resp = []
    for line in lines.split("\n"):
        if not line:
            continue
        resp.append([int(i) for i in line.split()])
    return resp


result = solve(
    {
        "name": "warmup",
        "rows": read_numbers(warmup_horizontal),
        "cols": read_numbers(warmup_vertical),
    }
)
for line in result["solution"]:
    print(line)


# http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.txt
up_horizontal = """
3 2
8
10
3 1 1

5 2 1
5 2 1
4 1 1
15

19
6 14
6 1 12
6 1 10

7 2 1 8
6 1 1 2 1 1 1 1
5 1 4 1
5 4 1 4 1 1 1

5 1 1 8
5 2 1 8
6 1 2 1 3
6 3 2 1

6 1 5
1 6 3
2 7 2
3 3 10 4

9 12 1
22 1
21 4
1 17 1

2 8 5 1
2 2 4
5 2 1 1
5
"""

up_vertical = """
5
5
5
3 1

3 1
5
5
6

5 6
9 5
11 5 1
13 6 1

14 6 1
7 12 1
6 1 11 1
3 1 1 1 9 1

3 4 10
8 1 1 2 8 1
10 1 1 1 7 1
10 4 1 1 7 1

3 2 5 2 1 2 6 2
3 2 4 2 1 1 4 1
2 6 3 1 1 1 1 1
12 3 1 2 1 1 1

3 2 7 3 1 2 1 2
2 6 3 1 1 1 1
12 3 1 5
6 3 1

6 4 1
5 4
4 1 1
5
"""

print("-" * 30)

result = solve(
    {
        "name": "up",
        "rows": read_numbers(up_horizontal),
        "cols": read_numbers(up_vertical),
    }
)
for line in result["solution"]:
    print(line)

# answer is "python"
# Go to http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/python.html
# "Free" as in "Free speech", not as in "free beer"
answer = "beer"
print(f"http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/{answer}.html")
