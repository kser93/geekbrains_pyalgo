"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

import math
import random

row_len = random.randint(1, 10)
col_len = random.randint(1, 10)

a = [[random.randint(-100, 100) for _ in range(row_len)] for _ in range(col_len)]

for row in a:
    for el in row:
        print(f'{el:>4}', end=' ')

    print()

print('-'*5*len(a[0]))

column_min_values = [+math.inf] * len(a[0])
for row in a:
    for i, el in enumerate(row):
        if el < column_min_values[i]:
            column_min_values[i] = el

for el in column_min_values:
    print(f'{el:>4}', end=' ')

print('\n', '-'*5*len(a[0]), sep='')


max_el = -math.inf
for el in column_min_values:
    if el > max_el:
        max_el = el

print(max_el)
