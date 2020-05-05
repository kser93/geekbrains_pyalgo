"""Определить, какое число в массиве встречается чаще всего."""

import random

a = [random.randint(1, 10) for _ in range(random.randint(11, 100))]
print(a)

viewed = dict()
for el in a:
    if el not in viewed:
        viewed[el] = 1
    else:
        viewed[el] += 1

most_often, el = 0, None
for k, v in viewed.items():
    if v > most_often:
        most_often = v
        el = k

print(f'{el} found {most_often} times')
