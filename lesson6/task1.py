"""Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть); проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
(Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;)
d. написать общий вывод: какой из трёх вариантов лучше и почему.

Выбрана задача 3.4:
Определить, какое число в массиве встречается чаще всего."""

from collections import Counter
import gc
import random
import sys


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

    return val, count


def most_frequent_sort(a):
    val = sorted(a, key=a.count, reverse=True)[0]
    count = a.count(val)
    return val, count


def most_frequent_counter(a):
    return Counter(a).most_common(1)[0]


_ = most_frequent_counter([0])  # need to rid out outlying first call where Counter statics initialized
func_list = [most_frequent_reference, most_frequent_sort, most_frequent_counter]


class LocalsTracer:
    def __init__(self, traced_functions):
        self.memory_usage = 0
        self.traced_functions = traced_functions
        self.found_ids = set()

    def __call__(self, *args, **kwargs):
        return self.call_tracer(*args)

    def call_tracer(self, frame, event, arg):
        if event is 'call' and frame.f_code.co_name in self.traced_functions:
            return self.local_tracer

    def local_tracer(self, frame, event, arg):
        if event is not 'line':
            return
        memory_usage = sum(map(sys.getsizeof, frame.f_locals.values()))
        self.found_ids |= set(map(id, frame.f_locals.values()))
        self.memory_usage = max(self.memory_usage, memory_usage)


if __name__ == '__main__':
    gc.disable()
    print(sys.version, sys.platform)
    _ = Counter()
    for n in (2 ** i for i in range(0, 21)):
        a = [random.randint(0, n // 2) for _ in range(n)]
        print(f'Input len is {n} elements ({sys.getsizeof(a)} bytes)')
        for func in func_list:
            tracer = LocalsTracer(map(lambda func: func.__name__, func_list))
            sys.settrace(tracer)
            before = gc.get_objects()
            result = func(a)
            after = gc.get_objects()
            sys.settrace(None)

            before, after = set(map(id, before)), set(map(id, after))
            objects = (obj for obj in gc.get_objects() if id(obj) in after - before - tracer.found_ids)
            locals_mem = tracer.memory_usage
            garbage_mem = sum(map(sys.getsizeof, objects))
            print(f'{func.__name__} uses {locals_mem + garbage_mem} bytes')


# Python version: 3.7.3 (Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
# Platform: win32
# Memory profile
# + ------+-----------+-------------------------+--------------------+-----------------------+
# |     N | input_len | most_frequent_reference | most_frequent_sort | most_frequent_counter |
# + ------+-----------+-------------------------+--------------------+-----------------------+
# |     1 |        96 |                     528 |                212 |                   160 |
# |     2 |        96 |                     536 |                212 |                   160 |
# |     4 |        96 |                     540 |                216 |                   160 |
# |     8 |       128 |                     568 |                248 |                   192 |
# |    16 |       192 |                     764 |                312 |                   256 |
# |    32 |       344 |                    1196 |                464 |                   408 |
# |    64 |       640 |                    2028 |                760 |                   704 |
# |   128 |      1248 |                    3732 |               1368 |                  1312 |
# |   256 |      2216 |                    7124 |               2336 |                  2280 |
# |   512 |      4272 |                   13796 |               4392 |                  4336 |
# |  1024 |      9024 |                   27756 |               9144 |                  9088 |
# |  2048 |     16560 |                   53732 |              16680 |                 16624 |
# |  4096 |     33928 |                  107956 |              34048 |                 33992 |
# |  8192 |     69160 |                  216924 |              69280 |                 69224 |
# | 16384 |    140584 |                  435796 |             140704 |                140648 |
# | 32768 |    285384 |                  875516 |             285504 |                285448 |
# | 65536 |    578936 |                 1889956 |             579056 |                579000 |
# + ------+-----------+-------------------------+--------------------+-----------------------+

# Из профиля использования памяти видно, что функции most_frequent_sort и most_frequent_counter потребляют схожее
# количество памяти, причем большую часть этой памяти занимают входные данные. Функция most_frequent_reference
# потребляет приблизительно в 3 раза больше памяти; предполагаю, это связано с использованием словаря для подсчета.
# Исходя из профиля памяти можно предложить использование реализации на основе коллекции Counter - помимо наименьшего
# использования памяти, она также является самой простой.
