import random
import operator

from copy import copy


def bubble_sort(a, func=operator.gt, reverse=False):
    a = copy(a)
    is_sorted = True
    for i in range(len(a), 0, -1):
        for j in range(i - 1):
            cmp = not func(a[j], a[j + 1]) if reverse else func(a[j], a[j + 1])
            if cmp:
                is_sorted = False
                a[j], a[j + 1] = a[j + 1], a[j]

        if is_sorted:
            break

    return a


def bubble_sort_recursive(a, func=operator.gt, reverse=False):
    a = copy(a)
    is_sorted = True
    for j in range(len(a) - 1):
        cmp = not func(a[j], a[j + 1]) if reverse else func(a[j], a[j + 1])
        if cmp:
            is_sorted = False
            a[j], a[j + 1] = a[j + 1], a[j]

    return a if is_sorted else bubble_sort_recursive(a[:-1], func) + [a[-1]]


def bubble_sort_bool(a, func=operator.gt, reverse=False):
    a, n = copy(a), len(a)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(n - 1):
            cmp = not func(a[j], a[j + 1]) if reverse else func(a[j], a[j + 1])
            if cmp:
                is_sorted = False
                a[j], a[j + 1] = a[j + 1], a[j]

        n -= 1

    return a


if __name__ == '__main__':
    a = random.sample(range(10 ** 2), 10)
    print(a)
    print(bubble_sort(a, reverse=True))
    print(bubble_sort_recursive(a))
    print(bubble_sort_bool(a))
