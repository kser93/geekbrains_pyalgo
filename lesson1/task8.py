"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
Предположение - вводятся валидные данные"""

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if (b - a) * (c - a) < 0:
    print(a)
elif (a - b) * (c - b) < 0:
    print(b)
else:
    print(c)