"""Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту."""

import cProfile
import math
import timeit


def prime_dummy(n):
    primes100 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
    if 0 <= n < len(primes100):
        return primes100[n]
    else:
        raise ValueError('dunno such big prime')


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def prime(n):
    cur = 1
    while n > 0:
        cur += 1
        if is_prime(cur):
            n -= 1

    return cur


def sieve(n):
    if n == 0:
        return 1

    primes = [0, 0]
    while True:
        primes.extend(range(len(primes), 2 * len(primes)))

        primes_count = 0
        for i, prime_candidate in enumerate(primes):
            if prime_candidate != 0:
                primes_count += 1
                if primes_count == n:
                    return prime_candidate

                for j in range(2 * i, len(primes), i):
                    primes[j] = 0


if __name__ == '__main__':
    func_list = (prime, sieve)

    for func in func_list:
        for i in range(101):
            if func(i) != prime_dummy(i):
                raise ValueError(f'{func.__name__}: {func(i)} != {prime_dummy(i)}')

    for n in (2 ** i for i in range(5, 13)):
        print(f'[[N = {n}]]')
        for func in func_list:
            profiler = cProfile.Profile()  # context manager works in python 3.8+
            profiler.enable()
            _ = func(n)
            profiler.disable()
            print(func.__name__)
            profiler.print_stats()

    for n in (2 ** i for i in range(13)):
        print(f'{n:>8}', end='\t')
        repetitions = 100
        for func in func_list:
            exec_time = timeit.timeit(f'_ = {func.__name__}(n)', number=repetitions, globals=globals())
            print(f'{func.__name__}: {exec_time / repetitions:.8f}', end='\t')

        print()

# timeit report (number=100)
#        N         prime         sieve
#       32    0.00012799    0.00009000
#       64    0.00033121    0.00019338
#      128    0.00082396    0.00045708
#      256    0.00199901    0.00085949
#      512    0.00479391    0.00177744
#     1024    0.01125151    0.00357714
#     2048    0.02747420    0.01372373
#     4096    0.06893351    0.02792275

# cProfile report
# [[N = 32]]
# prime
#          392 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       130    0.000    0.000    0.000    0.000 task2.py:27(is_prime)
#         1    0.000    0.000    0.000    0.000 task2.py:37(prime)
#       130    0.000    0.000    0.000    0.000 {built-in method math.floor}
#       130    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          126 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task2.py:47(sieve)
#       117    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         7    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 64]]
# prime
#          932 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       310    0.000    0.000    0.000    0.000 task2.py:27(is_prime)
#         1    0.000    0.000    0.000    0.000 task2.py:37(prime)
#       310    0.000    0.000    0.000    0.000 {built-in method math.floor}
#       310    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          215 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task2.py:47(sieve)
#       205    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         8    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 128]]
# prime
#          2156 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       718    0.001    0.000    0.001    0.000 task2.py:27(is_prime)
#         1    0.000    0.000    0.001    0.001 task2.py:37(prime)
#       718    0.000    0.000    0.000    0.000 {built-in method math.floor}
#       718    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          379 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task2.py:47(sieve)
#       368    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         9    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 256]]
# prime
#          4856 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1618    0.002    0.000    0.002    0.000 task2.py:27(is_prime)
#         1    0.000    0.000    0.003    0.003 task2.py:37(prime)
#      1618    0.000    0.000    0.000    0.000 {built-in method math.floor}
#      1618    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          682 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.001    0.001 task2.py:47(sieve)
#       670    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        10    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 512]]
# prime
#          11012 function calls in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      3670    0.004    0.000    0.005    0.000 task2.py:27(is_prime)
#         1    0.001    0.001    0.006    0.006 task2.py:37(prime)
#      3670    0.001    0.000    0.001    0.000 {built-in method math.floor}
#      3670    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          1250 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.002    0.002 task2.py:47(sieve)
#      1237    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        11    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 1024]]
# prime
#          24482 function calls in 0.014 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      8160    0.009    0.000    0.012    0.000 task2.py:27(is_prime)
#         1    0.002    0.002    0.014    0.014 task2.py:37(prime)
#      8160    0.002    0.000    0.002    0.000 {built-in method math.floor}
#      8160    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          2329 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.004    0.004    0.004    0.004 task2.py:47(sieve)
#      2315    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 2048]]
# prime
#          53588 function calls in 0.034 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     17862    0.023    0.000    0.030    0.000 task2.py:27(is_prime)
#         1    0.004    0.004    0.034    0.034 task2.py:37(prime)
#     17862    0.004    0.000    0.004    0.000 {built-in method math.floor}
#     17862    0.003    0.000    0.003    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          6287 function calls in 0.014 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.013    0.013    0.014    0.014 task2.py:47(sieve)
#      6271    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        14    0.001    0.000    0.001    0.000 {method 'extend' of 'list' objects}
#
#
# [[N = 4096]]
# prime
#          116618 function calls in 0.107 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     38872    0.081    0.000    0.099    0.000 task2.py:27(is_prime)
#         1    0.009    0.009    0.107    0.107 task2.py:37(prime)
#     38872    0.010    0.000    0.010    0.000 {built-in method math.floor}
#     38872    0.007    0.000    0.007    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# sieve
#          11850 function calls in 0.038 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.035    0.035    0.038    0.038 task2.py:47(sieve)
#     11833    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        15    0.002    0.000    0.002    0.000 {method 'extend' of 'list' objects}

# Видно, что функция sieve работает быстрее функции prime, хотя использует дополнительную память.
