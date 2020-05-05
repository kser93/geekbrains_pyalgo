"""Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

num = int(input('Input number: '))
evens, odds = 0, 0
while num > 0:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

    num //= 10

print(f'Четных:\t{evens}')
print(f'Нечетных:\t{odds}')