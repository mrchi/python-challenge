# coding=utf-8


def calc_nth_a(n):
    nth = "1"
    for _ in range(n):
        temp = []
        num = nth[0]
        count = 1
        for i in nth[1:]:
            if i == num:
                count += 1
            else:
                temp.append(f"{count}{num}")
                count = 1
                num = i
        temp.append(f"{count}{num}")
        nth = "".join(temp)
    return nth


length = len(calc_nth_a(30))
print(f"http://www.pythonchallenge.com/pc/return/{length}.html")
