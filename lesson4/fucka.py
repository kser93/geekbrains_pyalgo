import cProfile
import random
import timeit


def swap_classic(a):
    minimum = min(a)
    maximum = max(a)
    min_index = a.index(minimum)
    max_index = a.index(maximum)
    a[min_index], a[max_index] = a[max_index], a[min_index]
    return a


def swap_naive(a):
    minimum = maximum = 0
    for i in range(len(a)):
        if a[i] < a[minimum]:
            minimum = i
        elif a[i] > a[maximum]:
            maximum = i

    b = a[minimum]
    a[minimum] = a[maximum]
    a[maximum] = b
    return a


def swap_infunc(a):
    def finding_indecies(ind):
        min_index = max_index = 0
        for i in range(len(ind)):
            if ind[i] < ind[min_index]:
                min_index = i
            elif ind[i] > ind[max_index]:
                max_index = i

        return [min_index, max_index]

    def swapping_indicies(ind, min_index, max_index):
        ind[max_index], ind[min_index] = ind[min_index], ind[max_index]

    indicies = finding_indecies(a)
    swapping_indicies(a, min_index=indicies[0], max_index=indicies[1])
    return a


if __name__ == '__main__':
    func_list = (swap_classic, swap_naive, swap_infunc)

    # perform cProfile profiling
    for n in (2 ** i for i in range(10, 20)):
        a = [random.randint(0, n // 2) for _ in range(n)]
        print(f'[[N = {n}]]')
        for func in func_list:
            profiler = cProfile.Profile()  # context manager works in python 3.8+
            profiler.enable()
            _ = func(a)
            profiler.disable()
            print(func.__name__)
            profiler.print_stats()

    # perform timeit profiling
    for n in (2 ** i for i in range(10, 20)):
        a = [random.randint(0, n // 2) for _ in range(n)]
        print(f'{n:>8}', end='\t')
        repetitions = 100
        for func in func_list:
            exec_time = timeit.timeit(f'_ = {func.__name__}(a)', number=repetitions, globals=globals())
            print(f'{func.__name__}: {exec_time / repetitions:.8f}', end='\t')

        print()

# timeit report (number=100)
#     1024	swap_classic: 0.00004414	swap_naive: 0.00010860	swap_infunc: 0.00010288
#     2048	swap_classic: 0.00008953	swap_naive: 0.00021384	swap_infunc: 0.00021158
#     4096	swap_classic: 0.00016395	swap_naive: 0.00043018	swap_infunc: 0.00042337
#     8192	swap_classic: 0.00035503	swap_naive: 0.00086683	swap_infunc: 0.00094276
#    16384	swap_classic: 0.00071049	swap_naive: 0.00178225	swap_infunc: 0.00179252
#    32768	swap_classic: 0.00136617	swap_naive: 0.00352195	swap_infunc: 0.00346821
#    65536	swap_classic: 0.00236395	swap_naive: 0.00711907	swap_infunc: 0.00734778
#   131072	swap_classic: 0.00629691	swap_naive: 0.01405812	swap_infunc: 0.01383288
#   262144	swap_classic: 0.01508046	swap_naive: 0.02839586	swap_infunc: 0.02831233
#   524288	swap_classic: 0.02142368	swap_naive: 0.05609469	swap_infunc: 0.05636208
