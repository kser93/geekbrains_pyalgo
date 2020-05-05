"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

import random


def merge_sort(a):
    """MergeSort(A[N]):
    1. Sort A[:N//2]
    2. Sort A[N//2:]
    3. Merge(A[:N//2], A[N//2:])
    """
    if len(a) <= 1:
        return a
    else:
        n = len(a)//2
        return list(merge(
            iter(merge_sort(a[:n])),
            iter(merge_sort(a[n:]))
        ))


def merge(a, b):
    """a, b are iterators to sorted sequences"""

    try:
        a_val = next(a)
    except StopIteration:
        yield from b
        return

    try:
        b_val = next(b)
    except StopIteration:
        yield a_val
        yield from a
        return

    while True:
        if a_val <= b_val:
            yield a_val
            try:
                a_val = next(a)
            except StopIteration:
                yield b_val
                yield from b
                return
        else:
            yield b_val
            try:
                b_val = next(b)
            except StopIteration:
                yield a_val
                yield from a
                return


if __name__ == '__main__':
    n = random.randrange(50)
    a = random.sample(range(50), n)
    print(a)
    print(merge_sort(a))
