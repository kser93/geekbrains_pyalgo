"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import math
import random

a = [random.randint(1, 100) for _ in range(random.randint(1, 100))]
print(a)

min_index, min_val = None, +math.inf
max_index, max_val = None, -math.inf
for i, el in enumerate(a):
    if el > max_val:
        max_index, max_val = i, el
    if el < min_val:
        min_index, min_val = i, el

print(f'Swap {min_index}-th and {max_index}-th...')
a[min_index], a[max_index] = a[max_index], a[min_index]
print(a)
