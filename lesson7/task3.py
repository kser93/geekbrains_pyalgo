"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы."""

import random


def kth(a, k):
    if k == 0:
        return min(a)
    if k == len(a) - 1:
        return max(a)
    pivot_pos = random.randrange(len(a))
    a[0], a[pivot_pos] = a[pivot_pos], a[0]
    lesser, greater = [el for el in a[1:] if el <= a[0]], [el for el in a[1:] if el > a[0]]
    if len(lesser) == k:
        return a[0]
    elif len(lesser) > k:
        return kth(lesser, k)
    elif len(lesser) < k:
        return kth(greater, k - len(lesser) - 1)


if __name__ == '__main__':
    n = random.randrange(50)
    a = random.sample(range(-100, 100), 2 * n + 1)
    print(a)
    median = kth(a, n)
    print(f'Median:\t{median}')
    print(f'Check:\t{sorted(a)[n]}')
