import cProfile
import functools


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def fib_memo_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n not in fib_d:
            fib_d[n] = _fib_dict(n-1) + _fib_dict(n-2)

        return fib_d[n]

    return _fib_dict(n)


def fib_memo_list(n):
    fib_l = [None] * 1000
    fib_l[0] = 0
    fib_l[1] = 0

    def _fib_list(n):
        if n >= 1000:
            raise ValueError('fuck stack')
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n-1) + _fib_list(n-2)

        return fib_l[n]

    return _fib_list(n)


def fib_loop(n):
    if n == 0:
        return 0

    fib_prev, fib_cur = 0, 1
    for _ in range(2, n+1):
        fib_prev, fib_cur = fib_cur, fib_prev + fib_cur

    return fib_cur


# for i in range(100):
#     x, y = fib_loop(i), fib(i)
#     if x != y:
#         print(x, '!=', y)
#     else:
#         print(x, '==', y)

# cProfile.run('fib_memo_dict(500)')
# cProfile.run('fib_memo_list(500)')
# cProfile.run('fib_loop(50000)')
