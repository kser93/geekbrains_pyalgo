"""По введенным пользователем координатам двух точек вывести уравнение прямой
вида y = kx + b, проходящей через эти точки.
Предположение - вводятся валидные данные"""

x0 = float(input('x0: '))
y0 = float(input('y0: '))
x1 = float(input('x1: '))
y1 = float(input('y1: '))
a = y0 - y1
b = x1 - x0
c = x0 * y1 - x1 * y0

if a == 0 and b == 0:
    raise ValueError('Для определения уравнения прямой нужны две точки')
elif b == 0:
    print(f'x = {-c/a:.2}')
else:
    if a == 0:
        print(f'y = {-c/b:.2}')
    elif c == 0:
        print(f'y = {-a/b:.2}x')
    else:
        print(f'y = {-a/b:.2}x + {-c/b:.2}')
