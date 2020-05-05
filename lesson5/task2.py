"""Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import defaultdict, deque
from functools import reduce
from random import randint


def test_data():
    low_boundary, high_boundary = 0, 1000000
    a = randint(low_boundary, high_boundary)
    b = randint(low_boundary, high_boundary)
    return list(hex(a)[2:].upper()), list(hex(b)[2:].upper())


def user_data():
    a = input('First hexadecimal number: >')
    b = input('Second hexadecimal number: >')
    return list(a.upper()), list(b.upper())


def add_digit(d0, d1, carry='0'):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    i_sum = digits.index(d0) + digits.index(d1) + digits.index(carry)
    carry, result = digits[i_sum // len(digits)], digits[i_sum % len(digits)]
    return carry, result


def mul_digit(d0, d1, carry='0'):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    i_sum = digits.index(d0) * digits.index(d1) + digits.index(carry)
    carry, result = digits[i_sum // len(digits)], digits[i_sum % len(digits)]
    return carry, result


def add_numbers(a, b):
    a = defaultdict(lambda: '0', enumerate(reversed(a)))
    b = defaultdict(lambda: '0', enumerate(reversed(b)))

    # do not inline because defultdict changes its len implicitly on misaccess
    add_result = deque()
    carry = '0'
    for i in range(max(len(a), len(b))):
        carry, sum_digit = add_digit(a[i], b[i], carry)
        add_result.appendleft(sum_digit)

    add_result.appendleft(carry)
    while add_result[0] == '0':
        add_result.popleft()
    return list(add_result)


def mul_numbers(a, b):
    a = defaultdict(lambda: '0', enumerate(reversed(a)))
    b = defaultdict(lambda: '0', enumerate(reversed(b)))

    window_len = max(len(a), len(b))
    partials = list()
    for i in range(window_len):
        partial = deque('0' * i)
        carry = '0'
        for j in range(window_len):
            carry, digit = mul_digit(a[j], b[i], carry)
            partial.appendleft(digit)
        partial.appendleft(carry)
        partials.append(list(partial))

    result = reduce(add_numbers, partials)
    while result[0] == '0':
        result.pop(0)
    return result


if __name__ == '__main__':
    use_test_data = False  # swap to use user input or random data
    if use_test_data:
        a, b = test_data()
    else:
        a, b = user_data()

    print(f'{a} + {b} = {add_numbers(a, b)}')
    print(f'{a} * {b} = {mul_numbers(a, b)}')

    a, b = int(''.join(a), base=16), int(''.join(b), base=16)
    print('Check:')
    print(f'{a:0x} + {b:0x} = {a + b:0x}')
    print(f'{a:0x} * {b:0x} = {a * b:0x}')
