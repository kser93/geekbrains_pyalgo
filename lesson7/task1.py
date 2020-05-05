"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы."""

import random


def bubble_sort_bool(a, reverse=False):
    n = len(a)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(n - 1):
            cmp = a[j] < a[j + 1] if reverse else a[j] >= a[j + 1]
            if cmp:
                is_sorted = False
                a[j], a[j + 1] = a[j + 1], a[j]

        n -= 1


if __name__ == '__main__':
    n = random.randrange(100)
    a = random.sample(range(-100, 100), n)
    print(a)
    bubble_sort_bool(a, reverse=True)
    print(a)
