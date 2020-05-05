"""Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках ДЗ первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N проводились замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Выбрана задача 3.4:
Определить, какое число в массиве встречается чаще всего."""

import cProfile
import random
import timeit


def most_frequent_reference(a):
    viewed = dict()
    for el in a:
        if el not in viewed:
            viewed[el] = 1
        else:
            viewed[el] += 1

    count, val = 0, None
    for k, v in viewed.items():
        if v > count:
            count = v
            val = k

    return count, val


def most_frequent_sort(a):
    val = sorted(a, key=a.count, reverse=True)[0]
    count = a.count(val)
    return count, val


def most_frequent_counter(a):
    from collections import Counter
    return Counter(a).most_common(1)[0]


if __name__ == '__main__':

    func_list = (most_frequent_reference, most_frequent_counter, most_frequent_sort)
    for func in func_list:
        print(func.__name__)

        for n in (2 ** i for i in range(9, 21)):
            a = [random.randint(0, n // 2) for _ in range(n)]
            print(f'[[N = {n}]]')
            profiler = cProfile.Profile()  # context manager works in python 3.8+
            profiler.enable()
            _ = func(a)
            profiler.disable()
            profiler.print_stats()

        for n in (2 ** i for i in range(9, 21)):
            print(f'{n:>8}', end='\t')
            a = [random.randint(0, n // 2) for _ in range(n)]
            repetitions = 100
            exec_time = timeit.timeit(f'_ = {func.__name__}(a)', number=repetitions, globals=globals())
            print(f'{exec_time / repetitions:.8f}')

# timeit report (number=100)
#        N     reference       counter          sort
#     1024    0.00013266    0.00010104    0.01838510
#     2048    0.00026463    0.00021014    0.07353417
#     4096    0.00055518    0.00038643    0.29546663
#     8192    0.00127724    0.00094637    1.16712531
#    16384    0.00259318    0.00199334    4.64790758
#    32768    0.00540676    0.00407684    *
#    65536    0.01193362    0.00930157    *
#   131072    0.02712572    0.02148338    *
#   262144    0.05999375    0.05175475    *
#   524288    0.13976366    0.12200542    *
#  1048576    0.32905318    0.28370278    *

# Вывод cProfile сохранен в отдельных тестовых файлах ввиду их большого размера относительно кода.
# Наилучшие результаты показала функция most_frequent_counter, использующая стандартную реализацию счетчика вхождения.
# Примечание. Профиль функции most_frequent_sort я не стал доводить до конца, поскольку видно, что эта функция
# выполняется гораздо дольше остальных реализаций (most_frequent_reference и most_frequent_counter за O(n),
# most_frequent_sort за O(n*log(n))).
