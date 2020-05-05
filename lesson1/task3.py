"""Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
Предположение - вводятся валидные данные"""

import random
mode = input('Выберите режим генерации:\n\t* a - целое число\n\t* b - вещественное число\n\t* c - символ\n>')

start = input('Начало диапазона: ')
end = input('Конец диапазона: ')

if mode is 'a':
    start, end = int(start), int(end)
    print(random.randint(start, end))
elif mode is 'b':
    start, end = float(start), float(end)
    print(random.uniform(start, end))
else:  # mode is 'c'
    start, end = ord(start[0]), ord(end[0])
    print(chr(random.randint(start, end)))
