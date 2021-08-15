# coding=utf-8

import datetime

result = []
for year in range(1006, 1997, 10):
    if year % 4 != 0:
        continue
    if datetime.date(year, 1, 27).isoweekday() != 2:
        continue
    result.append(year)

# he ain't the youngest, he is the second
print(result[-2])  # 1756-01-27

answer = "mozart"
print(f"http://www.pythonchallenge.com/pc/return/{answer}.html")
